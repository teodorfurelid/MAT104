def f(x):
    return (-x**2)-x-12

a = float(input("Skriv inn startverdi: "))
b = float(input("Skriv inn sluttverdi: "))
n = int(input("Skriv inn antall rektangel: "))

delta_x = (b-a)/n
sum = 0

for i in range (1, n+1):
    sum += f(a+(i-1)*delta_x)*delta_x

print(f"{n} rektangler gir tilnærmingsverdi {sum:.3f}")