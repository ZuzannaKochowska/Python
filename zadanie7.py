#Catalan number

def catalan_numbers_below_milion():
    C = 1
    n = 0 
    catalans = []
    even_count = 0
    odd_count = 0
    even_count_list = []
    odd_count_list = []

    while C < 10**6:
        C = (4 * n + 2) * C // (n + 2)
        n += 1
        catalans.append(C)

        if C % 2 == 0:
            even_count +=1
            even_count_list.append(C)
        else: 
            odd_count +=1
            odd_count_list.append(C)
    
    
    print("Liczby katalońskie to: ")
    print(catalans, end=",")
    print( )
    print("Parzystych liczb jest: ")
    print(even_count)
    print("Są to liczby: ", even_count_list)
    print("Nieparzystych liczb jest: ")
    print(odd_count)
    print("Są to liczby: ", odd_count_list)

catalan_numbers_below_milion()