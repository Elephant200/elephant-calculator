from sympy import *
import os
import platform
from utils.formatters import format_expression, reverse_format

w, x, y, z, a, b, c, d = symbols("w x y z a b c d")

clear_cmd = "cls" if platform.system() == "Windows" else "clear"
def clear():
    os.system(clear_cmd)

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

def cas_cli():
    elephant = r"""            
            __     __
           /  \~~~/  \
     ,----(     ..    )
    /      \__     __/
   /|         (\  |(
  ^ \   /___\  /\ |   
     |__|   |__|-"    
"""
    while True:
        clear()
        print("The Elephant CAS (Computer Algebra System)\nPowered by sympy")
        print(elephant)
        print("\nPlease enter the task. (type QUIT to exit)")
        print("1. Factor")
        print("2. Expand")
        print("3. Simplify")
        print("4. Derivative")
        print("5. Indefinite Integrals")
        print("6. Definite Integrals")
        print("7. Solve Single-Variable Equation")
        print("8. Solve Multi-Variable Equations")
        print("9. Solve Differential Equation")
        task = input()

        if task.upper().startswith('Q'):
            print("Goodbye!")
            break

        if task == '1':
            clear()
            print(elephant)
            expression = input("\nTask: Factor\nPlease input your expression: ")
            input("Result: " + factor_expression(expression))

        elif task == '2':
            clear()
            print(elephant)
            expression = input("\nTask: Expand\nPlease input your expression: ")
            input("Result: " + expand_expression(expression))

        elif task == '3':
            clear()
            print(elephant)
            expression = input("\nTask: Simplify\nPlease input your expression: ")
            input("Result: " + simplify_expression(expression))

        elif task == '4':
            clear()
            print(elephant)
            expression = input("\nTask: Derivative\nPlease input your expression: ")
            input("Result: " + derivative(expression))

        elif task == '5':
            clear()
            print(elephant)
            expression = input("\nTask: Indefinite Integrals\nPlease input your expression: ")
            variable = input("What variable would you like to integrate with respect to? ")
            input("Result: " + indefinite_integral(expression, variable))

        elif task == '6':
            clear()
            print(elephant)
            expression = input("\nTask: Definite Integrals\nPlease input your expression: ")
            variable = input("What variable would you like to integrate over? ")
            lower_limit = input("Lower limit: ")
            upper_limit = input("Upper limit: ")
            input("Result: " + definite_integral(expression, variable, lower_limit, upper_limit))

        elif task == '7':
            clear()
            print(elephant)
            equation = input("\nTask: Solve Single-Variable Equation\nWrite your equation (e.g., x^2=4): ")
            variable = input("In what variable will your equation be? ")
            input("Result: " + solve_single_variable(equation, variable))

        elif task == '8':
            clear()
            print(elephant)
            variables = input("\nTask: Solve Multi-Variable Equations\nWhat variables will your equation have? Separate with commas: ")
            num_eqs = int(input("How many equations will you input? "))
            equations = []
            for i in range(num_eqs):
                equations.append(input(f"Equation {i+1}: "))
            input("Result: " + solve_multivariable(equations, variables))

        elif task == '9':
            clear()
            print(elephant)
            equation = input("\nTask: Solve Differential Equation\nPlease enter your differential equation (e.g., y'+y=0): ")
            input("Result: " + solve_differential(equation))

        else:
            clear()
            print(elephant)
            input("Invalid selection. Please try again.")

if __name__ == "__main__":
    cas_cli()