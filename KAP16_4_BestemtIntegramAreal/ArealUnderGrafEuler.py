from math import e


def f(x):
    return e**(-(x**2))

a = float(input("Skriv inn startverdi: "))
b = float(input("Skriv inn sluttverdi: "))
n = int(input("Skriv inn antall rektangel: "))

if a > b:
    a, b = b, a

delta_x = (b-a)/n
sum = 0

for i in range(1, n+1):
    sum += f(a+(i-(1/2))*delta_x)*delta_x

print(f"{n} rektangler sin tilnærmingsverdi {sum:.3f}")