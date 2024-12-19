from math import sqrt, pi, sin, cos, acos
import os

elephant = r"""            __     __
           /  \~~~/  \
     ,----(     ..    )
    /      \__     __/
   /|         (\  |(
  ^ \   /___\  /\ |   
     |__|   |__|-"    
"""

clear = lambda : os.system('clear')

def diagram():
    print("""Diagram (not to scale):
        B
        /\\
       /  \\
    c /    \\ a
     /      \\
    /        \\
  A ---------- C
         b""")

def triangle():
    print("""Here is a diagram of the triangle (not to scale):
        B
        /\\
       /  \\
    c /    \\ a
     /      \\
    /        \\
  A ---------- C
         b""")
    type = input("Which congruence theorem would you like to use? (SSS, SAS, AAS, ASA)\n").upper()
    while type not in ["SSS", "SAS", "AAS", "ASA"]:
        type = input("Invalid congruence theorem. Please try again.\nWhich congruence theorem would you like to use? (SSS, SAS, AAS, ASA)\n").upper()
    clear()
    print(elephant)
    diagram()
    eval("" + type + "()")

def SSS():
    a = float(eval(input("a = ")))
    b = float(eval(input("b = ")))
    c = float(eval(input("c = ")))
    clear()
    print(elephant)
    diagram()
    A = round(acos((b*b + c*c - a*a) / (2*b*c)) * 180 / pi, 10)
    B = round(acos((a*a + c*c - b*b) / (2*a*c)) * 180 / pi, 10)
    C = round(acos((a*a + b*b - c*c) / (2*a*b)) * 180 / pi, 10)
    input("A = %s deg\nB = %s deg\nC = %s deg\na = %s\nb = %s\nc = %s\nPress enter to continue." % (A, B, C, a, b, c))
def SAS():
    center = input("Which point will your angle be about? (A, B, C)").upper()
    while center not in list("ABC"): center = input("Invalid point. Please try again.\nWhich point will your angle be about? (A, B, C)").upper()
    if center == "A":
        A = float(eval(input("A = ")))
        b = float(eval(input("b = ")))
        c = float(eval(input("c = ")))
        a = round(sqrt(b*b + c*c - 2*b*c*cos(A / 180 * pi)), 10)
        B = round(acos((a*a + c*c - b*b) / (2*a*c)) * 180 / pi, 10)
        C = round(acos((a*a + b*b - c*c) / (2*a*b)) * 180 / pi, 10)
    elif center == "B":
        B = float(eval(input("B = ")))
        a = float(eval(input("a = ")))
        c = float(eval(input("c = ")))
        b = round(sqrt(a*a + c*c - 2*a*c*cos(B / 180 * pi)), 10)
        A = round(acos((b*b + c*c - a*a) / (2*b*c)) * 180 / pi, 10)
        C = round(acos((a*a + b*b - c*c) / (2*a*b)) * 180 / pi, 10)
    elif center == "C":
        C = float(eval(input("C = ")))
        a = float(eval(input("a = ")))
        b = float(eval(input("b = ")))
        c = round(sqrt(b*b + a*a - 2*b*a*cos(C / 180 * pi)), 10)
        B = round(acos((a*a + c*c - b*b) / (2*a*c)) * 180 / pi, 10)
        A = round(acos((b*b + c*c - a*a) / (2*b*c)) * 180 / pi, 10)
    clear()
    print(elephant)
    diagram()
    input("A = %s\nB = %s\nC = %s\na = %s\nb = %s\nc = %s\nPress enter to continue." % (A, B, C, a, b, c))
def AAS():
    print("Please input 2 of the below angles. ")
    try: 
        A = float(eval(input("A = ")))
        try:
            B = float(eval(input("B = ")))
            C = 180 - A - B
        except:
            C = float(eval(input("C = ")))
            B = 180 - A - C
    except: 
        B = float(eval(input("B = ")))
        C = float(eval(input("C = ")))
        A = 180 - B - C
    center = input("Which side will you input? (a, b, c)").lower()
    while center not in list("abc"): center = input("Invalid point. Please try again.\nWhich point will your angle be about? (a, b, c)").lower()
    if center == "a":
        a = float(eval(input("a = ")))
        b = round(a*sin(B*pi/180)/sin(A*pi/180),10)
        c = round(a*sin(C*pi/180)/sin(A*pi/180),10)
    elif center == "b":
        b = float(eval(input("b = ")))
        a = round(b*sin(A*pi/180)/sin(B*pi/180),10)
        c = round(b*sin(C*pi/180)/sin(B*pi/180),10)
    elif center == "c":
        c = float(eval(input("c = ")))
        a = round(c*sin(A*pi/180)/sin(C*pi/180),10)
        b = round(c*sin(B*pi/180)/sin(C*pi/180),10)
    clear()
    print(elephant)
    diagram()
    input("A = %s\nB = %s\nC = %s\na = %s\nb = %s\nc = %s\nPress enter to continue." % (A, B, C, a, b, c))
            
def ASA():
    AAS()

"""
if input("Is this a right triangle? (y/n)").lower().startswith('y'):
            print(\"\"\"
 A
 |\\
 | \\
 |  \\
b|   \\ c              
 |    \\
 |     \\
 C------B
     a\"\"\")
            self.type = "RIGHT"
            self.a, self.b, self.c, self.A, self.B, self.C = None, None, None, None, None, None
            while self.type not in ["HL", "LL", "AL", "AH"]:
                self.type = input("Which congruence theorem will you be using? (HL, LL, AL, AH) ").upper()
            if self.type == "HL":
                self.a = float(eval(input("a = ")))
                self.c = float(eval(input("c = ")))
            elif self.type == "LL":
                self.a = float(eval(input("a = ")))
                self.b = float(eval(input("b = ")))
            elif self.type == "AL":
                self.A = float(eval(input("A = ")))
                self.a = float(eval(input("a = ")))
            elif self.type == "AH":
                self.A = float(eval(input("A = ")))
                self.c = float(eval(input("c = ")))
            return
"""