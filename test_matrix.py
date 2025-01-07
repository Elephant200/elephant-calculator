import requests

def test_matrix_determinant_invalid():
    url = "http://127.0.0.1:8000/api/matrices/determinant"
    payload = {"matrix": [[1, 2, 3], [4, 5, 6]]}  # Non-square matrix
    headers = {"Content-Type": "application/json"}

    print("Sending request to:", url)
    response = requests.post(url, json=payload, headers=headers)

    # Debugging output
    print("================================================================")
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)
    print("================================================================")

    # Assertions
    assert response.status_code == 400, "Expected status code 400"
    assert response.json() == {
        "detail": "Determinant is only defined for square matrices.",
        "error_type": "ValueError",
        "path": url
    }

if __name__ == "__main__":
    test_matrix_determinant_invalid()