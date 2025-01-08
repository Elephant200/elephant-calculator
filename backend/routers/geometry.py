from fastapi import APIRouter
from models.geometry import *
from services.geometry import *

router = APIRouter()

# AREA CALCULATIONS
@router.post("/area/circle", response_model=float)
def calculate_area_circle(data: Circle):
    """
    Calculate the area of a circle.

    Args:
        data (Circle): Contains the radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return area_circle(data.radius)

@router.post("/area/semi_circle", response_model=float)
def calculate_area_semi_circle(data: SemiCircle):
    """
    Calculate the area of a semicircle.

    Args:
        data (SemiCircle): Contains the radius of the semicircle.

    Returns:
        float: The area of the semicircle.
    """
    return area_semi_circle(data.radius)

@router.post("/area/ellipse", response_model=float)
def calculate_area_ellipse(data: Ellipse):
    """
    Calculate the area of an ellipse.

    Args:
        data (Ellipse): Contains the semi-major and semi-minor axes of the ellipse.

    Returns:
        float: The area of the ellipse.
    """
    return area_ellipse(data.semi_major, data.semi_minor)

@router.post("/area/rectangle", response_model=float)
def calculate_area_rectangle(data: Rectangle):
    """
    Calculate the area of a rectangle.

    Args:
        data (Rectangle): Contains the length and width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return area_rectangle(data.length, data.width)

@router.post("/area/square", response_model=float)
def calculate_area_square(data: Square):
    """
    Calculate the area of a square.

    Args:
        data (Square): Contains the side length of the square.

    Returns:
        float: The area of the square.
    """
    return area_square(data.side)

@router.post("/area/parallelogram", response_model=float)
def calculate_area_parallelogram(data: Parallelogram):
    """
    Calculate the area of a parallelogram.

    Args:
        data (Parallelogram): Contains the two side lengths and the angle between them (in degrees).

    Returns:
        float: The area of the parallelogram.
    """
    return area_parallelogram(data.side1, data.side2, data.theta)

@router.post("/area/rhombus", response_model=float)
def calculate_area_rhombus(data: Rhombus):
    """
    Calculate the area of a rhombus.

    Args:
        data (Rhombus): Contains the lengths of the diagonals of the rhombus.

    Returns:
        float: The area of the rhombus.
    """
    return area_rhombus(data.diagonal1, data.diagonal2)

@router.post("/area/trapezoid", response_model=float)
def calculate_area_trapezoid(data: Trapezoid):
    """
    Calculate the area of a trapezoid.

    Args:
        data (Trapezoid): Contains the lengths of the two bases and the height of the trapezoid.

    Returns:
        float: The area of the trapezoid.
    """
    return area_trapezoid(data.base1, data.base2, data.height)

@router.post("/area/polygon", response_model=float)
def calculate_area_polygon(data: Polygon):
    """
    Calculate the area of a regular polygon.

    Args:
        data (Polygon): Contains the number of sides and the length of each side.

    Returns:
        float: The area of the polygon.
    """
    return area_polygon(data.sides, data.side_length)

@router.post("/area/triangle/heron", response_model=float)
def calculate_area_triangle_heron(data: TriangleHeron):
    """
    Calculate the area of a triangle using Heron's formula.

    Args:
        data (TriangleHeron): Contains the lengths of the three sides of the triangle.

    Returns:
        float: The area of the triangle.
    """
    return area_triangle_heron(data.side1, data.side2, data.side3)

@router.post("/area/triangle/sas", response_model=float)
def calculate_area_triangle_sas(data: TriangleSAS):
    """
    Calculate the area of a triangle using the SAS method.

    Args:
        data (TriangleSAS): Contains two side lengths and the angle between them (in degrees).

    Returns:
        float: The area of the triangle.
    """
    return area_triangle_sas(data.side1, data.side2, data.angle)

@router.post("/area/triangle/base_height", response_model=float)
def calculate_area_triangle_base_height(data: TriangleBaseHeight):
    """
    Calculate the area of a triangle using its base and height.

    Args:
        data (TriangleBaseHeight): Contains the base length and height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    return area_triangle_base_height(data.base, data.height)

# PERIMETER CALCULATIONS
@router.post("/perimeter/circle", response_model=float)
def calculate_perimeter_circle(data: Circle):
    """
    Calculate the perimeter of a circle (circumference).

    Args:
        data (Circle): Contains the radius of the circle.

    Returns:
        float: The perimeter of the circle.
    """
    return perimeter_circle(data.radius)

@router.post("/perimeter/rectangle", response_model=float)
def calculate_perimeter_rectangle(data: Rectangle):
    """
    Calculate the perimeter of a rectangle.

    Args:
        data (Rectangle): Contains the length and width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    return perimeter_rectangle(data.length, data.width)

@router.post("/perimeter/square", response_model=float)
def calculate_perimeter_square(data: Square):
    """
    Calculate the perimeter of a square.

    Args:
        data (Square): Contains the side length of the square.

    Returns:
        float: The perimeter of the square.
    """
    return perimeter_square(data.side)

@router.post("/perimeter/polygon", response_model=float)
def calculate_perimeter_polygon(data: Polygon):
    """
    Calculate the perimeter of a regular polygon.

    Args:
        data (Polygon): Contains the number of sides and the length of each side.

    Returns:
        float: The perimeter of the polygon.
    """
    return perimeter_polygon(data.sides, data.side_length)

@router.post("/perimeter/triangle", response_model=float)
def calculate_perimeter_triangle(data: TriangleHeron):
    """
    Calculate the perimeter of a triangle.

    Args:
        data (TriangleHeron): Contains the lengths of the three sides of the triangle.

    Returns:
        float: The perimeter of the triangle.
    """
    return perimeter_triangle(data.side1, data.side2, data.side3)

@router.post("/perimeter/trapezoid", response_model=float)
def calculate_perimeter_trapezoid(data: Trapezoid):
    """
    Calculate the perimeter of a trapezoid.

    Args:
        data (Trapezoid): Contains the lengths of the two bases and the two non-parallel sides.

    Returns:
        float: The perimeter of the trapezoid.
    """
    return perimeter_trapezoid(data.base1, data.base2, data.height, data.height)

@router.post("/perimeter/pentagon", response_model=float)
def calculate_perimeter_pentagon(data: Square):
    """
    Calculate the perimeter of a regular pentagon.

    Args:
        data (Square): Contains the side length of the pentagon.

    Returns:
        float: The perimeter of the pentagon.
    """
    return perimeter_pentagon(data.side)

@router.post("/perimeter/hexagon", response_model=float)
def calculate_perimeter_hexagon(data: Square):
    """
    Calculate the perimeter of a regular hexagon.

    Args:
        data (Square): Contains the side length of the hexagon.

    Returns:
        float: The perimeter of the hexagon.
    """
    return perimeter_hexagon(data.side)

@router.post("/perimeter/heptagon", response_model=float)
def calculate_perimeter_heptagon(data: Square):
    """
    Calculate the perimeter of a regular heptagon.

    Args:
        data (Square): Contains the side length of the heptagon.

    Returns:
        float: The perimeter of the heptagon.
    """
    return perimeter_heptagon(data.side)

@router.post("/perimeter/octagon", response_model=float)
def calculate_perimeter_octagon(data: Square):
    """
    Calculate the perimeter of a regular octagon.

    Args:
        data (Square): Contains the side length of the octagon.

    Returns:
        float: The perimeter of the octagon.
    """
    return perimeter_octagon(data.side)

@router.post("/perimeter/nonagon", response_model=float)
def calculate_perimeter_nonagon(data: Square):
    """
    Calculate the perimeter of a regular nonagon.

    Args:
        data (Square): Contains the side length of the nonagon.

    Returns:
        float: The perimeter of the nonagon.
    """
    return perimeter_nonagon(data.side)

@router.post("/perimeter/decagon", response_model=float)
def calculate_perimeter_decagon(data: Square):
    """
    Calculate the perimeter of a regular decagon.

    Args:
        data (Square): Contains the side length of the decagon.

    Returns:
        float: The perimeter of the decagon.
    """
    return perimeter_decagon(data.side)


@router.post("/perimeter/hexagon", response_model=float)
def calculate_perimeter_hexagon(data: Square):
    return perimeter_hexagon(data.side)

@router.post("/perimeter/heptagon", response_model=float)
def calculate_perimeter_heptagon(data: Square):
    return perimeter_heptagon(data.side)

@router.post("/perimeter/octagon", response_model=float)
def calculate_perimeter_octagon(data: Square):
    return perimeter_octagon(data.side)

@router.post("/perimeter/nonagon", response_model=float)
def calculate_perimeter_nonagon(data: Square):
    return perimeter_nonagon(data.side)

@router.post("/perimeter/decagon", response_model=float)
def calculate_perimeter_decagon(data: Square):
    return perimeter_decagon(data.side)

# VOLUME CALCULATIONS
@router.post("/volume/cube", response_model=float)
def calculate_volume_cube(data: Cube):
    """
    Calculate the volume of a cube.

    Args:
        data (Cube): Contains the side length of the cube.

    Returns:
        float: The volume of the cube.
    """
    return volume_cube(data.side)

@router.post("/volume/rectangular_prism", response_model=float)
def calculate_volume_rectangular_prism(data: RectangularPrism):
    """
    Calculate the volume of a rectangular prism.

    Args:
        data (RectangularPrism): Contains the length, width, and height of the prism.

    Returns:
        float: The volume of the rectangular prism.
    """
    return volume_rectangular_prism(data.length, data.width, data.height)

@router.post("/volume/cylinder", response_model=float)
def calculate_volume_cylinder(data: Circle):
    """
    Calculate the volume of a cylinder.

    Args:
        data (Circle): Contains the radius of the base and height of the cylinder.

    Returns:
        float: The volume of the cylinder.
    """
    return volume_cylinder(data.radius, data.height)

@router.post("/volume/cone", response_model=float)
def calculate_volume_cone(data: Circle):
    """
    Calculate the volume of a cone.

    Args:
        data (Circle): Contains the radius of the base and height of the cone.

    Returns:
        float: The volume of the cone.
    """
    return volume_cone(data.radius, data.height)

@router.post("/volume/sphere", response_model=float)
def calculate_volume_sphere(data: Circle):
    """
    Calculate the volume of a sphere.

    Args:
        data (Circle): Contains the radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    return volume_sphere(data.radius)

@router.post("/volume/ellipsoid", response_model=float)
def calculate_volume_ellipsoid(data: Ellipse):
    """
    Calculate the volume of an ellipsoid.

    Args:
        data (Ellipse): Contains the three axes (semi-major, semi-minor, and a third axis).

    Returns:
        float: The volume of the ellipsoid.
    """
    return volume_ellipsoid(data.semi_major, data.semi_minor, data.semi_major)

@router.post("/volume/prism", response_model=float)
def calculate_volume_prism(data: Prism):
    """
    Calculate the volume of a prism.

    Args:
        data (Prism): Contains the base area and height of the prism.

    Returns:
        float: The volume of the prism.
    """
    return volume_prism(data.base_area, data.height)

@router.post("/volume/tetrahedron", response_model=float)
def calculate_volume_tetrahedron(data: Cube):
    """
    Calculate the volume of a regular tetrahedron.

    Args:
        data (Cube): Contains the side length of the tetrahedron.

    Returns:
        float: The volume of the tetrahedron.
    """
    return volume_tetrahedron(data.side)

@router.post("/volume/octahedron", response_model=float)
def calculate_volume_octahedron(data: Cube):
    """
    Calculate the volume of a regular octahedron.

    Args:
        data (Cube): Contains the side length of the octahedron.

    Returns:
        float: The volume of the octahedron.
    """
    return volume_octahedron(data.side)

@router.post("/volume/dodecahedron", response_model=float)
def calculate_volume_dodecahedron(data: Cube):
    """
    Calculate the volume of a regular dodecahedron.

    Args:
        data (Cube): Contains the side length of the dodecahedron.

    Returns:
        float: The volume of the dodecahedron.
    """
    return volume_dodecahedron(data.side)

@router.post("/volume/icosahedron", response_model=float)
def calculate_volume_icosahedron(data: Cube):
    """
    Calculate the volume of a regular icosahedron.

    Args:
        data (Cube): Contains the side length of the icosahedron.

    Returns:
        float: The volume of the icosahedron.
    """
    return volume_icosahedron(data.side)


# SURFACE AREA CALCULATIONS
@router.post("/surface_area/cube", response_model=float)
def calculate_surface_area_cube(data: Cube):
    """
    Calculate the surface area of a cube.

    Args:
        data (Cube): Contains the side length of the cube.

    Returns:
        float: The surface area of the cube.
    """
    return surface_area_cube(data.side)

@router.post("/surface_area/rectangular_prism", response_model=float)
def calculate_surface_area_rectangular_prism(data: RectangularPrism):
    """
    Calculate the surface area of a rectangular prism.

    Args:
        data (RectangularPrism): Contains the length, width, and height of the prism.

    Returns:
        float: The surface area of the rectangular prism.
    """
    return surface_area_rectangular_prism(data.length, data.width, data.height)

@router.post("/surface_area/cylinder", response_model=float)
def calculate_surface_area_cylinder(data: Circle):
    """
    Calculate the surface area of a cylinder.

    Args:
        data (Circle): Contains the radius of the base and height of the cylinder.

    Returns:
        float: The surface area of the cylinder.
    """
    return surface_area_cylinder(data.radius, data.height)

@router.post("/surface_area/cone", response_model=float)
def calculate_surface_area_cone(data: Circle):
    """
    Calculate the surface area of a cone.

    Args:
        data (Circle): Contains the radius of the base and height of the cone.

    Returns:
        float: The surface area of the cone.
    """
    return surface_area_cone(data.radius, data.height)

@router.post("/surface_area/sphere", response_model=float)
def calculate_surface_area_sphere(data: Circle):
    """
    Calculate the surface area of a sphere.

    Args:
        data (Circle): Contains the radius of the sphere.

    Returns:
        float: The surface area of the sphere.
    """
    return surface_area_sphere(data.radius)

@router.post("/surface_area/ellipsoid", response_model=float)
def calculate_surface_area_ellipsoid(data: Ellipse):
    """
    Calculate the surface area of an ellipsoid.

    Args:
        data (Ellipse): Contains the three axes (semi-major, semi-minor, and a third axis).

    Returns:
        float: The surface area of the ellipsoid.
    """
    return surface_area_ellipsoid(data.semi_major, data.semi_minor, data.semi_major)

@router.post("/surface_area/prism", response_model=float)
def calculate_surface_area_prism(data: Prism):
    """
    Calculate the surface area of a prism.

    Args:
        data (Prism): Contains the base area, base perimeter, and height of the prism.

    Returns:
        float: The surface area of the prism.
    """
    return surface_area_prism(data.base_area, data.base_perimeter, data.height)

@router.post("/surface_area/tetrahedron", response_model=float)
def calculate_surface_area_tetrahedron(data: Cube):
    """
    Calculate the surface area of a regular tetrahedron.

    Args:
        data (Cube): Contains the side length of the tetrahedron.

    Returns:
        float: The surface area of the tetrahedron.
    """
    return surface_area_tetrahedron(data.side)

@router.post("/surface_area/octahedron", response_model=float)
def calculate_surface_area_octahedron(data: Cube):
    """
    Calculate the surface area of a regular octahedron.

    Args:
        data (Cube): Contains the side length of the octahedron.

    Returns:
        float: The surface area of the octahedron.
    """
    return surface_area_octahedron(data.side)

@router.post("/surface_area/dodecahedron", response_model=float)
def calculate_surface_area_dodecahedron(data: Cube):
    """
    Calculate the surface area of a regular dodecahedron.

    Args:
        data (Cube): Contains the side length of the dodecahedron.

    Returns:
        float: The surface area of the dodecahedron.
    """
    return surface_area_dodecahedron(data.side)

@router.post("/surface_area/icosahedron", response_model=float)
def calculate_surface_area_icosahedron(data: Cube):
    """
    Calculate the surface area of a regular icosahedron.

    Args:
        data (Cube): Contains the side length of the icosahedron.

    Returns:
        float: The surface area of the icosahedron.
    """
    return surface_area_icosahedron(data.side)
