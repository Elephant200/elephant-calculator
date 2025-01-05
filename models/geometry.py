from pydantic import BaseModel

class Circle(BaseModel):
    radius: float

class SemiCircle(BaseModel):
    radius: float

class Ellipse(BaseModel):
    semi_major: float
    semi_minor: float

class Rectangle(BaseModel):
    length: float
    width: float

class Square(BaseModel):
    side: float

class Parallelogram(BaseModel):
    side1: float
    side2: float
    theta: float

class Rhombus(BaseModel):
    diagonal1: float
    diagonal2: float

class Trapezoid(BaseModel):
    base1: float
    base2: float
    height: float

class Polygon(BaseModel):
    sides: int
    side_length: float

class TriangleHeron(BaseModel):
    side1: float
    side2: float
    side3: float

class TriangleSAS(BaseModel):
    side1: float
    side2: float
    angle: float

class TriangleBaseHeight(BaseModel):
    base: float
    height: float

class Cube(BaseModel):
    side: float

class RectangularPrism(BaseModel):
    length: float
    width: float
    height: float

class Prism(BaseModel):
    base_area: float
    base_perimeter: float = None
    height: float