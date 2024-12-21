from math import sin, cos, tan, radians, degrees, sqrt, asin, acos, atan

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
    if sum(1 for x in [a, b, c, A, B, C] if x is not None) < 3:
        raise ValueError("At least three parameters (including one side) are required to solve the triangle.")

    if A: A = radians(A)
    if B: B = radians(B)
    if C: C = radians(C)

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
        'a': a,
        'b': b,
        'c': c,
        'A': degrees(A),
        'B': degrees(B),
        'C': degrees(C)
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

    a = eval(a) if a else None
    b = eval(b) if b else None
    c = eval(c) if c else None
    A = eval(A) if A else None
    B = eval(B) if B else None
    C = eval(C) if C else None

    try:
        result = solve_triangle(a, b, c, A, B, C)
        print("\nSolved Triangle:")
        for key, value in result.items():
            print(f"{key}: {value:.2f}")
        return result
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    input_triangle()
