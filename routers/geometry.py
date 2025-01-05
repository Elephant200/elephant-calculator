from fastapi import APIRouter
from models.geometry import *
from services.geometry import *

router = APIRouter()

@router.post("/area/circle", response_model=float)
def calculate_area_circle(data: Circle):
    return area_circle(data.radius)

@router.post("/area/semi_circle", response_model=float)
def calculate_area_semi_circle(data: SemiCircle):
    return area_semi_circle(data.radius)

@router.post("/area/ellipse", response_model=float)
def calculate_area_ellipse(data: Ellipse):
    return area_ellipse(data.semi_major, data.semi_minor)

@router.post("/area/rectangle", response_model=float)
def calculate_area_rectangle(data: Rectangle):
    return area_rectangle(data.length, data.width)

@router.post("/area/square", response_model=float)
def calculate_area_square(data: Square):
    return area_square(data.side)

@router.post("/area/parallelogram", response_model=float)
def calculate_area_parallelogram(data: Parallelogram):
    return area_parallelogram(data.side1, data.side2, data.theta)

@router.post("/area/rhombus", response_model=float)
def calculate_area_rhombus(data: Rhombus):
    return area_rhombus(data.diagonal1, data.diagonal2)

@router.post("/area/trapezoid", response_model=float)
def calculate_area_trapezoid(data: Trapezoid):
    return area_trapezoid(data.base1, data.base2, data.height)

@router.post("/area/polygon", response_model=float)
def calculate_area_polygon(data: Polygon):
    return area_polygon(data.sides, data.side_length)

@router.post("/area/triangle/heron", response_model=float)
def calculate_area_triangle_heron(data: TriangleHeron):
    return area_triangle_heron(data.side1, data.side2, data.side3)

@router.post("/area/triangle/sas", response_model=float)
def calculate_area_triangle_sas(data: TriangleSAS):
    return area_triangle_sas(data.side1, data.side2, data.angle)

@router.post("/area/triangle/base_height", response_model=float)
def calculate_area_triangle_base_height(data: TriangleBaseHeight):
    return area_triangle_base_height(data.base, data.height)

@router.post("/area/pentagon", response_model=float)
def calculate_area_pentagon(data: Square):
    return area_pentagon(data.side)

@router.post("/area/hexagon", response_model=float)
def calculate_area_hexagon(data: Square):
    return area_hexagon(data.side)

@router.post("/area/heptagon", response_model=float)
def calculate_area_heptagon(data: Square):
    return area_heptagon(data.side)

@router.post("/area/octagon", response_model=float)
def calculate_area_octagon(data: Square):
    return area_octagon(data.side)

@router.post("/area/nonagon", response_model=float)
def calculate_area_nonagon(data: Square):
    return area_nonagon(data.side)

@router.post("/area/decagon", response_model=float)
def calculate_area_decagon(data: Square):
    return area_decagon(data.side)

@router.post("/perimeter/circle", response_model=float)
def calculate_perimeter_circle(data: Circle):
    return perimeter_circle(data.radius)

@router.post("/perimeter/rectangle", response_model=float)
def calculate_perimeter_rectangle(data: Rectangle):
    return perimeter_rectangle(data.length, data.width)

@router.post("/perimeter/square", response_model=float)
def calculate_perimeter_square(data: Square):
    return perimeter_square(data.side)

@router.post("/perimeter/polygon", response_model=float)
def calculate_perimeter_polygon(data: Polygon):
    return perimeter_polygon(data.sides, data.side_length)

@router.post("/perimeter/triangle", response_model=float)
def calculate_perimeter_triangle(data: TriangleHeron):
    return perimeter_triangle(data.side1, data.side2, data.side3)

@router.post("/perimeter/trapezoid", response_model=float)
def calculate_perimeter_trapezoid(data: Trapezoid):
    return perimeter_trapezoid(data.base1, data.base2, data.height, data.height)

@router.post("/perimeter/pentagon", response_model=float)
def calculate_perimeter_pentagon(data: Square):
    return perimeter_pentagon(data.side)

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

@router.post("/volume/cube", response_model=float)
def calculate_volume_cube(data: Cube):
    return volume_cube(data.side)

@router.post("/volume/rectangular_prism", response_model=float)
def calculate_volume_rectangular_prism(data: RectangularPrism):
    return volume_rectangular_prism(data.length, data.width, data.height)

@router.post("/volume/cylinder", response_model=float)
def calculate_volume_cylinder(data: Prism):
    return volume_cylinder(data.base_area, data.height)

@router.post("/volume/cone", response_model=float)
def calculate_volume_cone(data: Prism):
    return volume_cone(data.base_area, data.height)

@router.post("/volume/sphere", response_model=float)
def calculate_volume_sphere(data: Circle):
    return volume_sphere(data.radius)

@router.post("/volume/ellipsoid", response_model=float)
def calculate_volume_ellipsoid(data: Ellipse):
    return volume_ellipsoid(data.semi_major, data.semi_minor, data.semi_major)

@router.post("/volume/prism", response_model=float)
def calculate_volume_prism(data: Prism):
    return volume_prism(data.base_area, data.height)

@router.post("/volume/tetrahedron", response_model=float)
def calculate_volume_tetrahedron(data: Cube):
    return volume_tetrahedron(data.side)

@router.post("/volume/octahedron", response_model=float)
def calculate_volume_octahedron(data: Cube):
    return volume_octahedron(data.side)

@router.post("/volume/dodecahedron", response_model=float)
def calculate_volume_dodecahedron(data: Cube):
    return volume_dodecahedron(data.side)

@router.post("/volume/icosahedron", response_model=float)
def calculate_volume_icosahedron(data: Cube):
    return volume_icosahedron(data.side)

@router.post("/surface_area/cube", response_model=float)
def calculate_surface_area_cube(data: Cube):
    return surface_area_cube(data.side)

@router.post("/surface_area/rectangular_prism", response_model=float)
def calculate_surface_area_rectangular_prism(data: RectangularPrism):
    return surface_area_rectangular_prism(data.length, data.width, data.height)

@router.post("/surface_area/cylinder", response_model=float)
def calculate_surface_area_cylinder(data: Prism):
    return surface_area_cylinder(data.base_area, data.height)

@router.post("/surface_area/cone", response_model=float)
def calculate_surface_area_cone(data: Prism):
    return surface_area_cone(data.base_area, data.height)

@router.post("/surface_area/sphere", response_model=float)
def calculate_surface_area_sphere(data: Circle):
    return surface_area_sphere(data.radius)

@router.post("/surface_area/ellipsoid", response_model=float)
def calculate_surface_area_ellipsoid(data: Ellipse):
    return surface_area_ellipsoid(data.semi_major, data.semi_minor, data.semi_major)

@router.post("/surface_area/prism", response_model=float)
def calculate_surface_area_prism(data: Prism):
    return surface_area_prism(data.base_area, data.base_perimeter, data.height)

@router.post("/surface_area/tetrahedron", response_model=float)
def calculate_surface_area_tetrahedron(data: Cube):
    return surface_area_tetrahedron(data.side)

@router.post("/surface_area/octahedron", response_model=float)
def calculate_surface_area_octahedron(data: Cube):
    return surface_area_octahedron(data.side)

@router.post("/surface_area/dodecahedron", response_model=float)
def calculate_surface_area_dodecahedron(data: Cube):
    return surface_area_dodecahedron(data.side)

@router.post("/surface_area/icosahedron", response_model=float)
def calculate_surface_area_icosahedron(data: Cube):
    return surface_area_icosahedron(data.side)
