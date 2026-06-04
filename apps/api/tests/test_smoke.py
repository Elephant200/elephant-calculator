from fastapi.testclient import TestClient

from elephant_calculator_api.main import app


client = TestClient(app)


def test_openapi_docs_are_available() -> None:
    response = client.get("/api/docs")
    assert response.status_code == 200


def test_vector_addition() -> None:
    response = client.post(
        "/api/vectors/add",
        json={"vector1": [1, 2, 3], "vector2": [4, 5, 6]},
    )
    assert response.status_code == 200
    assert response.json() == [5, 7, 9]


def test_prime_check() -> None:
    response = client.post("/api/primes/is_prime", json={"number": 29})
    assert response.status_code == 200
    assert response.json() is True


def test_high_precision_addition() -> None:
    response = client.post(
        "/api/irrationals/add",
        json={"operand1": "123456789123456789", "operand2": "987654321987654321"},
    )
    assert response.status_code == 200
    assert response.json() == "1111111111111111110"


def test_cas_expand() -> None:
    response = client.post("/api/cas/expand", json={"expression": "(x + 1)^2"})
    assert response.status_code == 200
    assert response.json() == "x^2 + 2x + 1"
