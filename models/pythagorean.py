from pydantic import BaseModel

class PythagoreanTriplesRequest(BaseModel):
    max_hypotenuse: int