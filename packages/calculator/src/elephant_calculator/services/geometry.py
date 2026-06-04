import math

#====================AREA FORMULAS================================
def area_circle(radius):
    return math.pi * radius * radius

def area_semi_circle(radius):
    return 0.5 * math.pi * radius * radius

def area_ellipse(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

def area_rectangle(length, width):
    return length * width

def area_square(side):
    return side * side

def area_parallelogram(side1, side2, theta):
    return side1 * side2 * math.sin(math.radians(theta))

def area_rhombus(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def area_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def area_polygon(sides, side_length):
    if sides < 3:
        return "A polygon must have at least 3 sides."
    apothem = side_length / (2 * math.tan(math.pi / sides))
    return 0.5 * sides * side_length * apothem

def area_triangle_heron(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

def area_triangle_sas(side1, side2, angle):
    return 0.5 * side1 * side2 * math.sin(math.radians(angle))

def area_triangle_base_height(base, height):
    return 0.5 * base * height

def area_pentagon(side):
    return 0.25 * math.sqrt(25 + 10 * math.sqrt(5)) * side ** 2

def area_hexagon(side):
    return (3 * math.sqrt(3) / 2) * side ** 2

def area_heptagon(side):
    return 0.25 * 7 * side ** 2 / math.tan(math.pi / 7)

def area_octagon(side):
    return 2 * (1 + math.sqrt(2)) * side ** 2

def area_nonagon(side):
    return 0.25 * 9 * side ** 2 / math.tan(math.pi / 9)

def area_decagon(side):
    return 0.25 * 10 * side ** 2 / math.tan(math.pi / 10)

#====================PERIMETER FORMULAS===========================
def perimeter_circle(radius):
    return 2 * math.pi * radius

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def perimeter_square(side):
    return 4 * side

def perimeter_polygon(sides, side_length):
    return sides * side_length

def perimeter_triangle(side1, side2, side3):
    return side1 + side2 + side3

def perimeter_trapezoid(base1, base2, side1, side2):
    return base1 + base2 + side1 + side2

def perimeter_pentagon(side):
    return 5 * side

def perimeter_hexagon(side):
    return 6 * side

def perimeter_heptagon(side):
    return 7 * side

def perimeter_octagon(side):
    return 8 * side

def perimeter_nonagon(side):
    return 9 * side

def perimeter_decagon(side):
    return 10 * side

#====================VOLUME FORMULAS==============================
def volume_cube(side):
    return side ** 3

def volume_rectangular_prism(length, width, height):
    return length * width * height

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def volume_cone(radius, height):
    return (1 / 3) * math.pi * radius ** 2 * height

def volume_sphere(radius):
    return (4 / 3) * math.pi * radius ** 3

def volume_ellipsoid(axis1, axis2, axis3):
    return (4 / 3) * math.pi * axis1 * axis2 * axis3

def volume_prism(base_area, height):
    return base_area * height

def volume_tetrahedron(side):
    return (side ** 3) / (6 * math.sqrt(2))

def volume_octahedron(side):
    return (math.sqrt(2) / 3) * side ** 3

def volume_dodecahedron(side):
    return ((15 + 7 * math.sqrt(5)) / 4) * side ** 3

def volume_icosahedron(side):
    return (5 * (3 + math.sqrt(5)) / 12) * side ** 3

#====================SURFACE AREA FORMULAS========================
def surface_area_cube(side):
    return 6 * side ** 2

def surface_area_rectangular_prism(length, width, height):
    return 2 * (length * width + length * height + width * height)

def surface_area_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

def surface_area_cone(radius, height):
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)

def surface_area_sphere(radius):
    return 4 * math.pi * radius ** 2

def surface_area_ellipsoid(axis1, axis2, axis3):
    # Approximation formula for ellipsoid surface area
    p = 1.6075
    return 4 * math.pi * ((axis1**p * axis2**p + axis1**p * axis3**p + axis2**p * axis3**p) / 3) ** (1/p)

def surface_area_prism(base_area, base_perimeter, height):
  return 2*base_area + base_perimeter * height

def surface_area_tetrahedron(side):
    return math.sqrt(3) * side ** 2

def surface_area_octahedron(side):
    return 2 * math.sqrt(3) * side ** 2

def surface_area_dodecahedron(side):
    return 3 * math.sqrt(25 + 10 * math.sqrt(5)) * side ** 2

def surface_area_icosahedron(side):
    return 5 * math.sqrt(3) * side ** 2

def surface_area_prism(base_area, base_perimeter, height):
    return 2 * base_area + base_perimeter * height

#====================USER INTERFACE===============================
def area(type):
    type = type.lower()
    if type.startswith('cir'):
        radius = float(input("Radius = "))
        return area_circle(radius)
    elif type.startswith('sem'):
        radius = float(input("Radius = "))
        return area_semi_circle(radius)
    elif type.startswith('ell'):
        semi_major = float(input("Semi-major axis = "))
        semi_minor = float(input("Semi-minor axis = "))
        return area_ellipse(semi_major, semi_minor)
    elif type.startswith('rec'):
        length = float(input("Length = "))
        width = float(input("Width = "))
        return area_rectangle(length, width)
    elif type.startswith('squ'):
        side = float(input("Side = "))
        return area_square(side)
    elif type.startswith('par'):
        side1 = float(input("Side 1 = "))
        side2 = float(input("Side 2 = "))
        theta = float(input("Theta (degrees) = "))
        return area_parallelogram(side1, side2, theta)
    elif type.startswith('rho'):
        diagonal1 = float(input("Diagonal 1 = "))
        diagonal2 = float(input("Diagonal 2 = "))
        return area_rhombus(diagonal1, diagonal2)
    elif type.startswith('tra'):
        base1 = float(input("Base 1 = "))
        base2 = float(input("Base 2 = "))
        height = float(input("Height = "))
        return area_trapezoid(base1, base2, height)
    elif type.startswith('tri'):
        method = input("You may input:\n1. 3 sides\n2. 2 sides and included angle\n3. Base and height\nChoice: ")
        if method == '1':
            side1 = float(input("Side 1 = "))
            side2 = float(input("Side 2 = "))
            side3 = float(input("Side 3 = "))
            return area_triangle_heron(side1, side2, side3)
        elif method == '2':
            side1 = float(input("Side 1 = "))
            side2 = float(input("Side 2 = "))
            angle = float(input("Included angle (degrees) = "))
            return area_triangle_sas(side1, side2, angle)
        elif method == '3':
            base = float(input("Base = "))
            height = float(input("Height = "))
            return area_triangle_base_height(base, height)
        else:
            return "Invalid input for triangle area calculation."
    elif type.startswith('pol'):
        sides = float(input("# of sides = "))
        side = float(input("Side = "))
        return area_polygon(sides, side)
    elif type.startswith('pen'):
        side = float(input("Side = "))
        return area_pentagon(side)
    elif type.startswith('hex'):
        side = float(input("Side = "))
        return area_hexagon(side)
    elif type.startswith('hep'):
        side = float(input("Side = "))
        return area_heptagon(side)
    elif type.startswith('oct'):
        side = float(input("Side = "))
        return area_octagon(side)
    elif type.startswith('non'):
        side = float(input("Side = "))
        return area_nonagon(side)
    elif type.startswith('dec'):
        side = float(input("Side = "))
        return area_decagon(side)
    else:
        return "Unsupported shape type"

def perimeter(type):
    type = type.lower()
    if type.startswith('cir'):
        radius = float(input("Radius = "))
        return perimeter_circle(radius)
    elif type.startswith('rec'):
        length = float(input("Length = "))
        width = float(input("Width = "))
        return perimeter_rectangle(length, width)
    elif type.startswith('squ'):
        side = float(input("Side = "))
        return perimeter_square(side)
    elif type.startswith('tri'):
        side1 = float(input("Side 1 = "))
        side2 = float(input("Side 2 = "))
        side3 = float(input("Side 3 = "))
        return perimeter_triangle(side1, side2, side3)
    elif type.startswith('tra'):
        base1 = float(input("Base 1 = "))
        base2 = float(input("Base 2 = "))
        side1 = float(input("Side 1 = "))
        side2 = float(input("Side 2 = "))
        return perimeter_trapezoid(base1, base2, side1, side2)
    elif type.startswith('pol'):
        sides = float(input("# of sides = "))
        side = float(input("Side = "))
        return perimeter_polygon(sides, side)
    elif type.startswith('pen'):
        side = float(input("Side = "))
        return perimeter_pentagon(side)
    elif type.startswith('hex'):
        side = float(input("Side = "))
        return perimeter_hexagon(side)
    elif type.startswith('hep'):
        side = float(input("Side = "))
        return perimeter_heptagon(side)
    elif type.startswith('oct'):
        side = float(input("Side = "))
        return perimeter_octagon(side)
    elif type.startswith('non'):
        side = float(input("Side = "))
        return perimeter_nonagon(side)
    elif type.startswith('dec'):
        side = float(input("Side = "))
        return perimeter_decagon(side)
    else:
        return "Unsupported shape type."

def volume(type):
    type = type.lower()
    if type.startswith('cub'):
        side = float(input("Side = "))
        return volume_cube(side)
    elif type.startswith('rec'):
        length = float(input("Length = "))
        width = float(input("Width = "))
        height = float(input("Height = "))
        return volume_rectangular_prism(length, width, height)
    elif type.startswith('cyl'):
        radius = float(input("Radius = "))
        height = float(input("Height = "))
        return volume_cylinder(radius, height)
    elif type.startswith('con'):
        radius = float(input("Radius = "))
        height = float(input("Height = "))
        return volume_cone(radius, height)
    elif type.startswith('sph'):
        radius = float(input("Radius = "))
        return volume_sphere(radius)
    elif type.startswith('ell'):
        axis1 = float(input("Axis 1 = "))
        axis2 = float(input("Axis 2 = "))
        axis3 = float(input("Axis 3 = "))
        return volume_ellipsoid(axis1, axis2, axis3)
    elif type.startswith('pri'):
        shape_type = input("Enter the base shape type: ")
        base_area = area(shape_type)
        height = float(input("Height = "))
        return volume_prism(base_area, height)
    elif type.startswith('tet'):
        side = float(input("Side = "))
        return volume_tetrahedron(side)
    elif type.startswith('oct'):
        side = float(input("Side = "))
        return volume_octahedron(side)
    elif type.startswith('dod'):
        side = float(input("Side = "))
        return volume_dodecahedron(side)
    elif type.startswith('ico'):
        side = float(input("Side = "))
        return volume_icosahedron(side)
    else:
        return "Unsupported shape type."

def surface_area(type):
    type = type.lower()
    if type.startswith('cub'):
        side = float(input("Side = "))
        return surface_area_cube(side)
    elif type.startswith('rec'):
        length = float(input("Length = "))
        width = float(input("Width = "))
        height = float(input("Height = "))
        return surface_area_rectangular_prism(length, width, height)
    elif type.startswith('cyl'):
        radius = float(input("Radius = "))
        height = float(input("Height = "))
        return surface_area_cylinder(radius, height)
    elif type.startswith('con'):
        radius = float(input("Radius = "))
        height = float(input("Height = "))
        return surface_area_cone(radius, height)
    elif type.startswith('sph'):
        radius = float(input("Radius = "))
        return surface_area_sphere(radius)
    elif type.startswith('ell'):
        axis1 = float(input("Axis 1 = "))
        axis2 = float(input("Axis 2 = "))
        axis3 = float(input("Axis 3 = "))
        return surface_area_ellipsoid(axis1, axis2, axis3)
    elif type.startswith('pri'):
        shape_type = input("Enter the base shape type: ")
        base_area = area(shape_type)
        base_perimeter = perimeter(shape_type)
        height = float(input("Height = "))
        return surface_area_prism(base_area, base_perimeter, height)
    elif type.startswith('tet'):
        side = float(input("Side = "))
        return surface_area_tetrahedron(side)
    elif type.startswith('oct'):
        side = float(input("Side = "))
        return surface_area_octahedron(side)
    elif type.startswith('dod'):
        side = float(input("Side = "))
        return surface_area_dodecahedron(side)
    elif type.startswith('ico'):
        side = float(input("Side = "))
        return surface_area_icosahedron(side)
    else:
        return "Unsupported shape type."
