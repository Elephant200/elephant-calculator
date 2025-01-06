from pydantic import BaseModel, Field, field_validator
import math

class Circle(BaseModel):
    radius: float = Field(..., description="The radius of the circle.")

    @field_validator("radius")
    def validate_radius(cls, v):
        if v <= 0:
            raise ValueError("Radius must be greater than zero.")
        return v


class SemiCircle(BaseModel):
    radius: float = Field(..., description="The radius of the semicircle.")

    @field_validator("radius")
    def validate_radius(cls, v):
        if v <= 0:
            raise ValueError("Radius must be greater than zero.")
        return v


class Ellipse(BaseModel):
    semi_major: float = Field(..., description="The semi-major axis of the ellipse.")
    semi_minor: float = Field(..., description="The semi-minor axis of the ellipse.")

    @field_validator("semi_major", "semi_minor")
    def validate_axes(cls, v):
        if v <= 0:
            raise ValueError("Axes must be greater than zero.")
        return v

    @field_validator("semi_minor")
    def validate_minor_less_than_major(cls, v, values):
        semi_major = values.get("semi_major")
        if semi_major and v > semi_major:
            raise ValueError("Semi-minor axis must be less than or equal to semi-major axis.")
        return v


class Rectangle(BaseModel):
    length: float = Field(..., description="The length of the rectangle.")
    width: float = Field(..., description="The width of the rectangle.")

    @field_validator("length", "width")
    def validate_dimensions(cls, v):
        if v <= 0:
            raise ValueError("Length and width must be greater than zero.")
        return v


class Square(BaseModel):
    side: float = Field(..., description="The side length of the square.")

    @field_validator("side")
    def validate_side(cls, v):
        if v <= 0:
            raise ValueError("Side length must be greater than zero.")
        return v


class Parallelogram(BaseModel):
    side1: float = Field(..., description="The length of the first side.")
    side2: float = Field(..., description="The length of the second side.")
    theta: float = Field(..., description="The angle (in degrees) between the two sides.")

    @field_validator("side1", "side2")
    def validate_sides(cls, v):
        if v <= 0:
            raise ValueError("Sides must be greater than zero.")
        return v

    @field_validator("theta")
    def validate_theta(cls, v):
        if v <= 0 or v >= 180:
            raise ValueError("Theta must be in the range (0, 180) degrees.")
        return v


class Rhombus(BaseModel):
    diagonal1: float = Field(..., description="The length of the first diagonal.")
    diagonal2: float = Field(..., description="The length of the second diagonal.")

    @field_validator("diagonal1", "diagonal2")
    def validate_diagonals(cls, v):
        if v <= 0:
            raise ValueError("Diagonals must be greater than zero.")
        return v


class Trapezoid(BaseModel):
    base1: float = Field(..., description="The length of the first base.")
    base2: float = Field(..., description="The length of the second base.")
    height: float = Field(..., description="The height of the trapezoid.")

    @field_validator("base1", "base2", "height")
    def validate_dimensions(cls, v):
        if v <= 0:
            raise ValueError("Base lengths and height must be greater than zero.")
        return v


class Polygon(BaseModel):
    sides: int = Field(..., description="The number of sides of the polygon.")
    side_length: float = Field(..., description="The length of each side.")

    @field_validator("sides")
    def validate_sides(cls, v):
        if v < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        return v

    @field_validator("side_length")
    def validate_side_length(cls, v):
        if v <= 0:
            raise ValueError("Side length must be greater than zero.")
        return v


class TriangleHeron(BaseModel):
    side1: float = Field(..., description="The length of the first side.")
    side2: float = Field(..., description="The length of the second side.")
    side3: float = Field(..., description="The length of the third side.")

    @field_validator("side1", "side2", "side3")
    def validate_sides(cls, v):
        if v <= 0:
            raise ValueError("Sides must be greater than zero.")
        return v

    @field_validator("side3")
    def validate_triangle_inequality(cls, v, values):
        a, b = values.get("side1"), values.get("side2")
        if a and b and (a + b <= v or a + v <= b or b + v <= a):
            raise ValueError("Sides do not satisfy the triangle inequality.")
        return v


class TriangleSAS(BaseModel):
    side1: float = Field(..., description="The length of the first side.")
    side2: float = Field(..., description="The length of the second side.")
    angle: float = Field(..., description="The included angle (in degrees).")

    @field_validator("side1", "side2")
    def validate_sides(cls, v):
        if v <= 0:
            raise ValueError("Sides must be greater than zero.")
        return v

    @field_validator("angle")
    def validate_angle(cls, v):
        if v <= 0 or v >= 180:
            raise ValueError("Angle must be in the range (0, 180) degrees.")
        return v


class TriangleBaseHeight(BaseModel):
    base: float = Field(..., description="The base length of the triangle.")
    height: float = Field(..., description="The height of the triangle.")

    @field_validator("base", "height")
    def validate_base_and_height(cls, v):
        if v <= 0:
            raise ValueError("Base and height must be greater than zero.")
        return v


class Cube(BaseModel):
    side: float = Field(..., description="The side length of the cube.")

    @field_validator("side")
    def validate_side(cls, v):
        if v <= 0:
            raise ValueError("Side length must be greater than zero.")
        return v


class RectangularPrism(BaseModel):
    length: float = Field(..., description="The length of the rectangular prism.")
    width: float = Field(..., description="The width of the rectangular prism.")
    height: float = Field(..., description="The height of the rectangular prism.")

    @field_validator("length", "width", "height")
    def validate_dimensions(cls, v):
        if v <= 0:
            raise ValueError("Length, width, and height must be greater than zero.")
        return v


class Prism(BaseModel):
    base_area: float = Field(..., description="The base area of the prism.")
    base_perimeter: float = Field(None, description="The base perimeter of the prism (optional).")
    height: float = Field(..., description="The height of the prism.")

    @field_validator("base_area", "height")
    def validate_base_area_and_height(cls, v):
        if v <= 0:
            raise ValueError("Base area and height must be greater than zero.")
        return v

    @field_validator("base_perimeter", mode="before")
    def validate_base_perimeter(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Base perimeter must be greater than zero if provided.")
        return v
