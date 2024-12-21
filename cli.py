# Author: Elephant200
# See README.md for more information.


# Loading screen during imports
print(" - Loading os...\n - Loading sys...\n - Loading time...\n - Loading sympy...\n - Loading files... ")
import os
import platform
clear_cmd = "cls" if platform.system() == "Windows" else "clear"
def clear():
    os.system(clear_cmd)

clear()
print(" - Loading os... DONE\n - Loading sys...\n - Loading time...\n - Loading sympy...\n - Loading files... ")
import sys
from time import sleep, time
clear()
print(" - Loading os... DONE\n - Loading sys... DONE\n - Loading time... DONE\n - Loading sympy...\n - Loading files... ")
from services.cas import (
    factor_expression, expand_expression, simplify_expression,
    derivative, indefinite_integral, definite_integral,
    solve_single_variable, solve_multivariable, solve_differential
)
clear()
print(" - Loading os... DONE\n - Loading sys... DONE\n - Loading time... DONE\n - Loading sympy... DONE\n - Loading files... ")
from inputimeout import inputimeout
from services.geoFormulas import Area, Perimeter, Volume, SurfaceArea
from services import vectorCalc as vm
from services import triangleSolver as triangle
from services import irrationals as irr
from services import pythagGen as pythag
from services import primeGen as prime
from services import cas
clear()
print(" - Loading os... DONE\n - Loading sys... DONE\n - Loading time... DONE\n - Loading sympy... DONE\n - Loading files... DONE")
clear()

# Calculates current rating
try:
    with open("reviews/ratings.txt", 'r') as f: ratings = f.readline().strip().split(' ')
    for i in range(len(ratings)): ratings[i] = int(ratings[i])
    rating = round(float(sum(ratings)/len(ratings)), 1)
    n = len(ratings)
except Exception:
    rating, n = "unrated", 0

ELEPHANT = r"""                            _
                          .' `'.__
                         /      \ `'"-,
        .-''''--...__..-/ .     |      \
      .'               ; :'     '.  a   |
     /                 | :.       \     =\
    ;                   \':.      /  ,-.__;.-;`
   /|     .              '--._   /-.7`._..-;`
  ; |       '                |`-'      \  =|
  |/\        .   -' /     /  ;         |  =/
  (( ;.       ,_  .:|     | /     /\   | =|
   ) / `\     | `""`;     / |    | /   / =/
     | ::|    |      \    \ \    \ `--' =/
    /  '/\    /       )    |/     `-...-`
   /    | |  `\    /-'    /;
   \  ,,/ |    \   D    .'  \
    `""`   \    ""'"_.-'""
"""
elephant = r"""            __     __
           /  \~~~/  \
     ,----(     ..    )
    /      \__     __/
   /|         (\  |(
  ^ \   /___\  /\ |   
     |__|   |__|-"    
"""

# Initial Messages
print(f"Welcome to the Elephant Calculator!\n{ELEPHANT}\nCurrently rated %s/5 (%s ratings) at CalculatorRatings.\n" % (rating, n))
if input("Would you like to see the instructions? (y/n) ").startswith("y"):
    clear()
    print("INSTRUCTIONS")
    print("This is a calculator with many functions in numerous categories.\nEach calculator requests inputs. Note that only integers and decimals are supported.\nTo quit the program, type QUIT at the main page.\nAn option to write a review will be provided after the program is exited.")
if input("Would you like to read the reviews? (y/n) ").startswith('y'):
    clear()
    with open("reviews/reviews.txt", 'r') as f:
        num = 0
        for x in f.readlines():
            x = x.strip()
            if x == "<<REVIEW BREAK>>":
                print()
                num += 1
                x = "=" * (os.get_terminal_size()[0] // 2 - len("REVIEW %s" % num) // 2) + "REVIEW %s" % num + "=" * (os.get_terminal_size()[0] // 2 - len("REVIEW %s" % num) // 2)
            print(x)

func = ''

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
        print("The Elephant CAS (Command Line Interface)")
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
            num_eqs = int(input("\nTask: Solve Multi-Variable Equations\nHow many equations will you input? "))
            equations = []
            for i in range(num_eqs):
                equations.append(input(f"Equation {i+1}: "))
            variables = input("What variables will your equation have? Separate with commas: ")
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

while True:
    if func != "<<#TRIANGLE SOLVER#>>" and func != "<<#CAS#>>": input("\nPress Enter to continue.")
    clear()
    print(elephant)
    func = input("What category of functions would you like to use? (type QUIT to exit)\n1. Vectors and Matrices\n2. High-Precision Calculator\n3. Area\n4. Perimeter\n5. Volume\n6. Surface Area\n7. Triangle Solver\n8. Pythagorean Triple Generator\n9. Prime Numbers\n0. CAS (computer algebra system)\n").lower()
    clear()
    print(elephant)
    if func.startswith("q"): break
    if func.startswith('1'):
        func = input("What function would you like to use?\n1. Add Matrices\n2. Subtract Matrices\n3. Vector-matrix Multiplication\n4. Matrix-matrix Multiplication\n5. Matrix Exponentiation\n6. Determinant\n7. Invert Matrix\n8. Vector Cross Product\n9. Vector Dot Product").lower()
        clear()
        print(elephant)
        if func.startswith('1'):
            print("Output:\n" + str(vm.add(vm.inputMatrix(), vm.inputMatrix())))
        elif func.startswith('2'):
            print("Output:\n" + str(vm.subtract(vm.inputMatrix(), vm.inputMatrix())))
        elif func.startswith('3'):
            print("Output:\n" + str(vm.multiplyVM(vm.inputVector(), vm.inputMatrix())))
        elif func.startswith('4'):
            print("Output:\n" + str(vm.multiplyMM(vm.inputMatrix(), vm.inputMatrix())))
        elif func.startswith('5'):
            print("Output:\n" + str(vm.pow(vm.inputMatrix(), int(input("To what power would you like to bring this matrix?")))))
        elif func.startswith('6'):
            print("Output:\n" + str(vm.det(vm.inputMatrix())))
        elif func.startswith('7'):
            print("Output:\n" + str(vm.inverse(vm.inputMatrix())))
        elif func.startswith('8'):
            print("Output:\n" + str(vm.cross(vm.inputVector(), vm.inputVector())))
        elif func.startswith('9'):
            print("Output:\n" + str(vm.dot(vm.inputVector(), vm.inputVector())))
        #input()
    elif func.startswith('2'):
        func = input("What function would you like to use?\n1. Square Root Calculator\n2. nth Root Calculator\n3. Power of a Number Calculator\n4. Digits of pi\n5. Digits of e\n6. Sine\n7. Legacy Algorithms\n").lower()
        clear()
        print(elephant)
        if func.startswith('1'):
            print("Output:\n" + str(irr.sqrt(float(input("What value would you like to take the square root of? ")), int(input("How many decimal places would you like? ")))))
        elif func.startswith('2'):
            print("Output:\n" + str(irr.nRoot(float(input("What value would you like to take the nth root of? ")), int(input("What root would you like to take? ")), int(input("How many decimal places would you like? ")))))
        elif func.startswith('3'):
            print("Output:\n" + str(irr.power(float(input("What value would you like to take the nth power of? ")), int(input("What power would you like to take? ")), int(input("How many decimal places would you like? ")))))
        elif func.startswith('4'):
            print("Output:\n" + str(irr.chudnovsky(int(int(input("How many decimal places would you like? ")) / 8))))
        elif func.startswith('5'):
            print("Output:\n" + str(irr.advancedE(int(int(input("How many decimal places would you like? "))))))
        elif func.startswith('6'): #sin
            print("Output:\n" + str(irr.sin(float(input("What angle (in degrees) would you like to find the sine of? ")), int(input("How many decimal places would you like? ")), False)))
        elif func.startswith('7'):
            clear()
            print(elephant)
            func = input("What legacy function would you like to use?\n1. Gauss-Legendre Algorithm (PI)\n2. Taylor Series for E\n")
            if func.startswith('1'): print("Output:\n" + str(irr.gauss_legendre(int(input("How many decimal places would you like? ")) + 1)))
            elif func.startswith('2'): print("Output:\n" + str(irr.taylorE(int(input("How many decimal places would you like? ")))))
    elif func.startswith('3'):
        print("Area: " + str(Area.area(input("What shape would you like to find the area of? "))))
    elif func.startswith('4'):
        print("Perimeter: " + str(Perimeter.perimeter(input("What shape would you like to find the perimeter of? "))))
    elif func.startswith('5'):
        print("Volume: " + str(Volume.vol(input("What solid would you like to find the volume of? "))))
    elif func.startswith('6'):
        print("Surface Area: " + str(SurfaceArea.sa(input("What solid would you like to find the surface area of? "))))
    elif func.startswith('7'):
        func = "<<#TRIANGLE SOLVER#>>"
        triangle.triangle()
    elif func.startswith('8'):
        if input("Would you like to generate\n1. Primitive Pythagorean Triples\n2. Any Pythagorean Triple\n").startswith('1'): pythag.generatePrimitive(int(input("What is the maximum hypotenuse length you would like to allow? ")))
        else: pythag.generate(int(input("What is the maximum hypotenuse length you would like to allow? ")))
    elif func.startswith('9'):
        func = input("Would you like to\n1. Determine if a number is prime\n2. Calculate the nth prime number\n3. Generate the first n prime numbers\n4. Find the prime factorization of a number\n")
        if func.startswith('1'): print(prime.isPrime(int(input("Number to test: "))))
        elif func.startswith('2'): print(prime.nthPrime(int(input("n = "))))
        elif func.startswith('3'): print(prime.firstPrimes(int(input("n = "))))
        elif func.startswith('4'): print(prime.strPrimeFacs(int(input("n = "))))
    elif func.startswith('0'):
        func = "<<#CAS#>>"
        cas_cli()
    elif func.startswith('admin'):
        if input("Password: ") == "elephantus":
            print("Sucess! Admin mode entered. ")
            while True:
                func = input("Please select your command.\n1. Reset ratings\n2. Reset reviews\n3. Bulk add reviews\n")
                clear()
                if func.startswith('1'):
                    with open("reviews/ratings.txt", "w") as f: pass
                    print("Ratings.txt Cleared.")
                elif func.startswith('2'):
                    with open("reviews/reviews.txt", "w") as f: pass
                    print("Reviews.txt Cleared.")
                elif func.startswith('3'):
                    while not input("Type STOP to stop.").upper().startswith('S'):
                        clear()
                        with open('reviews/reviews.txt', 'a') as f:
                            f.write("<<REVIEW BREAK>>\n")
                            f.write("Name:   " + input("What is your name? ")+"\n")
                            stars = int(input("How many stars would you like to give? (out of 5)")[0])
                            f.write("Stars:  " + ("*" * stars) + "\n")
                            f.write("Review: " + input("Please write your review here. ")+"\n")
                        with open('reviews/ratings.txt', 'a') as f:
                            f.write(str(stars) + " ")
                elif func.lower().startswith('q'): break
    else:
        print("Invalid input. Please try again.")

try:
    if inputimeout(prompt="Thank you for using the Elephant Calculator. If you would like to leave a review, please type \"yes\".", timeout=5).startswith('y'):
        with open('reviews/reviews.txt', 'a') as f:
            f.write("<<REVIEW BREAK>>\n")
            f.write("Name:   " + input("What is your name? ")+"\n")
            stars = int(input("How many stars would you like to give? (out of 5)")[0])
            if stars > 5: stars = 5
            if stars < 1: stars = 1
            f.write("Stars:  " + ("*" * stars) + "\n")
            f.write("Review: " + input("Please write your review here. ")+"\n")
        with open('reviews/ratings.txt', 'a') as f:
            f.write(str(stars) + " ")
except: pass
print("See you soon! ")