# The Elephant Calculator #
## TABLE OF CONTENTS ##
1. Overview
2. Features
3. Calculator Functions Explanations
4. API Endpoints
5. Installation and Setup
6. How to Use
7. Contributing
8. About the Programmer

---

## Overview ##
* Work on this calculator began in May, 2024 by Elephant200.
* This calculator is intended to bring together many existing functions in one, convenient machine.
* "The Elephant Calculator" is a multi-purpose calculator that combines features like:
  - Vector and Matrix Operations
  - Geometry Formulas
  - High-Precision Calculations
  - Pythagorean Triple Generation
  - Prime Number Analysis
  - A built-in Computer Algebra System (CAS)
* Users can also leave reviews and ratings to provide feedback or suggest new features.

---

## Features ##
- **Matrix Operations**: Addition, subtraction, multiplication, exponentiation, determinants, inverses, and transposes.
- **Vector Operations**: Dot product, cross product, scaling, and addition/subtraction.
- **Geometry**: Calculate area, perimeter, volume, and surface area for 2D and 3D shapes.
- **Triangle Solver**: Solve triangles using the Law of Sines and Cosines.
- **Pythagorean Triples**: Generate primitive and non-primitive triples.
- **Prime Number Tools**: Prime checking, nth prime, and prime factorization.
- **High-Precision Calculations**: Square roots, nth roots, pi and e computation, trigonometric functions, and more.
- **CAS**: Factor, simplify, expand expressions, solve equations, derivatives, and integrals.

---

## Calculator Functions ##
1. **Vectors and Matrices**
   - Supports addition, subtraction, multiplication, exponentiation, determinants, and matrix inversions.
   - Uses numpy and normal python.
2. **High-Precision Calculator**
   - Supports square roots, nth roots, exponentiation, *pi* computation, *e* computation, and *sin* computation.
   - Uses Newton's method to compute square roots and nth roots.
   - Uses recursion to compute exponents.
   - Uses binary splitting to efficiently compute *pi* and *e*.
   - Uses Taylor series to compute sine.
3. **Area**
   - Includes formulas for nearly every single 2D shape whose area can be computed.
   - Determines exact values for expressions when applicable.
4. **Perimeter**
    - Includes formulas for nearly every single 2D shape whose perimeter can be computed.
    - Determines exact values for expressions when applicable.
5. **Surface Area**
    - Includes formulas for nearly every single 3D solid whose surface area can be computed.
    - Determines exact values for expressions when applicable.
6. **Volume**
    - Includes formulas for nearly every single 3D solid whose volume can be computed.
    - Determines exact values for expressions when applicable.
7. **Triangle Solver**
    - Computes the remaining 3 values for a triangle given 3 inputs (3 angles, 3 sides for 6 values).
    - Uses the Law of Sines and the Law of Cosines.
8. **Pythagorean Triple Generator**
    - Can compute both primitive Pythagorean triples (e.g., 3-4-5) and all Pythagorean triples (e.g., 6-8-10).
    - Iterates through all possible leg and hypotenuse lengths to find valid triples.
9. **Prime Number Generator**
    - Can determine if a number is prime, compute the nth prime, and generate the first n primes.
    - Checks for divisibility of integers up to the square root of the number.
10. **CAS (Computer Algebra System)**
    - Can factor, simplify, expand expressions, solve equations, compute derivatives, and integrate.
    - Uses the sympy module.

---

## API Endpoints ##
Each endpoint corresponds to a feature in your calculator. The endpoints are grouped by functionality.

### Vectors (`/api/vectors`)
- `POST /add`: Add two vectors.
- `POST /subtract`: Subtract two vectors.
- `POST /dot`: Calculate the dot product of two vectors.
- `POST /cross`: Compute the cross product of two vectors.
- `POST /scale`: Scale a vector by a scalar.

### Matrices (`/api/matrices`)
- `POST /add`: Add two matrices.
- `POST /subtract`: Subtract two matrices.
- `POST /multiply`: Multiply two matrices.
- `POST /vector-multiply`: Multiply a matrix by a vector.
- `POST /scale`: Scale a matrix by a scalar.
- `POST /determinant`: Calculate the determinant of a matrix.
- `POST /inverse`: Compute the inverse of a matrix.
- `POST /transpose`: Compute the transpose of a matrix.
- `POST /exponentiate`: Raise a matrix to a power.

### Geometry (`/api/geometry`)
- `POST /area`: Calculate the area of various 2D shapes.
  - Shapes supported: Circle, rectangle, square, triangle (multiple methods), ellipse, polygon, and more.
- `POST /perimeter`: Calculate the perimeter of various 2D shapes.
  - Shapes supported: Circle, rectangle, square, triangle, polygon, and more.
- `POST /volume`: Calculate the volume of various 3D solids.
  - Solids supported: Cube, sphere, cylinder, cone, ellipsoid, prism, and more.
- `POST /surface-area`: Calculate the surface area of various 3D solids.

### Triangle Solver (`/api/triangles`)
- `POST /solve`: Solve a triangle given sides and/or angles using the Law of Sines or Law of Cosines.

### Pythagorean Triples (`/api/pythagorean`)
- `POST /generate`: Generate all Pythagorean triples up to a maximum hypotenuse.
- `POST /generate-primitive`: Generate primitive Pythagorean triples up to a maximum hypotenuse.

### Prime Numbers (`/api/primes`)
- `POST /is_prime`: Check if a number is prime.
- `POST /nth_prime`: Find the nth prime number.
- `POST /first_primes`: Generate the first n prime numbers.
- `POST /factorization`: Perform prime factorization of a number.

### High-Precision Calculations (`/api/irrationals`)
- `POST /add`: Add two numbers with precision.
- `POST /subtract`: Subtract two numbers with precision.
- `POST /multiply`: Multiply two numbers with precision.
- `POST /divide`: Divide two numbers with precision.
- `POST /sqrt`: Compute the square root of a number with precision.
- `POST /power`: Raise a number to a power with precision.
- `POST /pi`: Compute digits of π with precision.
- `POST /e`: Compute digits of e with precision.
- `POST /sin`: Compute the sine of an angle with precision.
- `POST /cos`: Compute the cosine of an angle with precision.
- `POST /tan`: Compute the tangent of an angle with precision.
- `POST /arcsin`: Compute the arcsine of a value with precision.
- `POST /arccos`: Compute the arccosine of a value with precision.
- `POST /arctan`: Compute the arctangent of a value with precision.

### Computer Algebra System (CAS) (`/api/cas`)
- `POST /factor`: Factor an algebraic expression.
- `POST /expand`: Expand an algebraic expression.
- `POST /simplify`: Simplify an algebraic expression.
- `POST /differentiate`: Compute the derivative of an expression.
- `POST /integrate`: Compute the indefinite integral of an expression.
- `POST /definite-integral`: Compute the definite integral of an expression over a range.
- `POST /solve-equation`: Solve a single-variable equation.
- `POST /solve-multivariable`: Solve a system of equations with multiple variables.
- `POST /solve-differential`: Solve a first-order differential equation.

---

## Installation and Setup ##
### Requirements:
- Python 3.12.5 or later
- pip (Python package manager)

### Steps to Set Up:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Run the setup script:

   ```bash
   ./setup.sh
   ```
   This script will:

   * Set up a virtual environment.
   * Install dependencies.
   * Prepare the folder structure.
   * Create an empty .env file if not already present.
   
   Activate the virtual environment:

   * On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
   
   *On Windows:
   ```cmd
   .venv\Scripts\activate
   ```

   Run the calculator:

   ```bash
   uvicorn api:app --reload
   ```

---

## How to Use

   * Access the API at http://127.0.0.1:8000/docs for interactive API documentation.
   * Integrate the endpoints into your frontend or CLI applications for advanced calculations.

## Contributing

   Contributions are welcome! To contribute:

   1. Fork the repository.
   2. Create a new branch for your changes.
   3. Submit a pull request for review.

## About the Programmer
   Elephant200 began developing this calculator in May 2024 with a vision to create a comprehensive and powerful tool for mathematical operations. The Elephant Calculator reflects a blend of precision, performance, and usability.