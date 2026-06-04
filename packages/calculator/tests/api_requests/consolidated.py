import requests

BASE_URL = "http://localhost:8000/api"

def test_add_vectors():
    url = f"{BASE_URL}/vectors/add"

    # Valid request
    response = requests.post(url, json={"vector1": [1, 2, 3], "vector2": [4, 5, 6]})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == [5, 7, 9], f"Unexpected addition: {response.json()}"

    # Empty vectors
    response = requests.post(url, json={"vector1": [], "vector2": []})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Mismatched dimensions
    response = requests.post(url, json={"vector1": [1, 2], "vector2": [3, 4, 5]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Invalid payload
    response = requests.post(url, json={"vector1": [1, 2]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    print("test_add_vectors passed.")

def test_matrix_operations():
    # Matrix addition
    add_url = f"{BASE_URL}/matrices/add"
    response = requests.post(add_url, json={"matrix1": [[1, 2], [3, 4]], "matrix2": [[5, 6], [7, 8]]})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == [[6, 8], [10, 12]], f"Unexpected addition: {response.json()}"

    # Invalid addition
    response = requests.post(add_url, json={"matrix1": [[1, 2]], "matrix2": [[1, 2], [3, 4]]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Subtraction
    subtract_url = f"{BASE_URL}/matrices/subtract"
    response = requests.post(subtract_url, json={"matrix1": [[10, 20], [30, 40]], "matrix2": [[1, 2], [3, 4]]})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == [[9, 18], [27, 36]], f"Unexpected subtraction: {response.json()}"

    # Invalid subtraction
    response = requests.post(subtract_url, json={"matrix1": [[10]], "matrix2": [[1, 2]]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Transpose
    transpose_url = f"{BASE_URL}/matrices/transpose"
    response = requests.post(transpose_url, json={"matrix": [[1, 2], [3, 4]]})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == [[1, 3], [2, 4]], f"Unexpected transpose: {response.json()}"

    # Invalid transpose
    response = requests.post(transpose_url, json={"matrix": [1, 2, 3]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Determinant
    determinant_url = f"{BASE_URL}/matrices/determinant"
    response = requests.post(determinant_url, json={"matrix": [[1, 2], [3, 4]]})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == -2, f"Unexpected determinant: {response.json()}"

    # Invalid determinant
    response = requests.post(determinant_url, json={"matrix": [[1, 2, 3], [4, 5, 6]]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    print("test_matrix_operations passed.")

def test_geometry_operations():
    # Parallelogram area
    parallelogram_url = f"{BASE_URL}/geometry/area/parallelogram"
    response = requests.post(parallelogram_url, json={"side1": 10, "side2": 8, "theta": 30})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert abs(response.json() - 40) < 1e-2, f"Unexpected parallelogram area: {response.json()}"

    # Invalid parallelogram
    response = requests.post(parallelogram_url, json={"side1": -10, "side2": 8, "theta": 30})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Trapezoid area
    trapezoid_url = f"{BASE_URL}/geometry/area/trapezoid"
    response = requests.post(trapezoid_url, json={"base1": 10, "base2": 8, "height": 5})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == 45, f"Unexpected trapezoid area: {response.json()}"

    # Invalid trapezoid
    response = requests.post(trapezoid_url, json={"base1": 10, "height": 5})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Ellipse area
    ellipse_url = f"{BASE_URL}/geometry/area/ellipse"
    response = requests.post(ellipse_url, json={"semi_major": 7, "semi_minor": 5})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert abs(response.json() - 109.96) < 1e-2, f"Unexpected ellipse area: {response.json()}"

    # Invalid ellipse
    response = requests.post(ellipse_url, json={"semi_major": 7})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Cube volume
    cube_url = f"{BASE_URL}/geometry/volume/cube"
    response = requests.post(cube_url, json={"side": 3})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == 27, f"Unexpected cube volume: {response.json()}"

    # Invalid cube
    response = requests.post(cube_url, json={"radius": 3})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Sphere surface area
    sphere_url = f"{BASE_URL}/geometry/surface_area/sphere"
    response = requests.post(sphere_url, json={"radius": 4})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert abs(response.json() - 201.06) < 1e-2, f"Unexpected sphere area: {response.json()}"

    # Invalid sphere
    response = requests.post(sphere_url, json={"radius": 4, "height": 8})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    print("test_geometry_operations passed.")

def test_triangle_solver():
    url = f"{BASE_URL}/triangles/solve"

    # SAS triangle
    response = requests.post(url, json={"a": 7, "b": 10, "C": 60})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    result = response.json()
    assert result["c"] and result["A"] and result["B"], f"Unexpected triangle result: {result}"

    # Invalid inputs
    response = requests.post(url, json={"a": 7, "b": 10})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    print("test_triangle_solver passed.")

def test_primes():
    # Prime check
    prime_url = f"{BASE_URL}/primes/is_prime"
    response = requests.post(prime_url, json={"number": 29})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() is True, f"29 should be prime."

    # Invalid prime check
    response = requests.post(prime_url, json={"number": -29})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Factorization
    factorization_url = f"{BASE_URL}/primes/factorization"
    response = requests.post(factorization_url, json={"number": 120})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == "2^3 * 3 * 5", f"Unexpected factorization: {response.json()}"

    # Invalid factorization
    response = requests.post(factorization_url, json={"number": 0})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Prime list
    list_url = f"{BASE_URL}/primes/list_primes"
    response = requests.post(list_url, json={"count": 10})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], f"Unexpected prime list: {response.json()}"

    # Invalid prime list
    response = requests.post(list_url, json={"count": -10})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    print("test_primes passed.")

def test_irrationals():
    # Pi precision
    pi_url = f"{BASE_URL}/irrationals/pi"
    response = requests.get(f"{pi_url}?precision=10")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json().startswith("3.1415926"), f"Unexpected Pi precision: {response.json()}"

    # Invalid Pi precision
    response = requests.get(f"{pi_url}?precision=-5")
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Square root
    sqrt_url = f"{BASE_URL}/irrationals/sqrt"
    response = requests.post(sqrt_url, json={"operand": "16"})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert float(response.json()) == 4, f"Unexpected square root: {response.json()}"

    # Invalid square root
    response = requests.post(sqrt_url, json={"operand": "abc"})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Addition
    add_url = f"{BASE_URL}/irrationals/add"
    response = requests.post(add_url, json={"operand1": "123456789123456789", "operand2": "987654321987654321"})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == "1111111111111111110", f"Unexpected addition: {response.json()}"

    # Invalid addition
    response = requests.post(add_url, json={"operand1": "abc", "operand2": "123"})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    print("test_irrationals passed.")

def test_cas_operations():
    # Expand expression
    expand_url = f"{BASE_URL}/cas/expand"
    response = requests.post(expand_url, json={"expression": "(x + 1)^2"})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == "x^2 + 2x + 1", f"Unexpected expansion: {response.json()}"

    # Invalid expand expression
    response = requests.post(expand_url, json={"expression": "x + "})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Factor expression
    factor_url = f"{BASE_URL}/cas/factor"
    response = requests.post(factor_url, json={"expression": "x^2 - 4"})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == "(x - 2)(x + 2)", f"Unexpected factorization: {response.json()}"

    # Invalid factor expression
    response = requests.post(factor_url, json={"expression": "x + "})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Definite integral
    integral_url = f"{BASE_URL}/cas/definite-integral"
    response = requests.post(integral_url, json={"expression": "x^2", "variable": "x", "lower_limit": 0, "upper_limit": 2})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert abs(float(response.json()) - 8/3) < 1e-4, f"Unexpected integral value: {response.json()}"

    # Invalid definite integral
    response = requests.post(integral_url, json={"expression": "x^2"})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    print("test_cas_operations passed.")

def main():
    test_add_vectors()
    test_matrix_operations()
    test_geometry_operations()
    test_triangle_solver()
    test_primes()
    test_irrationals()
    test_cas_operations()

if __name__ == "__main__":
    print("Starting API tests...\n")
    main()
    print("\nAll tests passed successfully.")
