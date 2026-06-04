import requests

base_url = "http://localhost:8000/api"

# ====================================
# Geometry: Area Calculation Tests
# ====================================

def test_circle_area_invalid_radius():
    response = requests.post(f"{base_url}/geometry/area/circle", json={"radius": -5})
    assert response.status_code == 400
    assert "Radius must be greater than zero." in response.json()["detail"]
    print("test_circle_area_invalid_radius passed.")

def test_rectangle_area_valid():
    response = requests.post(f"{base_url}/geometry/area/rectangle", json={"length": 10, "width": 5})
    assert response.status_code == 200
    assert response.json() == 50
    print("test_rectangle_area_valid passed.")

def test_rectangle_area_invalid_dimensions():
    response = requests.post(f"{base_url}/geometry/area/rectangle", json={"length": 10})
    assert response.status_code == 400
    assert "Field required" in response.json()["detail"]
    print("test_rectangle_area_invalid_dimensions passed.")

# ====================================
# Irrationals: High-Precision Calculations
# ====================================

def test_sqrt_valid():
    response = requests.post(f"{base_url}/irrationals/sqrt", json={"operand": "16"})
    assert response.status_code == 200
    assert float(response.json()) == 4
    print("test_sqrt_valid passed.")

def test_sqrt_invalid_operand():
    response = requests.post(f"{base_url}/irrationals/sqrt", json={"operand": "abc"})
    assert response.status_code == 400
    assert "Invalid operand" in response.json()["detail"]
    print("test_sqrt_invalid_operand passed.")

def test_compute_pi_precision():
    response = requests.get(f"{base_url}/irrationals/pi?precision=10")
    assert response.status_code == 200
    assert response.json().startswith("3.1415926")
    print("test_compute_pi_precision passed.")

def test_compute_pi_invalid_precision():
    response = requests.get(f"{base_url}/irrationals/pi?precision=-5")
    assert response.status_code == 400
    assert "Precision must be positive" in response.json()["detail"]
    print("test_compute_pi_invalid_precision passed.")

# ====================================
# Primes: Prime Number Operations
# ====================================

def test_is_prime_invalid_number():
    response = requests.post(f"{base_url}/primes/is_prime", json={"number": -7})
    assert response.status_code == 400
    assert "Number must be greater than 1 to check for primality." in response.json()["detail"]
    print("test_is_prime_invalid_number passed.")

def test_prime_factorization_invalid():
    response = requests.post(f"{base_url}/primes/factorization", json={"number": 0})
    assert response.status_code == 400
    assert "Number must be greater than 1 for factorization." in response.json()["detail"]
    print("test_prime_factorization_invalid passed.")

def test_prime_list_valid():
    response = requests.post(f"{base_url}/primes/list_primes", json={"count": 10})
    assert response.status_code == 200
    assert response.json() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print("test_prime_list_valid passed.")

def test_prime_list_invalid():
    response = requests.post(f"{base_url}/primes/list_primes", json={"count": 0})
    assert response.status_code == 400
    assert "The count must be a positive integer." in response.json()["detail"]
    print("test_prime_list_invalid passed.")

# ====================================
# CAS: Algebra System Operations
# ====================================

def test_cas_simplify_valid():
    response = requests.post(f"{base_url}/cas/simplify", json={"expression": "x^2 + 2x + 1"})
    assert response.status_code == 200
    assert response.json() == "x^2 + 2x + 1"
    print("test_cas_simplify_valid passed.")

def test_cas_simplify_invalid_expression():
    response = requests.post(f"{base_url}/cas/simplify", json={"expression": "x + "})
    assert response.status_code == 400
    assert "Invalid mathematical expression" in response.json()["detail"]
    print("test_cas_simplify_invalid_expression passed.")

def test_cas_integral_valid():
    response = requests.post(f"{base_url}/cas/integrate", json={"expression": "x^2", "variable": "x"})
    assert response.status_code == 200
    assert response.json() == "x^3/3"
    print("test_cas_integral_valid passed.")

def test_cas_integral_invalid():
    response = requests.post(f"{base_url}/cas/integrate", json={"expression": "x^2"})
    assert response.status_code == 400
    assert "Field required" in response.json()["detail"]
    print("test_cas_integral_invalid passed.")

# ====================================
# Triangle Solver Tests
# ====================================

def test_triangle_solver_invalid():
    response = requests.post(f"{base_url}/triangles/solve", json={"a": 3, "b": None, "c": None})
    assert response.status_code == 400
    assert "At least three parameters, including one side, must be provided." in response.json()["detail"]
    print("test_triangle_solver_invalid passed.")

def test_triangle_solver_right_triangle():
    response = requests.post(f"{base_url}/triangles/solve", json={"a": 3, "b": 4, "C": 90})
    assert response.status_code == 200
    assert response.json() == {
        "a": 3.0,
        "b": 4.0,
        "c": 5.0,
        "A": 36.87,
        "B": 53.13,
        "C": 90.0
    }
    print("test_triangle_solver_right_triangle passed.")

def main():
    test_circle_area_invalid_radius()
    test_rectangle_area_valid()
    test_rectangle_area_invalid_dimensions()
    test_sqrt_valid()
    test_sqrt_invalid_operand()
    test_compute_pi_precision()
    test_compute_pi_invalid_precision()
    test_is_prime_invalid_number()
    test_prime_factorization_invalid()
    test_prime_list_valid()
    test_prime_list_invalid()
    test_cas_simplify_valid()
    test_cas_simplify_invalid_expression()
    test_cas_integral_valid()
    test_cas_integral_invalid()
    test_triangle_solver_invalid()
    test_triangle_solver_right_triangle()

if __name__ == "__main__":
    print("Starting API tests...\n")
    main()
    print("\nAll tests passed successfully.")