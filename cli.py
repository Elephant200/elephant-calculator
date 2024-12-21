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
from services.cas import cas_cli
clear()
print(" - Loading os... DONE\n - Loading sys... DONE\n - Loading time... DONE\n - Loading sympy... DONE\n - Loading files... ")
from inputimeout import inputimeout
from services.geometry import area, perimeter, volume, surface_area
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
        func = input("What function would you like to use?\n1. Square Root Calculator\n2. nth Root Calculator\n3. Power of a Number Calculator\n4. Digits of pi\n5. Digits of e\n6. Sine\n\n7. Cosine\n8. Tangent\n9. Inverse Trig Functions\n0. Legacy Algorithms (not recommended)\n").lower()
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
        elif func.startswith('7'): #cos
            print("Output:\n" + str(irr.cos(float(input("What angle (in degrees) would you like to find the cosine of? ")), int(input("How many decimal places would you like? ")), False)))
        elif func.startswith('8'): #tan
            print("Output:\n" + str(irr.tan(float(input("What angle (in degrees) would you like to find the tangent of? ")), int(input("How many decimal places would you like? ")), False)))
        elif func.startswith('9'): #inverse
            subfunc = input("1. arcsin\n2. arccos\n3. arctan")
            if subfunc.startswith('1'):
                print("Output:\n" + str(irr.arcsin(float(input("What would you like to find the inverse sine of? ")), int(input("How many decimal places would you like? ")), True)))
            if subfunc.startswith('2'):
                print("Output:\n" + str(irr.arccos(float(input("What would you like to find the inverse cosine of? ")), int(input("How many decimal places would you like? ")), True)))
            if subfunc.startswith('3'):
                print("Output:\n" + str(irr.arctan(float(input("What would you like to find the inverse tangent of? ")), int(input("How many decimal places would you like? ")), True)))
        elif func.startswith('0'):
            clear()
            print(elephant)
            func = input("What legacy function would you like to use?\n1. Gauss-Legendre Algorithm (PI)\n2. Taylor Series for E\n")
            if func.startswith('1'): print("Output:\n" + str(irr.gauss_legendre(int(input("How many decimal places would you like? ")) + 1)))
            elif func.startswith('2'): print("Output:\n" + str(irr.taylorE(int(input("How many decimal places would you like? ")))))
    elif func.startswith('3'):
        print("Area: " + str(area(input("What shape would you like to find the area of? "))))
    elif func.startswith('4'):
        print("Perimeter: " + str(perimeter(input("What shape would you like to find the perimeter of? "))))
    elif func.startswith('5'):
        print("Volume: " + str(volume(input("What solid would you like to find the volume of? "))))
    elif func.startswith('6'):
        print("Surface Area: " + str(surface_area(input("What solid would you like to find the surface area of? "))))
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