"""Regression tests for bugs fixed while hardening the API.

Each test pins a previously-broken endpoint so the failure can't silently
return. Values are checked against known-good references.
"""

import math

import pytest
from fastapi.testclient import TestClient

from elephant_calculator_api.main import app

# raise_server_exceptions=False so the app's exception handlers (which turn
# ValueError into a 400 response) are exercised instead of re-raising.
client = TestClient(app, raise_server_exceptions=False)


# ---- Geometry ----

def test_cylinder_volume_works():
    r = client.post("/api/geometry/volume/cylinder", json={"radius": 3, "height": 7})
    assert r.status_code == 200
    assert r.json() == pytest.approx(math.pi * 9 * 7)


def test_cylinder_volume_requires_height():
    r = client.post("/api/geometry/volume/cylinder", json={"radius": 3})
    assert r.status_code == 400


def test_cone_surface_area_works():
    r = client.post("/api/geometry/surface_area/cone", json={"radius": 3, "height": 7})
    assert r.status_code == 200


def test_trapezoid_perimeter_uses_legs():
    r = client.post(
        "/api/geometry/perimeter/trapezoid",
        json={"base1": 8, "base2": 5, "height": 4, "leg1": 4.5, "leg2": 5},
    )
    assert r.status_code == 200
    assert r.json() == pytest.approx(22.5)


def test_trapezoid_perimeter_requires_legs():
    r = client.post(
        "/api/geometry/perimeter/trapezoid",
        json={"base1": 8, "base2": 5, "height": 4},
    )
    assert r.status_code == 400


def test_ellipsoid_volume_uses_three_axes():
    r = client.post(
        "/api/geometry/volume/ellipsoid",
        json={"semi_major": 3, "semi_minor": 2, "axis3": 1},
    )
    assert r.status_code == 200
    assert r.json() == pytest.approx(4 / 3 * math.pi * 3 * 2 * 1)


def test_prism_surface_area_requires_perimeter():
    ok = client.post(
        "/api/geometry/surface_area/prism",
        json={"base_area": 16, "base_perimeter": 16, "height": 10},
    )
    assert ok.status_code == 200
    assert ok.json() == pytest.approx(192.0)
    missing = client.post(
        "/api/geometry/surface_area/prism", json={"base_area": 16, "height": 10}
    )
    assert missing.status_code == 400


# ---- Matrices ----

def test_matrix_times_vector():
    r = client.post(
        "/api/matrices/multiply/vector",
        json={"matrix": [[1, 2], [3, 4]], "vector": [1, 1]},
    )
    assert r.status_code == 200
    assert r.json() == [3, 7]


def test_matrix_times_vector_dimension_mismatch():
    r = client.post(
        "/api/matrices/multiply/vector",
        json={"matrix": [[1, 2, 3], [4, 5, 6]], "vector": [1, 1]},
    )
    assert r.status_code == 400


# ---- High precision trig ----

@pytest.mark.parametrize(
    "fn,ref",
    [("sin", math.sin(1)), ("cos", math.cos(1)), ("tan", math.tan(1))],
)
def test_trig_radians(fn, ref):
    r = client.post(f"/api/irrationals/{fn}", json={"angle": "1", "radians": True})
    assert r.status_code == 200
    assert float(r.json()) == pytest.approx(ref, abs=1e-12)


@pytest.mark.parametrize(
    "fn,arg,ref",
    [
        ("arcsin", "0.5", math.asin(0.5)),
        ("arccos", "0.5", math.acos(0.5)),
        ("arctan", "1", math.atan(1)),
    ],
)
def test_inverse_trig(fn, arg, ref):
    r = client.post(f"/api/irrationals/{fn}", json={"operand": arg}, params={"precision": 30})
    assert r.status_code == 200
    assert float(r.json()) == pytest.approx(ref, abs=1e-12)


def test_divide_by_zero_is_clean_error():
    r = client.post("/api/irrationals/divide", json={"operand1": "1", "operand2": "0"})
    assert r.status_code == 400
    assert "zero" in r.json()["detail"].lower()


# ---- CAS ----

def test_solve_differential_accepts_valid_ode():
    r = client.post("/api/cas/solve-differential", json={"equation": "y' + y = 0"})
    assert r.status_code == 200
    assert "exp(-x)" in r.json().replace(" ", "")
