import math

#====================AREA FORMULAS================================
class Area:
    def area(type):
        if type.lower().startswith('cir'):
            return Area.circleA(float(input("radius = ")))
        if type.lower().startswith('sem'):
            return Area.semiA(float(input("radius = ")))
        elif type.lower().startswith('ell'):
            return Area.ellipseA(float(input('semi-major axis = ')), float(input('semi-minor axis = ')))
        elif type.lower().startswith('rec'):
            return Area.rectangleA(float(input('length = ')), float(input('width = ')))
        elif type.lower().startswith('squ'):
            return Area.squareA(float(input('Side length = ')))
        elif type.lower().startswith('par'):
            return round(Area.parallelogramA(float(input("Side 1 = ")), float(input("Side 2 = ")), float(input("theta (degrees) = "))),10)
        elif type.lower().startswith('rho'):
            return Area.rhombusA(float(input("Diagonal 1 = ")), float(input("Diagonal 2 = ")))
        elif type.lower().startswith('kit'):
            return Area.rhombusA(float(input("Diagonal 1 = ")), float(input("Diagona 2 = ")))
        elif type.lower().startswith('tri'):
            return Area.triangleA()
        elif type.lower().startswith('tra'):
            return Area.trapezoidA(float(input("Longer base = ")), float(input("Shorter base = ")), float(input("Height = ")))
        elif type.lower().startswith('pol'):
            return Area.polygon(float(input("Number of sides = ")), float(input("Side = ")))
        elif type.lower().startswith('pen'):
            return Area.pentagonA(float(input("Side = ")))
        elif type.lower().startswith('hex'):
            return Area.hexagonA(float(input("Side = ")))
        elif type.lower().startswith('hep'):
            return Area.polygon(7, float(input("Side = ")))
        elif type.lower().startswith('oct'):
            return Area.octagonA(float(input("Side = ")))
        elif type.lower().startswith('non'):
            return Area.polygon(9, float(input("Side = ")))
        elif type.lower().startswith('dec'):
            return Area.polygon(10, float(input("Side = ")))
        else:
            return "That is an unsupported shape. Please try again. "

    def circleA(radius):
        return str(math.pi * radius * radius) + "\nExact: " + str(radius * radius) + "pi"
    def semiA(r):
        return str(math.pi * r * r/2) + "\nExact: " + (str(round(1/2*r*r)) if (r*r)%2==0 else str(round(r*r))+'/2') + "pi"
    def ellipseA(a, b):
        return str(math.pi * a * b) + " = " + str(a * b) + "pi"
    def squareA(side):
        return side * side
    def rectangleA(l, w):
        return l * w
    def parallelogramA(s1, s2, theta):
        return s1 * s2 * round(math.sin(theta * math.pi / 180),10)
    def rhombusA(d1, d2):
        return d1 * d2 / 2
    def trapezoidA(b1, b2, h):
        return (b1 + b2) * h / 2
    def pentagonA(s):
        return 0.25 * math.sqrt(25 + 10 * math.sqrt(5)) * s * s
    def hexagonA(s):
        return 1.5 * math.sqrt(3) * s * s
    def octagon(s):
        return (2 + 2 * math.sqrt(2)) * s * s
    def polygon(sides, s):
        match sides:
            case 3: return Area.herons(s, s, s)
            case 4: return Area.squareA(s)
            case 5: return Area.pentagonA(s)
            case 6: return Area.hexagonA(s)
            case 8: return Area.octagon(s)
            case _: return sides / 4 * 1/(math.tan(math.pi/sides)) * s * s
    def herons(s1, s2, s3):
        s = (s1 + s2 + s3) / 2
        return math.sqrt(s * (s-s1) * (s-s2) * (s-s3))
    def triangleA():
        method = input("You may either input\n1. 3 sides\n2. 2 sides and the included angle\n3. Base and height\n")
        if method.lower().startswith('1'):
            return round(Area.herons(float(input("Side 1 = ")), float(input("Side 2 = ")), float(input("Side 3 = "))), 10)
        elif method.lower().startswith('2'):
            return round(0.5 * float(input("Side 1 = ")) * float(input("Side 2 = ")) * math.sin(float(input("Included angle = ")) * math.pi / 180), 10)
        elif method.lower().startswith('3'):
            return 0.5 * float(input("Side 1 = ")) * float(input("Side 2 = "))
        else:
            return "Invalid input"   
    
#====================PERIMETER FORMULAS===========================
class Perimeter:
    def perimeter(type):
        if type.startswith('cir'):
            radius = float(input("Radius = "))
            return str(2*math.pi*radius) + "\nExact: " + str(2 * radius) + "pi"
        elif type.startswith('rec'):
            return 2*float(input("Length = ")) + 2*float(input("Width = "))
        elif type.startswith('squ'):
            return 4*float(input("Side = "))
        elif type.startswith('par'):
            return 2*float(input("Length = ")) + 2*float(input("Width = "))
        elif type.startswith('rho'):
            return 4*float(input("Side = "))
        elif type.startswith('kit'):
            return 2*float(input("Side 1 = ")) + 2*float(input("Side = 2"))
        elif type.startswith('tri'):
            return float(input("Side 1 = ")) + float(input("Side 2 = ")) + float(input("Side 3 = "))
        elif type.startswith('tra'):
            return float(input("Longer base = ")) + float(input("Shorter base = ")) + float(input("Left side = ")) + float(input("Right side = "))
        elif type.startswith('pol'):
            return sum([float(input("Side %s = " % (i+1))) for i in range(int(input("# sides: ")))])
        elif type.startswith('pen'):
            return sum([float(input("Side %s = " % (i+1))) for i in range(5)])
        elif type.startswith('hex'):
            return sum([float(input("Side %s = " % (i+1))) for i in range(6)])
        elif type.startswith('hep'):
            return sum([float(input("Side %s = " % (i+1))) for i in range(7)])
        elif type.startswith('oct'):
            return sum([float(input("Side %s = " % (i+1))) for i in range(8)])
        elif type.startswith('non'):
            return sum([float(input("Side %s = " % (i+1))) for i in range(9)])
        elif type.startswith('dec'):
            return sum([float(input("Side %s = " % (i+1))) for i in range(10)])
        else:
            return "This is an unsupported shape. Please try again. "

#====================VOLUME FORMULAS==============================
class Volume:
    def vol(type):
        if type.startswith('cub'):
            return float(input("side = "))**3
        elif type.startswith('rec'):
            return float(input("Length = "))*float(input("Width = "))*float(input("Height = "))
        elif type.startswith('cyl'):
            r, h = float(input("Radius = ")), float(input("Height = "))
            return f"{math.pi*r*r*h}\nExact:{round(r*r*h)}pi"
        elif type.startswith('con'):
            r, h = float(eval(input("Radius = "))), float(input("Height = "))
            return f"{1/3*math.pi*r*r*h}\nExact: {round(1/3*r*r*h) if (r*r*h)%3==0 else str(round(r*r*h))+'/3'}pi"
        elif type.startswith('sph'):
            r = float(eval(input("Radius = ")))
            return f"{4/3*math.pi*r**3}\nExact: {round(4/3*r**3) if r%3==0 else str(round(4*r**3))+'/3'}pi"
        elif type.startswith('ell'):
            a,b,c = float(input("a = ")),float(input("b = ")),float(input("c = "))
            return f"{4/3*math.pi*a*b*c}\nExact: {round(4/3*a*b*c) if (a*b*c)%3==0 else str(round(4*a*b*c))+'/3'}pi"
        elif type.startswith('hem'):
            r = float(eval(input("Radius = ")))
            return f"{2/3*math.pi*r**3}\nExact: {round(2/3*r**3) if r%3==0 else str(round(2*r**3))+'/3'}pi"
        elif type.startswith('pyr'):
            sides = int(input("How many sides does the regular polygon at the base of this pyramid have? "))
            if sides < 2: return "That is an unsupported polygon. Please try again."
            elif sides == 3: B = Area.herons(float(input("Side 1 = ")), float(input("Side 2 = ")), float(input("Side 3 = ")))
            else: B = Area.polygon(sides, float(input("Base side = ")))
            h = float(input("Height = "))
            return round(B*h/3) if (B*h)%3==0 else (f"{round(B*h/3,10)}\nExact: {round(B*h)}/3" if (B*h*3)%3==0 else round(B*h/3,10))
        elif type.startswith('pri'):
            sides = int(input("How many sides does the polygon at the base of this prism have? "))
            if sides < 2: return "That is an unsupported polygon. Please try again."
            elif sides == 3: B = Area.herons(float(input("Side 1 = ")), float(input("Side 2 = ")), float(input("Side 3 = ")))
            elif sides == 4: B = Area.rectangleA(float(input("Length = ")), float(input("Width = ")))
            else: B = Area.polygon(sides, float(input("Base side = ")))
            h = float(input("Height = "))
            return B*h
        elif type.startswith('tet'):
            side = float(eval(input("Side = ")))
            return side**3/(6 * math.sqrt(2))
        elif type.startswith('oct'):
            side = float(eval(input("Side = ")))
            return side**3*math.sqrt(2)/3
        elif type.startswith('dod'):
            side = float(eval(input("Side = ")))
            return (15 + 7*math.sqrt(5)) * side**3 / 4
        elif type.startswith('ico'):
            side = float(eval(input("Side = ")))
            return (15 + 5*math.sqrt(5)) * side**3 / 12
        else:
            return "That is an unsupported solid. Please try again."
#====================SURFACE AREA FORMULAS========================
class SurfaceArea:
    def sa(type):
        if type.startswith('cub'):
            return 6*float(input("Side = "))**2
        elif type.startswith('rec'):
            l, w, h = float(input("Length = ")), float(input("Width = ")), float(input("Height = "))
            return 2*l*w + 2*l*h + 2*w*h
        elif type.startswith('cyl'):
            r, h = float(input("Radius = ")), float(input("Height = "))
            return f"{2*math.pi*r*r+2*math.pi*r*h}\nExact: {2*r*(r+h)}pi" if 2*r*(r+h)%1==0 else 2*math.pi*r*r+2*math.pi*r*h
        elif type.startswith('con'):
            r, h = float(input("Radius = ")), float(input("Height = "))
            l = math.sqrt(r**2+h**2)
            return f"{math.pi*r*(r+l)}\nExact: {r*(r+l)}pi" if r*(r+l)%1==0 else math.pi*r*(r+l)
        elif type.startswith('sph'):
            r = float(input("Radius = "))
            return f"{4*math.pi*r*r}\nExact: {4*r*r}pi"
        elif type.startswith('hem'):
            r = float(input("Radius = "))
            return f"{3*math.pi*r*r}\nExact: {3*r*r}pi"
        elif type.startswith('pyr'):
            sides = int(input("How many sides does the regular polygon at the base of this pyramid have? "))
            side = float(input("Base side = "))
            h = float(eval(input("Height: ")))
            return 0.5*sides*side*math.sqrt(0.25*side**2+h**2) + Area.polygon(sides, side)
        elif type.startswith('pri'):
            sides = int(input("# sides: "))
            sideLength = float(input("Side = "))
            height = float(input("Height = "))
            return 2 * Area.polygon(sides, sideLength) + sides * sideLength * height
        elif type.startswith('tet'):
            return math.sqrt(3) * float(input("Side = "))**2
        elif type.startswith('oct'):
            return 2 * math.sqrt(3) * float(input("Side = "))**2
        elif type.startswith('dod'):
            return 12 * Area.polygon(5, float(input("Side = ")))
        elif type.startswith('ico'):
            return 5 * math.sqrt(3) * float(input("Side = "))**2
        else:
            return "That is an unsupported solid. Please try again."