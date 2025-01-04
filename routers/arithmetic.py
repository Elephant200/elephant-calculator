from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ArithmeticRequest(BaseModel):
    operand1: float
    operand2: float

@router.post("/add")
def add(request: ArithmeticRequest):
    return {"result": request.operand1 + request.operand2}

@router.post("/subtract")
def subtract(request: ArithmeticRequest):
    return {"result": request.operand1 - request.operand2}

@router.post("/multiply")
def multiply(request: ArithmeticRequest):
    return {"result": request.operand1 * request.operand2}

@router.post("/divide")
def divide(request: ArithmeticRequest):
    if request.operand2 == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": request.operand1 / request.operand2}