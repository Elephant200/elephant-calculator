def format_expression(expression, diff=False):
    if diff:
        expression = expression.replace("'", ".diff()")
    for i in list("wxyzabcd)"):
        for j in ['w','x','y','z','a','b','c','d','(','f','g','h','exp','ln','sin','cos','tan']:
            expression = expression.replace(f'{i}{j}', f'{i}*{j}')
            for k in range(10):
                expression = expression.replace(f'{i}^{k}{j}', f'({i}^{k})*{j}')
    expression = expression.replace(f'e^x', f'exp(x)')
    expression = expression.replace('e^', 'exp')
    expression = expression.replace('^', '**').replace(')(', ')*(').replace('infinity', 'oo').replace('infty', 'oo')
    for i in list("wxyzabcd(fe"):
        for num in range(10):
            expression = expression.replace(f'{num}{i}', f'{num}*{i}')
    return expression

def reverse_format(expression):
    expression = expression.replace('**', '^').replace(')*(', ')(').replace('x*(', 'x(')
    for i in range(10):
        expression = expression.replace(f'{i}*', f'{i}')
    for i in list("wxyzabcd)"):
        for j in ['w','x','y','z','a','b','c','d','(','f','g','h','exp','ln','sin','cos','tan']:
            expression = expression.replace(f'{i}*{j}', f'{i}{j}')
    return expression

def trim_trailing_zeroes(expression):
    """
    Trims trailing zeros from a string representation of a decimal number.

    Args:
        expression: A representation of the number.

    Returns:
        str: The simplified number string with excess trailing zeros removed.
    """
    if type(expression) != str:
        expression = str(expression)
    if '.' in expression:
        integer_part, fractional_part = expression.split('.')
        fractional_part = fractional_part.rstrip('0')
        return integer_part if not fractional_part else f"{integer_part}.{fractional_part}"
    return expression