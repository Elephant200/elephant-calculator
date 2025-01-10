import requests

BASE_URL = "http://localhost:8000/api"

# ===============================
# Geometry Endpoint Testers
# ===============================

def test_parallelogram_area():
    url = f"{BASE_URL}/geometry/area/parallelogram"
    
    # Valid request
    response = requests.post(url, json={"side1": 10, "side2": 8, "theta": 30})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert abs(response.json() - 40) < 1e-2, f"Expected area ~40, got {response.json()}"

    # Invalid: Negative side
    response = requests.post(url, json={"side1": -10, "side2": 8, "theta": 30})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Sides must be greater than zero." in response.json()["detail"]
    print("test_parallelogram_area passed.")

def test_triangle_area_heron():
    url = f"{BASE_URL}/geometry/area/triangle/heron"

    # Valid request
    response = requests.post(url, json={"side1": 3, "side2": 4, "side3": 5})
    assert response.status_code == 200, f"Expected 200, got {response.status_code} with data {response.json()}"
    assert abs(response.json() - 6) < 1e-2, f"Expected area 6, got {response.json()}"

    # Invalid: Non-triangle sides
    response = requests.post(url, json={"side1": 1, "side2": 2, "side3": 8})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Sides do not satisfy the triangle inequality." in response.json()["detail"], response.json()
    print("test_triangle_area_heron passed.")

# ===============================
# CAS Endpoint Testers
# ===============================

def test_expand_expression():
    url = f"{BASE_URL}/cas/expand"

    # Valid request
    response = requests.post(url, json={"expression": "(x + 1)^2"})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == "x^2 + 2x + 1", f"Unexpected expansion: {response.json()}"

    # Invalid request
    response = requests.post(url, json={"expression": "(x + "})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Invalid algebraic expression" in response.json()["detail"]
    print("test_expand_expression passed.")

def test_definite_integral():
    url = f"{BASE_URL}/cas/definite-integral"

    # Valid request
    response = requests.post(url, json={
        "expression": "x^2",
        "variable": "x",
        "lower_limit": "0",
        "upper_limit": "2"
    })
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == "8/3", f"Expected '8/3', got {response.json()}"

    # Invalid request: Missing limits
    response = requests.post(url, json={"expression": "x^2", "variable": "x"})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "field required" in response.json()["detail"]
    print("test_definite_integral passed.")

# ===============================
# Matrix Endpoint Testers
# ===============================

def test_matrix_addition():
    url = f"{BASE_URL}/matrices/add"

    # Valid request
    response = requests.post(url, json={
        "matrix1": [[1, 2], [3, 4]],
        "matrix2": [[5, 6], [7, 8]]
    })
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == [[6, 8], [10, 12]], f"Unexpected addition: {response.json()}"

    # Invalid: Mismatched dimensions
    response = requests.post(url, json={
        "matrix1": [[1, 2]],
        "matrix2": [[3, 4], [5, 6]]
    })
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Matrices must have the same dimensions." in response.json()["detail"]
    print("test_matrix_addition passed.")

def test_matrix_transpose():
    url = f"{BASE_URL}/matrices/transpose"

    # Valid request
    response = requests.post(url, json={"matrix": [[1, 2], [3, 4]]})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == [[1, 3], [2, 4]], f"Unexpected transpose: {response.json()}"

    # Invalid: Non-square matrix (if unsupported)
    response = requests.post(url, json={"matrix": [[1, 2, 3]]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    print("test_matrix_transpose passed.")

# ===============================
# Vector Endpoint Testers
# ===============================

def test_vector_addition():
    url = f"{BASE_URL}/vectors/add"

    # Valid request
    response = requests.post(url, json={"vector1": [1, 2, 3], "vector2": [4, 5, 6]})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == [5, 7, 9], f"Unexpected addition: {response.json()}"

    # Invalid: Different dimensions
    response = requests.post(url, json={"vector1": [1, 2], "vector2": [3, 4, 5]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "Vectors must have the same dimensions." in response.json()["detail"]
    print("test_vector_addition passed.")

def test_vector_scale():
    url = f"{BASE_URL}/vectors/scale"

    # Valid request
    response = requests.post(url, json={"vector": [1, 2, 3], "scalar": 2})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == [2, 4, 6], f"Unexpected scaling: {response.json()}"

    # Invalid: Scalar missing
    response = requests.post(url, json={"vector": [1, 2, 3]})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "field required" in response.json()["detail"]
    print("test_vector_scale passed.")

# ===============================
# Main Function to Run All Tests
# ===============================

def main():
    print("Starting API tests...")
    #test_parallelogram_area()
    test_triangle_area_heron()
    test_expand_expression()
    test_definite_integral()
    test_matrix_addition()
    test_matrix_transpose()
    test_vector_addition()
    test_vector_scale()
    print("All tests passed successfully.")

if __name__ == "__main__":
    main()
