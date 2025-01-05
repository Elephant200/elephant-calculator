from pydantic import BaseModel

class TriangleRequest(BaseModel):
    a: float = None
    b: float = None
    c: float = None
    A: float = None
    B: float = None
    C: float = None