"""Smoke tests for operations added to the calculator: statistics, number-base
conversion, combined Platonic solids, extra vector ops, and matrix trace/power."""

import math

from fastapi.testclient import TestClient

from elephant_calculator_api.main import app

# raise_server_exceptions=False so the app's exception handlers (which turn
# service-layer ValueErrors into 400s) run instead of the error re-raising.
client = TestClient(app, raise_server_exceptions=False)


# --- Statistics ------------------------------------------------------------

def test_statistics_summary_has_rich_rows() -> None:
    r = client.post("/api/statistics/summary", json={"data": [4, 8, 15, 16, 23, 42]})
    assert r.status_code == 200
    rows = {row["label"]: row["value"] for row in r.json()}
    assert rows["Count"] == "6"
    assert rows["Mean"] == "18"
    assert rows["Median"] == "15.5"
    assert rows["Range"] == "38"
    # Richer descriptive stats are present.
    for label in (
        "Lower quartile (Q1)",
        "Interquartile range",
        "Skewness",
        "Excess kurtosis",
        "Geometric mean",
    ):
        assert label in rows


def test_statistics_mean_and_mode() -> None:
    assert client.post("/api/statistics/mean", json={"data": [2, 4, 6]}).json() == 4.0
    assert client.post("/api/statistics/mode", json={"data": [2, 4, 4, 7, 7]}).json() == [4, 7]


def test_statistics_stddev_sample_vs_population() -> None:
    data = {"data": [4, 8, 15, 16, 23, 42]}
    sample = client.post("/api/statistics/standard-deviation", json={**data, "sample": True}).json()
    pop = client.post("/api/statistics/standard-deviation", json={**data, "sample": False}).json()
    assert sample > pop > 0


# --- Number bases ----------------------------------------------------------

def test_base_conversion() -> None:
    r = client.post("/api/bases/convert", json={"number": "2A", "from_base": 16})
    assert r.status_code == 200
    rows = {row["label"]: row["value"] for row in r.json()}
    assert rows["Decimal (10)"] == "42"
    assert rows["Binary (2)"] == "101010"


def test_base_conversion_rejects_invalid_digit() -> None:
    r = client.post("/api/bases/convert", json={"number": "9", "from_base": 2})
    assert r.status_code == 400


# --- Geometry: combined Platonic solid -------------------------------------

def test_regular_solid() -> None:
    r = client.post("/api/geometry/solid", json={"solid": "cube", "side": 2})
    assert r.status_code == 200
    rows = {row["label"]: row["value"] for row in r.json()}
    assert rows["Faces"] == "6"
    assert rows["Volume"] == "8"
    assert rows["Surface area"] == "24"


def test_regular_solid_rejects_unknown() -> None:
    r = client.post("/api/geometry/solid", json={"solid": "sphere", "side": 2})
    assert r.status_code == 400


# --- Vector operations -----------------------------------------------------

def test_vector_magnitude_and_normalize() -> None:
    assert client.post("/api/vectors/magnitude", json={"vector": [3, 4]}).json() == 5.0
    assert client.post("/api/vectors/normalize", json={"vector": [3, 4]}).json() == [0.6, 0.8]


def test_vector_distance_angle_projection() -> None:
    assert client.post(
        "/api/vectors/distance", json={"vector1": [0, 0], "vector2": [3, 4]}
    ).json() == 5.0
    angle = client.post(
        "/api/vectors/angle", json={"vector1": [1, 0, 0], "vector2": [1, 1, 0]}
    ).json()
    assert math.isclose(angle, 45.0, abs_tol=1e-6)
    assert client.post(
        "/api/vectors/projection", json={"vector1": [3, 4], "vector2": [1, 0]}
    ).json() == [3, 0]


def test_vector_normalize_rejects_zero() -> None:
    r = client.post("/api/vectors/normalize", json={"vector": [0, 0]})
    assert r.status_code == 400


# --- Matrix trace & power --------------------------------------------------

def test_matrix_trace() -> None:
    r = client.post("/api/matrices/trace", json={"matrix": [[1, 2], [3, 4]]})
    assert r.status_code == 200
    assert r.json() == 5


def test_matrix_power() -> None:
    r = client.post("/api/matrices/power", json={"matrix": [[1, 1], [0, 1]], "exponent": 3})
    assert r.status_code == 200
    assert r.json() == [[1, 3], [0, 1]]


def test_vector_times_vector_is_dot_product() -> None:
    # Regression: Vector.__mul__ previously called dot with the wrong arity.
    from elephant_calculator.services.vector import Vector

    assert Vector([1, 2, 3]) * Vector([4, 5, 6]) == 32
