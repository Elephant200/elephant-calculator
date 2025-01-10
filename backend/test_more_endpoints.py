import pytest
from fastapi.testclient import TestClient
from api import app  # Import your FastAPI app

client = TestClient(app)

# ====================================
# Geometry: Area Calculation Tests
# ====================================

def test_circle_area_invalid_radius():
    # Invalid: Negative radius
    response = client.post("/api/geometry/area/circle", json={"radius": -5})
    assert response.status_code == 400
    assert "Radius must be greater than zero." in response.json()["detail"]

def test_rectangle_area_valid():
    # Valid: Rectangle area
    response = client.post("/api/geometry/area/rectangle", json={"length": 10, "width": 5})
    assert response.status_code == 200
    assert response.json() == 50  # 10 * 5

def test_rectangle_area_invalid_dimensions():
    # Invalid: Missing width
    response = client.post("/api/geometry/area/rectangle", json={"length": 10})
    assert response.status_code == 400  # Validation error
    assert "field required" in response.json()["detail"][0]["msg"]

# ====================================
# Irrationals: High-Precision Calculations
# ====================================

def test_sqrt_valid():
    # Valid: Square root
    response = client.post("/api/irrationals/sqrt", json={"operand": "16"})
    assert response.status_code == 200
    assert float(response.json()) == 4

def test_sqrt_invalid_operand():
    # Invalid: Non-numeric operand
    response = client.post("/api/irrationals/sqrt", json={"operand": "abc"})
    assert response.status_code == 400
    assert "Invalid operand" in response.json()["detail"]

def test_compute_pi_precision():
    # Valid: Compute Pi with precision
    response = client.get("/api/irrationals/pi?precision=10")
    assert response.status_code == 200
    assert response.json().startswith("3.1415926")

def test_compute_pi_invalid_precision():
    # Invalid: Negative precision
    response = client.get("/api/irrationals/pi?precision=-5")
    assert response.status_code == 400
    assert "Precision must be a positive integer" in response.json()["detail"]

# ====================================
# Primes: Prime Number Operations
# ====================================

def test_is_prime_invalid_number():
    # Invalid: Negative number
    response = client.post("/api/primes/is_prime", json={"number": -7})
    assert response.status_code == 400
    assert "Number must be greater than 1 to check for primality." in response.json()["detail"]

def test_prime_factorization_invalid():
    # Invalid: Non-positive number
    response = client.post("/api/primes/factorization", json={"number": 0})
    assert response.status_code == 400
    assert "Number must be greater than 1 for factorization." in response.json()["detail"]

def test_prime_list_valid():
    # Valid: Generate a list of the first 10 primes
    response = client.post("/api/primes/list_primes", json={"count": 10})
    assert response.status_code == 200
    assert response.json() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_prime_list_invalid():
    # Invalid: Requesting 0 primes
    response = client.post("/api/primes/list_primes", json={"count": 0})
    assert response.status_code == 400
    assert "The count must be a positive integer." in response.json()["detail"]

# ====================================
# CAS: Algebra System Operations
# ====================================

def test_cas_simplify_valid():
    # Valid: Simplify algebraic expression
    response = client.post("/api/cas/simplify", json={"expression": "x^2 + 2x + 1"})
    assert response.status_code == 200
    assert response.json() == "x^2 + 2x + 1"

def test_cas_simplify_invalid_expression():
    # Invalid: Non-algebraic expression
    response = client.post("/api/cas/simplify", json={"expression": "x + "})
    assert response.status_code == 400
    assert "Invalid mathematical expression" in response.json()["detail"]

def test_cas_integral_valid():
    # Valid: Compute indefinite integral
    response = client.post("/api/cas/integrate", json={"expression": "x^2", "variable": "x"})
    assert response.status_code == 200
    assert response.json() == "x^3/3"

def test_cas_integral_invalid():
    # Invalid: Missing variable
    response = client.post("/api/cas/integrate", json={"expression": "x^2"})
    assert response.status_code == 400
    assert "field required" in response.json()["detail"][0]["msg"]

# ====================================
# Triangle Solver Tests
# ====================================

def test_triangle_solver_invalid():
    # Invalid: Less than three parameters
    response = client.post("/api/triangles/solve", json={"a": 3, "b": None, "c": None})
    assert response.status_code == 400
    assert "At least three parameters, including one side, must be provided." in response.json()["detail"]

def test_triangle_solver_right_triangle():
    # Valid: Right triangle
    response = client.post("/api/triangles/solve", json={"a": 3, "b": 4, "C": 90})
    assert response.status_code == 200
    assert response.json() == {
        "a": 3.0,
        "b": 4.0,
        "c": 5.0,
        "A": 36.87,
        "B": 53.13,
        "C": 90.0
    }
