import math

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Proszę podać prawidłową liczbę całkowitą.")

def combining(first_number, second_number):
    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number
    try:
        division = first_number/second_number
    except ZeroDivisionError:
        division = "Nie można dzielić przez 0."
    
    square_root = math.sqrt(first_number+second_number)
    exponentiation1 = first_number ** second_number
    exponentiation2 = second_number ** first_number

    print('Wynik dodawania to: ',addition)
    print('Wynik odejmowania to: ', subtraction)
    print('Wynik mnożenia to: ', multiplication)
    print('Wynik dzielenia to: ', division)
    print('Wynik pierwiastkowania to: ', square_root)
    print(' Potęgowanie : ', exponentiation1, 'oraz', exponentiation2)

def main():
    first_number = get_number('Podaj pierwszą liczbę: ')
    second_number = get_number('Podaj drugą liczbę: ')
    combining(first_number, second_number)

if __name__ == "__main__":
    main()