from sympy import *
w, x, y, z, a, b, c, d = symbols("w x y z a b c d")

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

def factor_expression(expression):
    try:
        formatted = format_expression(expression)
        return reverse_format(str(factor(formatted)))
    except Exception as e:
        return f"Error: {str(e)}"

def expand_expression(expression):
    try:
        formatted = format_expression(expression)
        return reverse_format(str(expand(formatted)))
    except Exception as e:
        return f"Error: {str(e)}"

def simplify_expression(expression):
    try:
        formatted = format_expression(expression)
        return reverse_format(str(simplify(formatted)))
    except Exception as e:
        return f"Error: {str(e)}"

def derivative(expression):
    try:
        formatted = format_expression(expression)
        return reverse_format(str(eval(formatted).diff()))
    except Exception as e:
        return f"Error: {str(e)}"

def indefinite_integral(expression, variable):
    try:
        formatted = format_expression(expression)
        var = Symbol(variable)
        return reverse_format(str(integrate(formatted, var)))
    except Exception as e:
        return f"Error: {str(e)}"

def definite_integral(expression, variable, lower_limit, upper_limit):
    try:
        formatted = format_expression(expression)
        var = Symbol(variable)
        lower = float(eval(format_expression(lower_limit)))
        upper = float(eval(format_expression(upper_limit)))
        return reverse_format(str(integrate(formatted, (var, lower, upper))))
    except Exception as e:
        return f"Error: {str(e)}"

def solve_single_variable(equation, variable):
    try:
        left, right = equation.split('=')
        left = format_expression(left.strip())
        right = format_expression(right.strip())
        var = Symbol(variable)
        return reverse_format(str(solveset(Eq(eval(left), eval(right)), var)))
    except Exception as e:
        return f"Error: {str(e)}"

def solve_multivariable(equations, variables):
    try:
        vars = [Symbol(v.strip()) for v in variables.split(',')]
        eq_list = []
        for eq in equations:
            left, right = eq.split('=')
            eq_list.append(Eq(eval(format_expression(left.strip())), eval(format_expression(right.strip()))))
        return reverse_format(str(solve(eq_list, vars, dict=True)))
    except Exception as e:
        return f"Error: {str(e)}"

def solve_differential(equation):
    try:
        left, right = equation.split('=')
        left = format_expression(left.strip(), diff=True)
        right = format_expression(right.strip(), diff=True)
        y = Function('y')(x)
        solution = dsolve(Eq(eval(left), eval(right)), y)
        return reverse_format(str(solution.lhs)) + " = " + reverse_format(str(solution.rhs))
    except Exception as e:
        return f"Error: {str(e)}"
