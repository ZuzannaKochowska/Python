# delta

import math

def assumptions():
    a = float(input("Wprowadź współczynnik a: "))
    b = float(input("Wprowadź współczynnik b: "))
    c = float(input("Wprowadź współczynnik c: "))
    return a, b, c 

def scores_x1_x2_x(a,b,c):
    delta = ((b**2) - (4*a*c))
    if delta > 0:
        x1 = ((-b)-math.sqrt(delta))/(2*a)
        x2 = ((-b)+math.sqrt(delta))/(2*a)
        print("x1= ",x1 ,"x2= ",x2)
        return x1, x2,
    elif delta == 0:
         x = (-b/(2*a))
         print("x={x}")
         return x,
    else:
        print("brak rozwiązań")
        return None

a, b, c = assumptions()

roots = scores_x1_x2_x(a, b, c)

if roots is not None:
    if len(roots) == 1:
        print(f"Jedno rozwiązanie: x = {roots[0]:.2f}")
    elif len(roots) == 2:
        print(f"Dwa rozwiązania: x1 = {roots[0]:.2f}, x2 = {roots[1]:.2f}")

