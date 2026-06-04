import requests

base_url = "http://localhost:8000/api"

# VECTORS
def test_add_vectors():
    response = requests.post(f"{base_url}/vectors/add", json={"vector1": [1, 2, 3], "vector2": [4, 5, 6]})
    assert response.status_code == 200
    assert response.json() == [5, 7, 9]
    print("test_add_vectors passed.")

def test_add_vectors_empty():
    response = requests.post(f"{base_url}/vectors/add", json={"vector1": [], "vector2": []})
    assert response.status_code == 400
    print("test_add_vectors_empty passed.")

def test_add_vectors_mismatched_dimensions():
    response = requests.post(f"{base_url}/vectors/add", json={"vector1": [1, 2], "vector2": [3, 4, 5]})
    assert response.status_code == 400
    print("test_add_vectors_mismatched_dimensions passed.")

def test_scale_vector_negative_scalar():
    response = requests.post(f"{base_url}/vectors/scale", json={"vector": [1, -2, 3], "scalar": -2})
    assert response.status_code == 200
    assert response.json() == [-2, 4, -6]
    print("test_scale_vector_negative_scalar passed.")

def test_dot_product_zeros():
    response = requests.post(f"{base_url}/vectors/dot", json={"vector1": [0, 0, 0], "vector2": [0, 0, 0]})
    assert response.status_code == 200
    assert response.json() == 0
    print("test_dot_product_zeros passed.")

# MATRICES
def test_add_matrices():
    response = requests.post(
        f"{base_url}/matrices/add", 
        json={"matrix1": [[1, 2], [3, 4]], "matrix2": [[5, 6], [7, 8]]}
    )
    assert response.status_code == 200
    assert response.json() == [[6, 8], [10, 12]]
    print("test_add_matrices passed.")

def test_subtract_matrices_large_numbers():
    response = requests.post(
        f"{base_url}/matrices/subtract",
        json={"matrix1": [[1000, 2000], [3000, 4000]], "matrix2": [[500, 600], [700, 800]]}
    )
    assert response.status_code == 200
    assert response.json() == [[500, 1400], [2300, 3200]]
    print("test_subtract_matrices_large_numbers passed.")


# PRIME NUMBERS
def test_is_prime_true():
    response = requests.post(f"{base_url}/primes/is_prime", json={"number": 29})
    assert response.status_code == 200
    assert response.json() is True
    print("test_is_prime_true passed.")

def test_is_prime_false():
    response = requests.post(f"{base_url}/primes/is_prime", json={"number": 28})
    assert response.status_code == 200
    assert response.json() is False
    print("test_is_prime_false passed.")

def test_nth_prime_large():
    response = requests.post(f"{base_url}/primes/nth_prime", json={"n": 100})
    assert response.status_code == 200
    assert response.json() == 541
    print("test_nth_prime_large passed.")


# GEOMETRY
def test_circle_area_large_radius():
    response = requests.post(f"{base_url}/geometry/area/circle", json={"radius": 100})
    assert response.status_code == 200
    assert abs(response.json() - 31415.92653589793) < 1e-6
    print("test_circle_area_large_radius passed.")

def test_polygon_area_invalid_sides():
    response = requests.post(f"{base_url}/geometry/area/polygon", json={"sides": 2, "side_length": 10})
    assert response.status_code == 400
    print("test_polygon_area_invalid_sides passed.")

# TRIANGLE SOLVER
def test_triangle_solver():
    response = requests.post(f"{base_url}/triangles/solve", json={"a": 6, "b": 4, "c": 5})
    assert response.status_code == 200
    result = response.json()
    assert result["A"] == 82.82
    assert result["B"] == 41.41
    assert result["C"] == 55.77
    print("test_triangle_solver passed.")

# HIGH PRECISION
def test_add_high_precision():
    response = requests.post(
        f"{base_url}/irrationals/add", 
        json={"operand1": "123456789123456789", "operand2": "987654321987654321"}
    )
    assert response.status_code == 200
    assert response.json() == "1111111111111111110"
    print("test_add_high_precision passed.")

def test_sqrt_precision():
    response = requests.post(f"{base_url}/irrationals/sqrt", json={"operand": "16"})
    assert response.status_code == 200
    assert float(response.json()) == 4.0
    print("test_sqrt_precision passed.")

def test_pi_precision():
    response = requests.get(f"{base_url}/irrationals/pi?precision=50")
    assert response.status_code == 200
    assert response.json().startswith("3.14159265358979323846264")
    print("test_pi_precision passed.")

def test_e_precision():
    response = requests.get(f"{base_url}/irrationals/e?precision=50")
    assert response.status_code == 200
    assert response.json().startswith("2.71828182845904523536028")
    print("test_e_precision passed.")

# PYTHAGOREAN TRIPLES
def test_pythagorean_triples_large():
    response = requests.post(f"{base_url}/pythagorean/generate", json={"max_hypotenuse": 50})
    assert response.status_code == 200
    assert [3, 4, 5] in response.json()
    assert [6, 8, 10] in response.json()
    print("test_pythagorean_triples_large passed.")

def test_pythagorean_triples_invalid():
    response = requests.post(f"{base_url}/pythagorean/generate", json={"max_hypotenuse": -1})
    assert response.status_code == 400
    print("test_pythagorean_triples_invalid passed.")

def main():
    test_add_vectors()
    test_add_vectors_empty()
    test_add_vectors_mismatched_dimensions()
    test_scale_vector_negative_scalar()
    test_dot_product_zeros()
    test_add_matrices()
    test_subtract_matrices_large_numbers()
    test_is_prime_true()
    test_is_prime_false()
    test_nth_prime_large()
    test_circle_area_large_radius()
    test_polygon_area_invalid_sides()
    test_triangle_solver()
    test_add_high_precision()
    test_sqrt_precision()
    test_pi_precision()
    test_e_precision()
    test_pythagorean_triples_large()
    test_pythagorean_triples_invalid()

if __name__ == "__main__":
    print("Starting API tests...\n")
    main()
    print("\nAll tests passed successfully.")
