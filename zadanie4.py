import math

def get_calc(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0 :
             return value
            else:
                print("Wprowadź liczbę większą od zera.")
        except ValueError:
            print("Wprowadź poprawną liczbę")
        

def circle_calc():
    radius = get_calc('Wprowadź promień koła: ')
    circumference = math.pi * radius * 2
    area = math.pi * (radius**2)
    return radius, circumference, area

radius, circumference, area = circle_calc()

print("Obwód koła to:", circumference, "Pole koła to: " , area)
    
