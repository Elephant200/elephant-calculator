from pydantic import BaseModel

class VectorOperation(BaseModel):
    vector1: list[float]
    vector2: list[float]

class ScalarVectorOperation(BaseModel):
    vector: list[float]
    scalar: float