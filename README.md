# The Elephant Calculator #
## TABLE OF CONTENTS ##
1. Overview
2. Calculator Functions Explanations
3. About the Programmer

## Overview ##
* Work on this calculator began in May, 2024 by Elephant200
* This calculator is intended to bring together many existing functions in one, convenient machine
* "The Elephant Calculator" includes diverse features like geometry formulas, ultra-high precision algorithms, and a CAS
* There is a built-in review system that enables users to give feedback and request new features. All reviews are read carefully, so feel free to write them!

## Calculator Functions ##
1. Vectors and Matrices
	- Supports addition, subtraction, multiplication, exponentiation, determinants, and matrix inversions
   - Uses numpy and normal python
2. High-Precision Calculator
	- Supports square roots, nth roots, exponentiation, *pi* computation, *e* computation, and *sin* computation
   - Uses newton's method to compute square roots and nth roots
   - Uses recursion to compute exponents
   - Uses binary splitting to efficiently compute *pi* and *e*
   - Uses taylor series to compute sine
3. Area
   - Includes formulas for nearly every single 2d shape whose area can be computed.
   - Determines exact values for expressions when applicable.
4. Perimeter
    - Includes formulas for nearly every single 2d shape whose perimeter can be computed.
    - Determines exact values for expressions when applicable
5. Surface Area
    - Includes formulas for nearly every single 3d solid whose surface area can be computed.
    - Determines exact values for expressions when applicable
6. Volume
    - Includes formulas for nearly every single 3d solid whose volume can be computed.
    - Determines exact values for expressions when applicable
7. Triangle Solver
    - Computes the remaining 3 values for a triangle given 3 inputs (3 angles, 3 sides for 6 values)
    - Uses the Law of Sines and the Law of Cosines
8. Pythagorean Triple Generator
    - Can compute both primitive pythagorean triples (includes 3-4-5 but excludes 6-8-10) and all pythagorean triples (includes both 3-4-5 and 6-8-10)
    - Iterates through all possible leg and hypotenuse lengths and determines if the last leg would be an integer
9. Prime Number Generator
    - Can determine if a number is prime, can compute the nth prime, and can compute the first n primes
    - Determines if a number is prime by checking for divisiblity of all integers up to the square root of the number
0. CAS (computer algebra system)
   - Can factor, simplify, and expand expressions. Can solve equations. Can differentiate, integrate, and compute definite integrals
   - Uses the sympy module