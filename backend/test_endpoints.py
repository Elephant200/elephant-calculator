import pytest
from fastapi.testclient import TestClient
from api import app  # Replace with the name of your FastAPI app file

client = TestClient(app)

# VECTORS
def test_add_vectors():
    response = client.post("/api/vectors/add", json={"vector1": [1, 2, 3], "vector2": [4, 5, 6]})
    assert response.status_code == 200
    assert response.json() == [5, 7, 9]

def test_add_vectors_empty():
    response = client.post("/api/vectors/add", json={"vector1": [], "vector2": []})
    assert response.status_code == 422  # Validation error

def test_add_vectors_mismatched_dimensions():
    response = client.post("/api/vectors/add", json={"vector1": [1, 2], "vector2": [3, 4, 5]})
    assert response.status_code == 422  # Validation error

def test_scale_vector_negative_scalar():
    response = client.post("/api/vectors/scale", json={"vector": [1, -2, 3], "scalar": -2})
    assert response.status_code == 200
    assert response.json() == [-2, 4, -6]

def test_dot_product_zeros():
    response = client.post("/api/vectors/dot", json={"vector1": [0, 0, 0], "vector2": [0, 0, 0]})
    assert response.status_code == 200
    assert response.json() == 0


# MATRICES
def test_add_matrices():
    response = client.post(
        "/api/matrices/add", 
        json={"matrix1": [[1, 2], [3, 4]], "matrix2": [[5, 6], [7, 8]]}
    )
    assert response.status_code == 200
    assert response.json() == [[6, 8], [10, 12]]

def test_subtract_matrices_large_numbers():
    response = client.post(
        "/api/matrices/subtract",
        json={"matrix1": [[1000, 2000], [3000, 4000]], "matrix2": [[500, 600], [700, 800]]}
    )
    assert response.status_code == 200
    assert response.json() == [[500, 1400], [2300, 3200]]

def test_matrix_determinant_invalid():
    # Invalid case: Non-square matrix
    print("Starting non-square matrix test")
    response = client.post(
        "/api/matrices/determinant",
        json={"matrix": [[1, 2, 3], [4, 5, 6]]}  # Not square
    )
    print("================================================================")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 400  # Ensure validation catches this

def test_matrix_determinant_valid():
    # Valid case: Square matrix
    response = client.post(
        "/api/matrices/determinant",
        json={"matrix": [[1, 2], [3, 4]]}
    )
    assert response.status_code == 200
    assert response.json() == -2  # Expected determinant


# PRIME NUMBERS
def test_is_prime_true():
    response = client.post("/api/primes/is_prime", json={"number": 29})
    assert response.status_code == 200
    assert response.json() is True

def test_is_prime_false():
    response = client.post("/api/primes/is_prime", json={"number": 28})
    assert response.status_code == 200
    assert response.json() is False

def test_nth_prime_large():
    response = client.post("/api/primes/nth_prime", json={"n": 100})
    assert response.status_code == 200
    assert response.json() == 541

def test_prime_factorization():
    response = client.post("/api/primes/factorization", json={"number": 120})
    assert response.status_code == 200
    assert response.json() == "2^3 * 3 * 5"


# GEOMETRY
def test_circle_area_large_radius():
    response = client.post("/api/geometry/area/circle", json={"radius": 100})
    assert response.status_code == 200
    assert abs(response.json() - 31415.92653589793) < 1e-6  # π * r^2

def test_polygon_area_invalid_sides():
    response = client.post("/api/geometry/area/polygon", json={"sides": 2, "side_length": 10})
    assert response.status_code == 422  # Validation error


# TRIANGLE SOLVER
def test_triangle_solver():
    response = client.post("/api/triangles/solve", json={"a": 6, "b": 4, "c": 5})
    print("Elephant")
    assert response.status_code == 200
    result = response.json()
    assert result["A"] == 36.87
    assert result["B"] == 53.13
    assert result["C"] == 90.0


# HIGH PRECISION
def test_add_high_precision():
    response = client.post(
        "/api/irrationals/add", 
        json={"operand1": "123456789123456789", "operand2": "987654321987654321"}
    )
    assert response.status_code == 200
    assert response.json() == "1111111111111111110"

def test_sqrt_precision():
    response = client.post("/api/irrationals/sqrt", json={"operand": "16"})
    assert response.status_code == 200
    assert float(response.json()) == 4.0

def test_pi_precision():
    response = client.get("/api/irrationals/pi?precision=50")
    assert response.status_code == 200
    # Verify the first 20 digits of π for higher precision
    assert response.json().startswith("3.14159265358979323846264")

def test_e_precision():
    response = client.get("/api/irrationals/e?precision=50")
    assert response.status_code == 200
    # Verify the first 20 digits of e for higher precision
    assert response.json().startswith("2.71828182845904523536028")

# PYTHAGOREAN TRIPLES
def test_pythagorean_triples_large():
    response = client.post("/api/pythagorean/generate", json={"max_hypotenuse": 50})
    assert response.status_code == 200
    #print(response)
    assert (3, 4, 5) in response.json(), response.json()
    assert (6, 8, 10) in response.json()

def test_pythagorean_triples_invalid():
    response = client.post("/api/pythagorean/generate", json={"max_hypotenuse": -1})
    assert response.status_code == 422  # Validation error

