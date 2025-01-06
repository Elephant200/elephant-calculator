from pydantic import BaseModel, validator
import math

class Circle(BaseModel):
    radius: float

    @validator("radius")
    def validate_radius(cls, v):
        if v <= 0:
            raise ValueError("Radius must be greater than zero.")
        return v


class SemiCircle(BaseModel):
    radius: float

    @validator("radius")
    def validate_radius(cls, v):
        if v <= 0:
            raise ValueError("Radius must be greater than zero.")
        return v


class Ellipse(BaseModel):
    semi_major: float
    semi_minor: float

    @validator("semi_major", "semi_minor")
    def validate_axes(cls, v):
        if v <= 0:
            raise ValueError("Axes must be greater than zero.")
        return v

    @validator("semi_minor")
    def minor_less_than_major(cls, v, values):
        if "semi_major" in values and v > values["semi_major"]:
            raise ValueError("Semi-minor axis must be less than or equal to semi-major axis.")
        return v


class Rectangle(BaseModel):
    length: float
    width: float

    @validator("length", "width")
    def validate_dimensions(cls, v):
        if v <= 0:
            raise ValueError("Length and width must be greater than zero.")
        return v


class Square(BaseModel):
    side: float

    @validator("side")
    def validate_side(cls, v):
        if v <= 0:
            raise ValueError("Side length must be greater than zero.")
        return v


class Parallelogram(BaseModel):
    side1: float
    side2: float
    theta: float

    @validator("side1", "side2")
    def validate_sides(cls, v):
        if v <= 0:
            raise ValueError("Sides must be greater than zero.")
        return v

    @validator("theta")
    def validate_theta(cls, v):
        if v <= 0 or v >= 180:
            raise ValueError("Theta must be in the range (0, 180) degrees.")
        return v


class Rhombus(BaseModel):
    diagonal1: float
    diagonal2: float

    @validator("diagonal1", "diagonal2")
    def validate_diagonals(cls, v):
        if v <= 0:
            raise ValueError("Diagonals must be greater than zero.")
        return v


class Trapezoid(BaseModel):
    base1: float
    base2: float
    height: float

    @validator("base1", "base2", "height")
    def validate_trapezoid_dimensions(cls, v):
        if v <= 0:
            raise ValueError("Base lengths and height must be greater than zero.")
        return v


class Polygon(BaseModel):
    sides: int
    side_length: float

    @validator("sides")
    def validate_sides(cls, v):
        if v < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        return v

    @validator("side_length")
    def validate_side_length(cls, v):
        if v <= 0:
            raise ValueError("Side length must be greater than zero.")
        return v


class TriangleHeron(BaseModel):
    side1: float
    side2: float
    side3: float

    @validator("side1", "side2", "side3")
    def validate_sides(cls, v):
        if v <= 0:
            raise ValueError("Sides must be greater than zero.")
        return v

    @validator("side3")
    def validate_triangle_inequality(cls, v, values):
        a, b = values.get("side1"), values.get("side2")
        if a and b and (a + b <= v or a + v <= b or b + v <= a):
            raise ValueError("Sides do not satisfy the triangle inequality.")
        return v


class TriangleSAS(BaseModel):
    side1: float
    side2: float
    angle: float

    @validator("side1", "side2")
    def validate_sides(cls, v):
        if v <= 0:
            raise ValueError("Sides must be greater than zero.")
        return v

    @validator("angle")
    def validate_angle(cls, v):
        if v <= 0 or v >= 180:
            raise ValueError("Angle must be in the range (0, 180) degrees.")
        return v


class TriangleBaseHeight(BaseModel):
    base: float
    height: float

    @validator("base", "height")
    def validate_base_and_height(cls, v):
        if v <= 0:
            raise ValueError("Base and height must be greater than zero.")
        return v


class Cube(BaseModel):
    side: float

    @validator("side")
    def validate_side(cls, v):
        if v <= 0:
            raise ValueError("Side length must be greater than zero.")
        return v


class RectangularPrism(BaseModel):
    length: float
    width: float
    height: float

    @validator("length", "width", "height")
    def validate_dimensions(cls, v):
        if v <= 0:
            raise ValueError("Length, width, and height must be greater than zero.")
        return v


class Prism(BaseModel):
    base_area: float
    base_perimeter: float = None
    height: float

    @validator("base_area", "height")
    def validate_area_and_height(cls, v):
        if v <= 0:
            raise ValueError("Base area and height must be greater than zero.")
        return v

    @validator("base_perimeter", always=True)
    def validate_perimeter(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Base perimeter must be greater than zero if provided.")
        return v
