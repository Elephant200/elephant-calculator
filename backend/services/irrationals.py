from decimal import getcontext, Decimal
import numpy as np


def add(n1, n2, precision=100):
    getcontext().prec = precision
    return Decimal(n1) + Decimal(n2)


def subtract(n1, n2, precision=100):
    getcontext().prec = precision
    return Decimal(n1) - Decimal(n2)


def multiply(n1, n2, precision=100):
    getcontext().prec = precision
    return Decimal(n1) * Decimal(n2)


def divide(n1, n2, precision=100):
    getcontext().prec = precision
    return Decimal(n1) / Decimal(n2)


def sqrt(num, precision=100):
    getcontext().prec = precision
    num = Decimal(num)
    initial = Decimal(num)
    for i in range(precision + 5):
        initial = Decimal(0.5) * (initial + num / initial)
    return initial


def nRoot(num, root, precision=100):
    getcontext().prec = precision
    num = Decimal(num)
    root = Decimal(root)
    initial = Decimal(num)
    for i in range(precision + 5):
        initial = ((root - 1) / root) * initial + (num / root) / power(
            initial, root - 1, precision)
    return initial


def power(n, p, precision=100):
    getcontext().prec = precision
    if p == 0: return Decimal(1)
    decn = Decimal(n)
    return decn * power(n, p - 1, precision)


def pi(precision=100):
    if precision <= 50: return gauss_legendre(precision)
    return chudnovsky(precision // 8)

def e(precision=100):
    return advancedE(precision)


def gauss_legendre(precision=100):
    getcontext().prec = precision + 10
    a = Decimal(1)
    b = Decimal(1) / sqrt(2, precision + 10)
    t = Decimal(0.25)
    p = Decimal(1)
    for i in range(int(precision / 10) + 10):
        a_next = (a + b) / 2
        b = sqrt(a * b, precision + 10)
        t -= p * (a - a_next) * (a - a_next)
        a = a_next
        p *= 2
    getcontext().prec = precision
    return (a + b) * (a + b) / (Decimal(4) * t)


def binary_split(a, b):
    a = Decimal(a)
    b = Decimal(b)
    if b == a + 1:
        Pab = -(Decimal(6) * a - Decimal(5)) * (
            Decimal(2) * a - Decimal(1)) * (Decimal(6) * a - Decimal(1))
        Qab = Decimal(10939058860032000) * a * a * a
        Rab = Pab * (Decimal(545140134) * a + Decimal(13591409))
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)

        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab


def chudnovsky(n):
    getcontext().prec = n * 8
    P1n, Q1n, R1n = binary_split(1, n)
    return (Decimal(426880) * Decimal(10005).sqrt() *
            Q1n) / (Decimal(13591409) * Q1n + R1n)


def factorial(n, precision=100):
    getcontext().prec = precision + 10
    fac = 1
    if n == Decimal(0): return 1
    for i in range(1, int(n)):
        fac *= i
    return fac


def factorials(n, precision=100):
    getcontext().prec = precision + 10
    facs = [Decimal(1)]
    if n == Decimal(0): return facs
    for i in range(1, int(n)):
        facs.append(facs[i - 1] * (Decimal(i)))
    return facs


def taylorE(precision=100):
    getcontext().prec = precision + 10
    e = 1
    facs = factorials(precision + 10, precision)
    for i in range(1, precision + 10):
        e += Decimal(1) / facs[i]
    getcontext().prec = precision
    return e


def binary_splitE(a, b):
    a = Decimal(a)
    b = Decimal(b)
    if b == a + 1:
        Pab = Decimal(1)
        Qab = b
    else:
        m = (a + b) // 2
        Pam, Qam = binary_splitE(a, m)
        Pmb, Qmb = binary_splitE(m, b)

        Pab = Pam * Qmb + Pmb
        Qab = Qam * Qmb
    return Pab, Qab


def advancedE(n):
    getcontext().prec = n
    P0n, Q0n = binary_splitE(0, n)
    return Decimal(1) + P0n / Q0n


def sin(n, precision=100, rad=True):
    getcontext().prec = precision + 10
    PI = pi(precision + 10)
    if not rad:
        n = (Decimal(n) % Decimal(360)) * PI / Decimal(180)
    n = n % (Decimal(2) * PI)

    epsilon = Decimal(10)**(-precision - 10)
    sin, sign, term, i = Decimal(0), Decimal(1), n, Decimal(1)

    while abs(term) > epsilon:
        sin += sign * term
        sign *= -1
        term *= n * n / (i + 1) / (i + 2)
        i += 2

    getcontext().prec = precision
    return +sin  # Using unary plus to round correctly


def cos(n, precision=100, rad=True):
    getcontext().prec = precision + 10
    PI = pi(precision + 10)
    if not rad:
        n = (Decimal(n) % Decimal(360)) * PI / Decimal(180)
    n = n % (Decimal(2) * PI)

    epsilon = Decimal(10)**(-precision - 10)
    cos, sign, term, i = Decimal(1), Decimal(-1), n*n/Decimal(2), Decimal(2)

    while abs(term) > epsilon:
        cos += sign * term
        sign *= -1
        term *= n * n / (i + 1) / (i + 2)
        i += 2

    getcontext().prec = precision
    return +cos

def tan(n, precision=100, rad=True):
    getcontext().prec = precision + 10
    result = sin(n, precision + 10, rad) / cos(n, precision + 10, rad)
    getcontext().prec = precision
    return +result

def arcsin(n, precision=100, degrees=False):
    getcontext().prec = precision + 10
    if abs(Decimal(n)) > 1:
        return "arcsin input must be between -1 and 1"
    if n == 1:
        result = Decimal(90) if degrees else pi(precision + 10) / Decimal(2)
        getcontext().prec = precision
        return +result
    if n == -1:
        result = Decimal(-90) if degrees else -pi(precision + 10) / Decimal(2)
        getcontext().prec = precision
        return +result
    result = Decimal(n)
    term = Decimal(n)
    epsilon = Decimal(10)**(-precision - 10)
    i = Decimal(1)

    while abs(term) > epsilon:
        term *= (2*i - 1) * (2*i - 1) * Decimal(n) * Decimal(n)
        term /= (2*i) * (2*i + 1)
        result += term / (2*i + 1)
        i += 1

    if degrees:
        result = result * Decimal(180) / pi(precision + 10)
    
    getcontext().prec = precision
    return +result

def arccos(n, precision=100, degrees=False):
    getcontext().prec = precision + 10
    PI = pi(precision + 10)
    result = PI/Decimal(2) - arcsin(n, precision + 10)

    if degrees:
        result = result * Decimal(180) / pi(precision + 10)
    
    getcontext().prec = precision
    return +result

def arctan(n, precision=100, degrees=False):
    getcontext().prec = precision + 10
    x = Decimal(n)
    result = Decimal(0)
    term = x
    epsilon = Decimal(10)**(-precision)
    i = Decimal(1)

    while abs(term) > epsilon:
        result += term
        term *= -x * x
        term /= (2*i + 1)
        i += 1

    if degrees:
        result = result * Decimal(180) / pi(precision + 10)
    
    getcontext().prec = precision
    return +result
