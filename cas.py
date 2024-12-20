from sympy import *
w, x, y, z, a, b, c, d = symbols("w x y z a b c d")

import os
import platform

clear_cmd = "cls" if platform.system() == "Windows" else "clear"
def clear():
    os.system(clear_cmd)

elephant = r"""            
            __     __
           /  \~~~/  \
     ,----(     ..    )
    /      \__     __/
   /|         (\  |(
  ^ \   /___\  /\ |   
     |__|   |__|-"    
"""

# Converts a human-readable expression into something sympy understands
def formatExp(expression, diff=False):
	if diff:
		#expression = expression.replace("y", "f(x)")
		#while expression.replace("'", ".diff()") != expression:
		expression = expression.replace("'", ".diff()")
	for i in list("wxyzabcd)"):
		for j in ['w','x','y','z','a','b','c','d','(','f','g','h','exp','ln','sin','cos','tan']:
			expression = expression.replace('%s%s' % (i,j), '%s*%s' % (i,j))
			for k in range(10): expression = expression.replace('%s^%s%s' % (i, k, j), '(%s^%s)*%s' % (i, k, j))
	expression = expression.replace('^', '**').replace(')(', ')*(').replace('infinity','oo').replace('infty','oo').replace('e^%s' % x,'exp(%s)' % x)
	for i in list("wxyzabcd(fe"):
		expression = expression.replace('0%s' % i,'0*%s' % i).replace('2%s' % i,'2*%s' % i).replace('3%s' % i,'3*%s' % i).replace('4%s' % i,'4*%s' % i).replace('5%s' % i,'5*%s' % i).replace('6%s' % i,'6*%s' % i).replace('7%s' % i,'7*%s' % i).replace('8%s' % i,'8*%s' % i).replace('9%s' % i,'9*%s' % i)
	return expression

def reverseFormat(expression):
	expression = expression.replace('**', '^').replace(')*(', ')(').replace('x*(','x(')
	expression = expression.replace('0*%s' % x,'0%s' % x).replace('2*%s' % x,'2%s' % x).replace('3*%s' % x,'3%s' % x).replace('4*%s' % x,'4%s' % x).replace('5*%s' % x,'5%s' % x).replace('6*%s' % x,'6%s' % x).replace('7*%s' % x,'7%s' % x).replace('8*%s' % x,'8%s' % x).replace('9*%s' % x,'9%s' % x)
	expression = expression.replace('0*(', '0(').replace('2*(','2(').replace('3*(','3(').replace('4*(','4(').replace('5*(','5(').replace('6*(','6(').replace('7*(','7(').replace('8*(','8(').replace('9*(','9(')
	for i in list("wxyzabcd)"):
		for j in ['w','x','y','z','a','b','c','d','(','f','g','h','exp','ln','sin','cos','tan']:
			expression = expression.replace('%s*%s' % (i,j), '%s%s' % (i,j))
	return expression

# print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")

def hub():
	clear()
	print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
	task = input("Please enter the task. (type QUIT to exit)\n1. Factor\n2. Expand\n3. Simplify\n4. Solvers\n5. Derivative\n6. Indefinite Integrals\n7. Definite Integrals\n")
	if task.startswith('1'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
		expression = formatExp(input("\nTask: Factor\nPlease input your expression.\n"))
		try: input("Result: " + reverseFormat(str(factor(expression))))
		except:	input("Sorry, your input could not be interpreted. Please try again.")
	elif task.startswith('2'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
		expression = formatExp(input("\nTask: Expand\nPlease input your expression.\n"))
		try: input("Result: " + reverseFormat(str(expand(expression))))
		except:	input("Sorry, your input could not be interpreted. Please try again.")
	elif task.startswith('3'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
		expression = formatExp(input("\nTask: Simplify\nPlease input your expression.\n"))
		try: input("Result: " + reverseFormat(str(simplify(expression))))
		except:	input("Sorry, your input could not be interpreted. Please try again.")
	elif task.startswith('4'):
		solving()
	elif task.startswith('5'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
		expression = formatExp(input("\nTask: Derivatives\nPlease input your expression.\n"))
		try: input("Result: " + reverseFormat(str(eval(expression).diff())))
		except:	input("Sorry, your input could not be interpreted. Please try again.")
	elif task.startswith('6'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
		expression = formatExp(input("\nTask: Indefinite Integrals\nPlease input your expression\n"))
		variable = Symbol(input("What variable would you like to integrate with respect to? ")[0])
		try: input("Result: " + reverseFormat(str(integrate(expression,variable))))
		except:	input("Sorry, your input could not be interpreted. Please try again.")
	elif task.startswith('7'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
		expression = formatExp(input("\nTask: Definite Integrals\nPlease input your expression\n"))
		variable = Symbol(input("What variable would you like to integrate over? ")[0])
		lowerLim = float(eval(formatExp(input("Lower limit: "))))
		upperLim = float(eval(formatExp(input("Upper limit: "))))
		try: input("Result: " + reverseFormat(str(integrate(expression,(variable, lowerLim, upperLim)))))
		except:	input("Sorry, your input could not be interpreted. Please try again.")
	elif task.startswith('8'):
		clear()
		if not input("Are you sure? This can crash the computer.").startswith('y'): hub()
		graphing()
	if task.upper().startswith('Q'): return
	hub()

def solving():
	clear()
	print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
	task = input("Please enter type of equation you would like to input.\n1. Single-variable Equation\n2. Multivariable Equations\n3. Differential Equation\n")
	if task.startswith('1'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
		var = input("In what variable will your equation be? ")
		try:
			equation = input("Write your equation (in x) below.\n").split("=")
			equation[0],equation[1] = formatExp(equation[0].strip()), formatExp(equation[1].strip())
			input("Solution set:\n" + reverseFormat(str(solveset(Eq(eval(equation[0]), eval(equation[1])), eval(var)))))
		except Exception as error:
			input("Sorry, your input could not be interpreted. Please try again.\nError: " + str(error))
			solving()
	elif task.startswith('2'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
		vars = input("What variables will your equation have? Separate with commas. ").split(', ')
		equations = []
		try:
			while True:
				for i in range(len(vars)):
					try: vars[i] = eval(vars[i])
					except: 
						print("Sorry, this variable is not supported. Please pick a different set of variables.")
						vars = input("What variables will your equation have? Separate with commas. ").split(', ')
						break
				break
			for i in range(len(vars)):
				equation = input(f"Equation {i+1}: ").split('=')
				equation[0],equation[1] = formatExp(equation[0].strip()), formatExp(equation[1].strip())
				equations.append(Eq(eval(equation[0]), eval(equation[1])))
			input("Solutions:\n" + reverseFormat(str(solve(equations, vars, dict=True))))
		except:
			input("Sorry, your input could not be interpreted. Please try again. ")
			solving()
	elif task.startswith('3'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n" + elephant + "\n")
		y = Function('y')(x)
		try:
			equation = input("Please enter your differential equation. Use y' for the derivative of y.\n").split('=')
			equation[0],equation[1] = formatExp(equation[0].strip(), True), formatExp(equation[1].strip(), True)
		except:
			input("Sorry, your input could not be interpreted. Please try again. ")
			solving()
		try: 
			solution = dsolve(Eq(eval(equation[0]), eval(equation[1])), y)
			LHS = solution.lhs
			RHS = solution.rhs
			input("Solution:\n" + reverseFormat(str(LHS)) + " = " + reverseFormat(str(RHS)))
		except Exception as e: 
			print("Error: " + str(e))
			input("Sorry, your differential equation could not be solved. Please try a different differential equation. ")

#DANGEROUS--CAN CRASH COMPUTER
def graphing():
	clear()
	print("The Elephant CAS (computer algebra system)\nPowered by sympy\n and matplotlib\n\nThe Graphing Calculator\n")
	task = input("Please enter the task. (type QUIT to exit)\n1. 2d Functions\n2. 2d Parametric\n3. 3d Functions\n4. 3d Parametric\n")
	if task.startswith('1'):
		clear()
		print("The Elephant CAS (computer algebra system)\nPowered by sympy\n and matplotlib\n\nThe Graphing Calculator\n")
		numFuncs = int(input("How many functions would you like to graph? "))
		function = "plot("
		for i in range(numFuncs): 
			function += str((formatExp(input(f"Please input function {i}: ")), (Symbol(input("Independent Variable: ")[0]), float(eval(input("Lower bound: "))), float(eval(input("Upper bound: "))))))
			if i < numFuncs-1: function += ", "
		function += ")"
		input(function)
		#DANGEROUS--CAN CRASH COMPUTER