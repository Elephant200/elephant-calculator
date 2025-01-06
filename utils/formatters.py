def format_expression(expression, diff=False):
    if diff:
        expression = expression.replace("'", ".diff()")
    for i in list("wxyzabcd)"):
        for j in ['w','x','y','z','a','b','c','d','(','f','g','h','exp','ln','sin','cos','tan']:
            expression = expression.replace(f'{i}{j}', f'{i}*{j}')
            for k in range(10):
                expression = expression.replace(f'{i}^{k}{j}', f'({i}^{k})*{j}')
    expression = expression.replace('^', '**').replace(')(', ')*(').replace('infinity', 'oo').replace('infty', 'oo').replace(f'e^{x}', f'exp({x})')
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