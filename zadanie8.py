

def natural_numbers():
    natural = []
    n = 0

    while n < 5:
        n += 1
        natural.append(n)
    
    reversed_natural = natural[::-1]

    print("Dwie kolumny liczb naturalnych")
    for a, b in zip(natural, reversed_natural):
        print(f"{a:<3} {b:<3}")

natural_numbers()