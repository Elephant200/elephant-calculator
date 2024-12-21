from math import sqrt, gcd
import os

def calculate_columns(column_width):
    """
    Calculate the number of columns that can fit in the terminal based on the column width.
    """
    terminal_width = os.get_terminal_size().columns
    return max(1, terminal_width // column_width)

def calculate_column_width(limit):
    """
    Calculate the column width based on the largest possible triple (limit, limit, limit).
    """
    largest_triple = (limit, limit, limit)
    return len(str(largest_triple)) + 4  # Add padding for spacing

def print_in_columns(triple, column_width, count, columns):
    """
    Prints a single triple in the appropriate column layout.
    """
    print(f"{triple!s:<{column_width}}", end="")
    if (count + 1) % columns == 0:
        print()

def generate(n, printIt=True): # n is the highest hypotenuse allowed
    print("Pythagorean Triples:\n")
    triples = []
    if printIt:
        column_width = calculate_column_width(n)
        columns = calculate_columns(column_width)
        count = 0
    for i in range(5, n): # searches every possible hypotenuse length
        for j in range(3, i): # searches every possible leg length
            k = sqrt(i * i - j * j) # calculates other leg length
            if k.is_integer(): # checks if other leg length is an integer
                k = int(k)
                if j < k: # adds the triple (only once)
                    triples.append((j, k, i))
                    if printIt:
                        print_in_columns((j, k, i), column_width, count, columns)
                        count += 1
    if printIt and count % columns != 0:
        print()
    return triples

def generatePrimitive(n, printIt=True):
    print("Primitive Pythagorean Triples:\n")
    triples = []
    if printIt:
        column_width = calculate_column_width(n)
        columns = calculate_columns(column_width)
        count = 0
    for i in range(5, n): # searches every possible hypotenuse length
        for j in range(3, i): # searches every possible leg length
            k = sqrt(i * i - j * j) # calculates other leg length
            if k.is_integer(): # checks if other leg length is an integer
                k = int(k)
                if j < k and gcd(i, gcd(j, k)) == 1: # adds the triple only if primitive
                    triples.append((j, k, i))
                    if printIt:
                        print_in_columns((j, k, i), column_width, count, columns)
                        count += 1
    if printIt and count % columns != 0:
        print()
    return triples
