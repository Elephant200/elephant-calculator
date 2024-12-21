from math import sqrt

def generate(n, printIt=True): # n is the highest hypotenuse allowed
    print("Pythagorean Triples:\n")
    triples = []
    if printIt: print('[', end='')
    for i in range(5, n): # searches every possible hypotenuse length
        for j in range(3, i): # searches every possible leg length
            k = sqrt(i*i - j*j) # calculates other leg length
            if float(int(k)) - k == 0: # checks if other leg length is an integer
                if (j < k): # adds the triple (only once)
                    if len(triples) != 0: print(', ', end='')
                    triples.append((j, int(k), i))
                    if printIt: print("(%s, %s, %s)" % (j, int(k), i), end='')
    if printIt: print("]")
    return triples

def generatePrimitive(n, printIt=True):
    print("Primitive Pythagorean Triples:\n")
    triples = []
    valid = False
    if printIt: print('[', end='')
    for i in range(5, n): # searches every possible hypotenuse length
        for j in range(3, i): # searches every possible leg length
            k = sqrt(i*i - j*j) # calculates other leg length
            if float(int(k)) - k == 0: # checks if other leg length is an integer
                if (j < k): # adds the triple (only once)
                    valid = True
                    for x in range(2,i): 
                        if i % x == 0 and j % x == 0 and k % x == 0: valid = False
                    if len(triples) != 0 and valid: print(', ', end='')
                    if valid: triples.append((j, int(k), i))
                    if printIt and valid: print("(%s, %s, %s)" % (j, int(k), i), end='')
    if printIt: print("]")
    return triples