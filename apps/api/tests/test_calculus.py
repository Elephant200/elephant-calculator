"""Tests for the multivariable / vector calculus endpoints."""

from fastapi.testclient import TestClient

from elephant_calculator_api.main import app

client = TestClient(app, raise_server_exceptions=False)


def _post(path, body):
    r = client.post(f"/api/calculus{path}", json=body)
    assert r.status_code == 200, r.text
    return r.json()


def test_partial_derivative():
    assert _post("/partial", {"expression": "x**3", "variable": "x", "order": 2}) == "6x"


def test_gradient():
    assert _post(
        "/gradient", {"expression": "x**2 + y**2 + z**2", "variables": "x,y,z"}
    ) == ["2x", "2y", "2z"]


def test_divergence():
    assert _post(
        "/divergence", {"field": ["x*y", "y*z", "z*x"], "variables": "x,y,z"}
    ) == "x + y + z"


def test_curl():
    assert _post(
        "/curl", {"field": ["x*y", "y*z", "z*x"], "variables": "x,y,z"}
    ) == ["-y", "-z", "-x"]


def test_curl_requires_three_dimensions():
    r = client.post("/api/calculus/curl", json={"field": ["x", "y"], "variables": "x,y"})
    assert r.status_code == 400


def test_laplacian():
    assert _post("/laplacian", {"expression": "x**2 + y**2", "variables": "x,y"}) == "4"


def test_hessian():
    assert _post("/hessian", {"expression": "x**2*y", "variables": "x,y"}) == [
        ["2y", "2x"],
        ["2x", "0"],
    ]


def test_jacobian():
    assert _post(
        "/jacobian", {"functions": ["x*y", "x+y"], "variables": "x,y"}
    ) == [["y", "x"], ["1", "1"]]


def test_double_integral():
    body = {
        "expression": "x*y", "var1": "x", "lower1": "0", "upper1": "1",
        "var2": "y", "lower2": "0", "upper2": "2",
    }
    assert _post("/double-integral", body) == "1"


def test_triple_integral_unit_cube():
    body = {
        "expression": "1", "var1": "x", "lower1": "0", "upper1": "1",
        "var2": "y", "lower2": "0", "upper2": "1",
        "var3": "z", "lower3": "0", "upper3": "1",
    }
    assert _post("/triple-integral", body) == "1"


def test_limit():
    assert _post("/limit", {"expression": "sin(x)/x", "variable": "x", "point": "0"}) == "1"


def test_taylor_series():
    assert _post(
        "/taylor-series", {"expression": "exp(x)", "variable": "x", "point": "0", "order": 5}
    ) == "x^4/24 + x^3/6 + x^2/2 + x + 1"


def test_invalid_expression_is_rejected():
    r = client.post("/api/calculus/partial", json={"expression": "x +* 2", "variable": "x"})
    assert r.status_code == 400
