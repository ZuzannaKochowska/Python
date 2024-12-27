#Catalan number

def catalan_numbers_below_milion():
    C = 1
    n = 0 
    catalans = []
    even_count = 0
    odd_count = 0

    while C < 10**6:
        catalans.append(C)
        if C % 2 == 0:
            even_count +=1
        else: 
            odd_count +=1
    
    C = (4 * n + 2) * C // (n + 2)
    n += 1

    print("Liczby katalońskie to: ")
    print(catalans)
    print("Parzystych liczb jest: ")
    print(even_count)
    print("Nieparzystych liczb jest: ")
    print(odd_count)

catalan_numbers_below_milion()