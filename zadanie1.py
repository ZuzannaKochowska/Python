import datetime

obecny_rok = datetime.datetime.now().year

imie = input('Podaj swoje imię: ')
rok_urodzenia = int(input('Podaj swój rok urodzenia: '))

def wiek_użytkownika(rok_urodzenia):
    if rok_urodzenia > obecny_rok:
        print("Jeszcze się nie urodziłeś")
        return None
    else:
        return obecny_rok - rok_urodzenia




print("Cześć " + imie)
print("Twój wiek to: ", wiek_użytkownika(rok_urodzenia))

