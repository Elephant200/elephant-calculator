from math import sin, cos, tan, radians, degrees, sqrt, asin, acos, atan, isclose
from utils.validators import parse_input

def solve_triangle(a=None, b=None, c=None, A=None, B=None, C=None):
    """
    Solves a general triangle given sufficient inputs using the law of sines, law of cosines,
    or by calling the right triangle solver if a right angle is present.

    Parameters:
        a, b, c (float): Sides of the triangle.
        A, B, C (float): Angles of the triangle in degrees.

    Returns:
        dict: Solved triangle with all sides and angles.

    Raises:
        ValueError: If insufficient or inconsistent inputs are provided.
    """
    known = 0
    known += (a is not None)
    known += (b is not None)
    known += (c is not None)
    known += (A is not None)
    known += (B is not None)
    known += (C is not None)
    if known < 3:
        raise ValueError("Need at least three known values (angles or sides) to solve a triangle.")
    if (a is None) and (b is None) and (c is None):
        raise ValueError("At least one side must be known.")

    A_rad = radians(A) if A is not None else None
    B_rad = radians(B) if B is not None else None
    C_rad = radians(C) if C is not None else None

    def sides_satisfy_triangle_inequality(x, y, z):
        return (x + y > z) and (y + z > x) and (z + x > y)

    if A == 90:
        if a is not None:
            if b is not None and c is not None:
                if abs(a**2 - (b**2 + c**2)) > 1e-7:
                    raise ValueError("Inconsistent data: a^2 != b^2 + c^2 for right triangle with A=90.")
                B_rad = asin(b / a)
                C_rad = asin(c / a)
            elif b is not None and c is None:
                temp = a**2 - b**2
                if temp <= 0:
                    raise ValueError("Inconsistent data: cannot compute c from a^2 - b^2.")
                c = sqrt(temp)
                B_rad = asin(b / a)
                C_rad = radians(90) - B_rad
            elif b is None and c is not None:
                temp = a**2 - c**2
                if temp <= 0:
                    raise ValueError("Inconsistent data: cannot compute b from a^2 - c^2.")
                b = sqrt(temp)
                C_rad = asin(c / a)
                B_rad = radians(90) - C_rad
            else:
                raise ValueError("Insufficient data for right triangle with A=90 (need at least 2 sides).")
        else:
            if b is not None and c is not None:
                a = sqrt(b**2 + c**2)
                B_rad = asin(b / a)
                C_rad = asin(c / a)
            else:
                raise ValueError("Insufficient data: A=90 but 'a' is unknown and we don't have both b and c.")
        A_rad = radians(90)
        if B_rad is None:
            if B is not None:
                B_rad = radians(B)
                C_rad = radians(90) - B_rad
            else:
                if C is not None:
                    C_rad = radians(C)
                    B_rad = radians(90) - C_rad
                else:
                    raise ValueError("Cannot find angles B or C, insufficient info.")
        if C_rad is None:
            C_rad = radians(90) - B_rad

    elif B == 90:
        if b is not None:
            if a is not None and c is not None:
                if abs(b**2 - (a**2 + c**2)) > 1e-7:
                    raise ValueError("Inconsistent data: b^2 != a^2 + c^2 for right triangle with B=90.")
                A_rad = asin(a / b)
                C_rad = asin(c / b)
            elif a is not None and c is None:
                temp = b**2 - a**2
                if temp <= 0:
                    raise ValueError("Inconsistent data: cannot compute c from b^2 - a^2.")
                c = sqrt(temp)
                A_rad = asin(a / b)
                C_rad = radians(90) - A_rad
            elif a is None and c is not None:
                temp = b**2 - c**2
                if temp <= 0:
                    raise ValueError("Inconsistent data: cannot compute a from b^2 - c^2.")
                a = sqrt(temp)
                C_rad = asin(c / b)
                A_rad = radians(90) - C_rad
            else:
                raise ValueError("Insufficient data for right triangle with B=90 (need at least 2 sides).")
        else:
            if a is not None and c is not None:
                b = sqrt(a**2 + c**2)
                A_rad = asin(a / b)
                C_rad = asin(c / b)
            else:
                raise ValueError("Insufficient data: B=90 but 'b' is unknown and we don't have both a and c.")
        B_rad = radians(90)
        if A_rad is None:
            if A is not None:
                A_rad = radians(A)
                C_rad = radians(90) - A_rad
            else:
                if C is not None:
                    C_rad = radians(C)
                    A_rad = radians(90) - C_rad
                else:
                    raise ValueError("Cannot find angles A or C, insufficient info.")
        if C_rad is None:
            C_rad = radians(90) - A_rad

    elif C == 90:
        if c is not None:
            if a is not None and b is not None:
                if abs(c**2 - (a**2 + b**2)) > 1e-7:
                    raise ValueError("Inconsistent data: c^2 != a^2 + b^2 for right triangle with C=90.")
                A_rad = asin(a / c)
                B_rad = asin(b / c)
            elif a is not None and b is None:
                temp = c**2 - a**2
                if temp <= 0:
                    raise ValueError("Inconsistent data: cannot compute b from c^2 - a^2.")
                b = sqrt(temp)
                A_rad = asin(a / c)
                B_rad = radians(90) - A_rad
            elif a is None and b is not None:
                temp = c**2 - b**2
                if temp <= 0:
                    raise ValueError("Inconsistent data: cannot compute a from c^2 - b^2.")
                a = sqrt(temp)
                B_rad = asin(b / c)
                A_rad = radians(90) - B_rad
            else:
                raise ValueError("Insufficient data for right triangle with C=90 (need at least 2 sides).")
        else:
            if a is not None and b is not None:
                c = sqrt(a**2 + b**2)
                A_rad = asin(a / c)
                B_rad = asin(b / c)
            else:
                raise ValueError("Insufficient data: C=90 but 'c' is unknown and we don't have both a and b.")
        C_rad = radians(90)
        if A_rad is None:
            if A is not None:
                A_rad = radians(A)
                B_rad = radians(90) - A_rad
            else:
                if B is not None:
                    B_rad = radians(B)
                    A_rad = radians(90) - B_rad
                else:
                    raise ValueError("Cannot find angles A or B, insufficient info.")
        if B_rad is None:
            B_rad = radians(90) - A_rad

    else:
        sides_known = sum(x is not None for x in (a, b, c))
        angles_known = sum(x is not None for x in (A_rad, B_rad, C_rad))

        if sides_known == 3:
            if not sides_satisfy_triangle_inequality(a, b, c):
                raise ValueError("Inconsistent sides: triangle inequality not satisfied.")
            A_rad = acos((b**2 + c**2 - a**2) / (2*b*c))
            B_rad = acos((a**2 + c**2 - b**2) / (2*a*c))
            C_rad = acos((a**2 + b**2 - c**2) / (2*a*b))

        elif angles_known == 2 and sides_known == 1:
            s = (A_rad or 0) + (B_rad or 0) + (C_rad or 0)
            m = radians(180) - s
            if A_rad is None:
                A_rad = m
            elif B_rad is None:
                B_rad = m
            else:
                C_rad = m
            if a is not None:
                ratio = a / sin(A_rad)
            elif b is not None:
                ratio = b / sin(B_rad)
            else:
                ratio = c / sin(C_rad)
            if a is None:
                a = ratio * sin(A_rad)
            if b is None:
                b = ratio * sin(B_rad)
            if c is None:
                c = ratio * sin(C_rad)

        elif sides_known == 2 and angles_known == 1:
            if A_rad is not None:
                known_angle_name, known_angle_val = 'A', A_rad
            elif B_rad is not None:
                known_angle_name, known_angle_val = 'B', B_rad
            else:
                known_angle_name, known_angle_val = 'C', C_rad
            side_names = []
            if a is not None: side_names.append('a')
            if b is not None: side_names.append('b')
            if c is not None: side_names.append('c')

            def angle_between_sides(ang, s1, s2):
                if ang == 'A' and (s1 in ['b','c'] and s2 in ['b','c']):
                    return True
                if ang == 'B' and (s1 in ['a','c'] and s2 in ['a','c']):
                    return True
                if ang == 'C' and (s1 in ['a','b'] and s2 in ['a','b']):
                    return True
                return False

            if angle_between_sides(known_angle_name, side_names[0], side_names[1]):
                if known_angle_name == 'A':
                    a = sqrt(b**2 + c**2 - 2*b*c*cos(A_rad))
                elif known_angle_name == 'B':
                    b = sqrt(a**2 + c**2 - 2*a*c*cos(B_rad))
                else:
                    c = sqrt(a**2 + b**2 - 2*a*b*cos(C_rad))
                if known_angle_name == 'A':
                    ratio = a / sin(A_rad)
                elif known_angle_name == 'B':
                    ratio = b / sin(B_rad)
                else:
                    ratio = c / sin(C_rad)
                if A_rad is None:
                    A_rad = asin(a / ratio)
                if B_rad is None:
                    B_rad = asin(b / ratio)
                if C_rad is None:
                    C_rad = asin(c / ratio)
            else:
                if known_angle_name == 'A' and a is not None:
                    ratio = a / sin(A_rad)
                    if b is not None and B_rad is None:
                        val = b / ratio
                        if abs(val) > 1:
                            raise ValueError("No real solution (SSA).")
                        B_rad = asin(val)
                    if c is not None and C_rad is None:
                        val = c / ratio
                        if abs(val) > 1:
                            raise ValueError("No real solution (SSA).")
                        C_rad = asin(val)
                elif known_angle_name == 'B' and b is not None:
                    ratio = b / sin(B_rad)
                    if a is not None and A_rad is None:
                        val = a / ratio
                        if abs(val) > 1:
                            raise ValueError("No real solution (SSA).")
                        A_rad = asin(val)
                    if c is not None and C_rad is None:
                        val = c / ratio
                        if abs(val) > 1:
                            raise ValueError("No real solution (SSA).")
                        C_rad = asin(val)
                elif known_angle_name == 'C' and c is not None:
                    ratio = c / sin(C_rad)
                    if a is not None and A_rad is None:
                        val = a / ratio
                        if abs(val) > 1:
                            raise ValueError("No real solution (SSA).")
                        A_rad = asin(val)
                    if b is not None and B_rad is None:
                        val = b / ratio
                        if abs(val) > 1:
                            raise ValueError("No real solution (SSA).")
                        B_rad = asin(val)
                else:
                    raise ValueError("SSA pattern but the side opposite the known angle is missing or mismatched.")
                angles_list = [('A', A_rad), ('B', B_rad), ('C', C_rad)]
                if sum(x[1] is not None for x in angles_list) == 2:
                    s = sum(x[1] for x in angles_list if x[1] is not None)
                    missing = radians(180) - s
                    for n, v in angles_list:
                        if v is None:
                            if n == 'A':
                                A_rad = missing
                            elif n == 'B':
                                B_rad = missing
                            else:
                                C_rad = missing
                            break
                angles_list = [('A', A_rad, a), ('B', B_rad, b), ('C', C_rad, c)]
                known_pair = None
                for nm, ang, sd in angles_list:
                    if ang is not None and sd is not None:
                        known_pair = (nm, ang, sd)
                        break
                if not known_pair:
                    raise ValueError("Cannot find a fully known side-angle pair to finish SSA solution.")
                ratio = known_pair[2] / sin(known_pair[1])
                for nm, ang, sd in angles_list:
                    if sd is None and ang is not None:
                        val = ratio * sin(ang)
                        if val < 0:
                            raise ValueError("No real solution (side ended up negative?).")
                        if nm == 'A':
                            a = val
                        elif nm == 'B':
                            b = val
                        elif nm == 'C':
                            c = val
        else:
            raise ValueError("Unsupported combination of known sides/angles for a non-right triangle.")

    if A_rad is None or B_rad is None or C_rad is None:
        raise ValueError("Could not solve all angles. Possibly insufficient or inconsistent data.")

    A_deg = degrees(A_rad)
    B_deg = degrees(B_rad)
    C_deg = degrees(C_rad)
    if abs(A_deg + B_deg + C_deg - 180) > 0.001:
        raise ValueError("Inconsistent or invalid data: angles do not sum to 180.")

    if a is not None and b is not None and c is not None:
        if not sides_satisfy_triangle_inequality(a, b, c):
            raise ValueError("Sides do not satisfy the triangle inequality.")

    return {
        'a': round(a, 2),
        'b': round(b, 2),
        'c': round(c, 2),
        'A': round(A_deg, 2),
        'B': round(B_deg, 2),
        'C': round(C_deg, 2)
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
