from fastapi import APIRouter, Query
from models.pythagorean import *
from services.pythagorean import *

router = APIRouter()

@router.post("/generate", response_model=list)
def generate_pythagorean_triples(data: PythagoreanTriplesRequest, primitive: bool = Query(False, description="Set to True for primitive triples")):
    if primitive:
        return generatePrimitive(data.max_hypotenuse, printIt=False)
    return generate(data.max_hypotenuse, printIt=False)
