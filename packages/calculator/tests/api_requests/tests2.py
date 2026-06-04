import requests

BASE_URL = "http://localhost:8000/api"

# ===============================
# Geometry Endpoint Testers
# ===============================

def test_trapezoid_area():
    url = f"{BASE_URL}/geometry/area/trapezoid"

    # Valid request
    response = requests.post(url, json={"base1": 10, "base2": 8, "height": 5})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == 45, f"Expected area 45, got {response.json()}"

    # Invalid: Negative base
    response = requests.post(url, json={"base1": -10, "base2": 8, "height": 5})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Base lengths and height must be greater than zero." in response.json()["detail"], response.json()
    print("test_trapezoid_area passed.")

def test_ellipse_area():
    url = f"{BASE_URL}/geometry/area/ellipse"

    # Valid request
    response = requests.post(url, json={"semi_major": 7, "semi_minor": 5})
    assert response.status_code == 200, f"Expected 200, got {response.status_code} with data {response.json()}"
    assert abs(response.json() - 109.96) < 1e-2, f"Expected area ~109.96, got {response.json()}"

    # Invalid: Missing semi_minor
    response = requests.post(url, json={"semi_major": 7})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Field required" in response.json()["detail"], response.json()
    print("test_ellipse_area passed.")

def test_cube_volume():
    url = f"{BASE_URL}/geometry/volume/cube"

    # Valid request
    response = requests.post(url, json={"side": 3})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == 27, f"Expected volume 27, got {response.json()}"

    # Invalid: Negative side length
    response = requests.post(url, json={"side": -3})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Side length must be greater than zero." in response.json()["detail"], response.json()
    print("test_cube_volume passed.")

def test_sphere_surface_area():
    url = f"{BASE_URL}/geometry/surface_area/sphere"

    # Valid request
    response = requests.post(url, json={"radius": 4})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert abs(response.json() - 201.06) < 1e-2, f"Expected area ~201.06, got {response.json()}"

    # Invalid: Missing radius
    response = requests.post(url, json={})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Field required" in response.json()["detail"], response.json()
    print("test_sphere_surface_area passed.")

# ===============================
# CAS Endpoint Testers
# ===============================

def test_factor_expression():
    url = f"{BASE_URL}/cas/factor"

    # Valid request
    response = requests.post(url, json={"expression": "x^2 - 4"})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == "(x - 2)(x + 2)", f"Unexpected factorization: {response.json()}"

    # Invalid request: Unfactorable expression
    response = requests.post(url, json={"expression": "x + "})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Invalid mathematical expression" in response.json()["detail"], response.json()
    print("test_factor_expression passed.")

# ===============================
# Matrix Endpoint Testers
# ===============================

def test_matrix_determinant_valid():
    url = f"{BASE_URL}/matrices/determinant"

    # Valid request
    response = requests.post(url, json={"matrix": [[1, 2], [3, 4]]})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == -2, f"Expected determinant -2, got {response.json()}"

    # Invalid: Non-square matrix
    response = requests.post(url, json={"matrix": [[1, 2, 3], [4, 5, 6]]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Determinant is only defined for square matrices." in response.json()["detail"], response.json()
    print("test_matrix_determinant_valid passed.")

# ===============================
# Prime Endpoint Testers
# ===============================

def test_prime_factorization():
    url = f"{BASE_URL}/primes/factorization"

    # Valid request
    response = requests.post(url, json={"number": 120})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == "2^3 * 3 * 5", f"Unexpected factorization: {response.json()}"

    # Invalid: Zero
    response = requests.post(url, json={"number": 0})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Number must be greater than 1" in response.json()["detail"], response.json()
    print("test_prime_factorization passed.")

# ===============================
# Triangle Solver Endpoint Testers
# ===============================

def test_triangle_solver_sas():
    url = f"{BASE_URL}/triangles/solve"

    # Valid request (SAS)
    response = requests.post(url, json={"a": 7, "b": 10, "C": 60})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    result = response.json()
    assert result["c"], "c not solved"
    assert result["A"], "A not solved"
    assert result["B"], "B not solved"

    # Invalid: Not enough inputs
    response = requests.post(url, json={"a": 7, "b": 10})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "At least three parameters" in response.json()["detail"], response.json()
    print("test_triangle_solver_sas passed.")

# ===============================
# Main Function to Run All Tests
# ===============================

def main():
    test_trapezoid_area()
    test_ellipse_area()
    test_cube_volume()
    test_sphere_surface_area()
    test_factor_expression()
    test_matrix_determinant_valid()
    test_prime_factorization()
    test_triangle_solver_sas()
    

if __name__ == "__main__":
    print("Starting API tests...\n")
    main()
    print("\nAll tests passed successfully.")
