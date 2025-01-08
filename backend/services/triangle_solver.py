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
    """
    if sum(1 for x in [a, b, c, A, B, C] if x is not None) < 3:
        raise ValueError("At least three parameters (including one side) are required to solve the triangle.")

    # Convert angles to radians
    if A is not None: A = radians(A)
    if B is not None: B = radians(B)
    if C is not None: C = radians(C)

    # Right triangle handling
    if C and is_right_angle(C):
        if a and b:
            c = sqrt(a**2 + b**2)
        elif a and c:
            b = sqrt(c**2 - a**2)
        elif b and c:
            a = sqrt(c**2 - b**2)
        else:
            raise ValueError("Insufficient data to solve the right triangle.")
        A = atan(a / b) if b else radians(90)
        B = radians(90) - A
    elif A and is_right_angle(A):
        if b and c:
            a = sqrt(c**2 - b**2)
        elif a and c:
            b = sqrt(c**2 - a**2)
        elif a and b:
            c = sqrt(a**2 + b**2)
        else:
            raise ValueError("Insufficient data to solve the right triangle.")
        C = atan(b / a) if a else radians(90)
        B = radians(90) - C
    elif B and is_right_angle(B):
        if a and c:
            b = sqrt(c**2 - a**2)
        elif b and c:
            a = sqrt(c**2 - b**2)
        elif a and b:
            c = sqrt(a**2 + b**2)
        else:
            raise ValueError("Insufficient data to solve the right triangle.")
        A = atan(a / b) if b else radians(90)
        C = radians(90) - A
    else:
        # Use the law of sines or law of cosines based on available data
        if a and b and c:
            A = acos((b**2 + c**2 - a**2) / (2 * b * c))
            B = acos((a**2 + c**2 - b**2) / (2 * a * c))
            C = acos((a**2 + b**2 - c**2) / (2 * a * b))
        elif a and b and A:
            B = asin(b * sin(A) / a)
            C = radians(180) - A - B
            c = a * sin(C) / sin(A)
        elif a and c and A:
            C = asin(c * sin(A) / a)
            B = radians(180) - A - C
            b = a * sin(B) / sin(A)
        elif b and c and B:
            C = asin(c * sin(B) / b)
            A = radians(180) - B - C
            a = b * sin(A) / sin(B)
        elif a and c and C:
            A = asin(a * sin(C) / c)
            B = radians(180) - A - C
            b = a * sin(B) / sin(A)
        elif a and b and C:
            A = asin(a * sin(C) / c)
            B = radians(180) - A - C
            c = a * sin(C) / sin(A)
        else:
            raise ValueError("Insufficient or inconsistent data to solve the triangle.")

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
		 c /     \ b
		  /       \
		 /_________\
		A     a     B
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
