import math

def get_coordinate(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Proszę podać prawidłowe współrzędne.")

def input_coordinate():
    xx = float(get_coordinate('Podaj pierwszą współrzędną kartezjańską: '))
    yy = float(get_coordinate('Podaj drugą współrzędną kartezjańską: '))
    zz = float(get_coordinate('Podaj trzecią współrzędną kartezjańską: '))
    return xx, yy, zz



def transform_coordinate(xx, yy, zz):
    rr = math.sqrt((xx**2)+(yy**2))
    phi = math.atan2(yy, xx) 
    ro = math.sqrt((xx**2) + (yy**2) + (zz**2))
    psi = math.asin(zz/ro)
    return rr, phi, ro, psi

xx, yy, zz = input_coordinate()
rr, phi, ro, psi = transform_coordinate(xx, yy, zz)

print('Współrzędne cylindryczne to:')
print("r: ", rr, "radiany: ", phi , "z: ", zz, "ro: ", ro, "psi: ", psi )

print(f"r: {rr:.2f} phi: {phi:.2f} z: {zz:.2f} ro: {ro:.2f} psi: {psi:.2f}")







