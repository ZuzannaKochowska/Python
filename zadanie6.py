import random

def get_random_number():
    return random.randint(0, 10)
    
def guess(a):
    while True:
        try:
            b = int(input("Zgadnij liczbę od 0-10: "))
            if b != a and b > a:
                print("Ta liczba jest większa od wylosowanej")
            elif b != a and b < a:
                print("Ta liczba jest mniejsza od wylosowanej")
            else: 
                print("brawo zgadłaś")
                break
        except ValueError:
            print('Wprowadź poprawną liczbę')

a = get_random_number()
guess(a)

