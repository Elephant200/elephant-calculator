from fastapi import APIRouter
from models.pythagorean import PythagoreanTriplesRequest
from services.pythagorean import generate, generatePrimitive

router = APIRouter()

@router.post("/generate", response_model=list[tuple[int, int, int]])
def generate_pythagorean_triples(data: PythagoreanTriplesRequest, primitive: bool = False):
    """
    Generate Pythagorean triples up to a maximum hypotenuse.

    Args:
        data (PythagoreanTriplesRequest): Contains the maximum hypotenuse length.
        primitive (bool, optional): Whether to generate only primitive triples. Defaults to False.

    Returns:
        list[tuple[int, int, int]]: A list of Pythagorean triples as (a, b, c).
    """
    if primitive:
        return generatePrimitive(data.max_hypotenuse, printIt=False)
    return generate(data.max_hypotenuse, printIt=False)
