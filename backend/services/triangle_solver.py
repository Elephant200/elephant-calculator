from math import sin, cos, tan, radians, degrees, sqrt, asin, acos, atan
from utils.validators import parse_input

def is_right_angle(angle):
    """
    Check if an angle is approximately 90 degrees.
    """
    return abs(degrees(angle) - 90) < 1e-6

def solve_triangle(a=None, b=None, c=None, A=None, B=None, C=None):
    """
    Solves a triangle given sufficient inputs using the law of sines or law of cosines.

    Parameters:
        a, b, c (float): Sides of the triangle.
        A, B, C (float): Angles of the triangle (in degrees).

    Returns:
        dict: A dictionary containing all sides and angles of the triangle.

    Raises:
        ValueError: If insufficient or inconsistent inputs are provided.
    """
    inputs = [a, b, c, A, B, C]
    num_known = sum(1 for x in inputs if x is not None)
    num_sides = sum(1 for x in [a, b, c] if x is not None)

    if num_known < 3 or num_sides < 1:
        raise ValueError("At least three parameters (including one side) are required to solve the triangle.")
    if A and B and C and not abs(A + B + C - 180) < 1e-6:
        raise ValueError("The sum of angles in a triangle must be 180 degrees.")

    # Convert angles to radians
    if A: A = radians(A)
    if B: B = radians(B)
    if C: C = radians(C)

    # Handle right triangle cases explicitly
    if B and abs(degrees(B) - 90) < 1e-6:
        if a and c:
            b = sqrt(a**2 + c**2)
        elif a and b:
            c = sqrt(b**2 - a**2)
        elif b and c:
            a = sqrt(b**2 - c**2)
        elif A and a:
            c = a / sin(A)
            b = sqrt(c**2 - a**2)
        elif A and c:
            a = c * sin(A)
            b = sqrt(c**2 - a**2)
        elif C and a:
            b = a / cos(C)
            c = sqrt(a**2 + b**2)
        elif C and b:
            a = b * cos(C)
            c = sqrt(a**2 + b**2)
        elif C and c:
            b = sqrt(c**2 - (c * sin(C))**2)
            a = sqrt(c**2 - b**2)
        else:
            raise ValueError("Insufficient data to solve the right triangle.")
        A = asin(a / c) if c else radians(90)
        C = radians(90) - A
    elif A and abs(degrees(A) - 90) < 1e-6:
        # Right triangle where A = 90 degrees
        if a and C:
            B = radians(90) - C
            c = a / cos(C)
            b = c * sin(C)
        elif a and b:
            c = sqrt(a**2 + b**2)
        elif a and c:
            b = sqrt(c**2 - a**2)
        elif b and c:
            a = sqrt(c**2 - b**2)
        elif B and b:
            c = b / sin(B)
            a = sqrt(c**2 - b**2)
        elif B and c:
            b = c * sin(B)
            a = sqrt(c**2 - b**2)
        elif C and b:
            a = b / cos(C)
            c = sqrt(a**2 + b**2)
        elif C and c:
            b = sqrt(c**2 - (c * sin(C))**2)
            a = sqrt(c**2 - b**2)
        else:
            raise ValueError("Insufficient data to solve the right triangle.")
        B = asin(b / c) if c else radians(90)
        C = radians(90) - B
    elif C and abs(degrees(C) - 90) < 1e-6:
        # Similar logic for right triangle with C = 90 degrees
        if a and b:
            c = sqrt(a**2 + b**2)
        elif a and c:
            b = sqrt(c**2 - a**2)
        elif b and c:
            a = sqrt(c**2 - b**2)
        elif A and a:
            c = a / sin(A)
            b = sqrt(c**2 - a**2)
        elif A and c:
            a = c * sin(A)
            b = sqrt(c**2 - a**2)
        elif B and b:
            c = b / sin(B)
            a = sqrt(c**2 - b**2)
        elif B and c:
            b = c * sin(B)
            a = sqrt(c**2 - b**2)
        else:
            raise ValueError("Insufficient data to solve the right triangle.")
        A = asin(a / c) if c else radians(90)
        B = radians(90) - A
    else:
        if A and B:
            C = radians(180) - A - B
        elif A and C:
            B = radians(180) - A - C
        elif B and C:
            A = radians(180) - B - C

        if a and A:
            if B:
                b = a * sin(B) / sin(A)
                c = a * sin(C) / sin(A)
            elif C:
                c = a * sin(C) / sin(A)
                b = a * sin(B) / sin(A)
        elif b and B:
            if A:
                a = b * sin(A) / sin(B)
                c = b * sin(C) / sin(B)
            elif C:
                c = b * sin(C) / sin(B)
                a = b * sin(A) / sin(B)
        elif c and C:
            if A:
                a = c * sin(A) / sin(C)
                b = c * sin(B) / sin(C)
            elif B:
                b = c * sin(B) / sin(C)
                a = c * sin(A) / sin(C)
        elif a and b and C:
            c = sqrt(a**2 + b**2 - 2 * a * b * cos(C))
            A = asin(a * sin(C) / c)
            B = radians(180) - A - C
        elif a and c and B:
            b = sqrt(a**2 + c**2 - 2 * a * c * cos(B))
            A = asin(a * sin(B) / b)
            C = radians(180) - A - B
        elif b and c and A:
            a = sqrt(b**2 + c**2 - 2 * b * c * cos(A))
            B = asin(b * sin(A) / a)
            C = radians(180) - A - B

    return {
        'a': round(a, 2) if a else None,
        'b': round(b, 2) if b else None,
        'c': round(c, 2) if c else None,
        'A': round(degrees(A), 2) if A else None,
        'B': round(degrees(B), 2) if B else None,
        'C': round(degrees(C), 2) if C else None
    }


def input_triangle():
    """
    Interactively solves a triangle based on user input.

    Returns:
        dict: The solved triangle's sides and angles.
    """
    diagram = r"""
              C
             / \
            /   \
         b /     \ a
          /       \
         /_________\
        A     c     B
    """
    print(diagram)
    print("Enter the known values. Leave unknowns blank.")

    a = input("Side a: ")
    b = input("Side b: ")
    c = input("Side c: ")
    A = input("Angle A (degrees): ")
    B = input("Angle B (degrees): ")
    C = input("Angle C (degrees): ")

    a = parse_input(a) if a else None
    b = parse_input(b) if b else None
    c = parse_input(c) if c else None
    A = parse_input(A) if A else None
    B = parse_input(B) if B else None
    C = parse_input(C) if C else None

    try:
        result = solve_triangle(a, b, c, A, B, C)
        print("\nSolved Triangle:")
        for key, value in result.items():
            print(f"{key}: {value:.2f}")
        input("Press enter to continue.")
        return result
    except ValueError as e:
        print(f"Error: {e}")
        input("Press enter to continue.")
        return None

if __name__ == "__main__":
	input_triangle()
