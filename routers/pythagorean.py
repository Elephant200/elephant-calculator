from fastapi import APIRouter
from models.pythagorean import *
from services.pythagorean import *

router = APIRouter()

@router.post("/generate", response_model=list)
def generate_pythagorean_triples(data: PythagoreanTriplesRequest, primitive: bool):
    return generate(data.max_hypotenuse, printIt=False) if primitive else generatePrimitive(data.max_hypotenuse, printIt=False)

