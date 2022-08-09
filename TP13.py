from ast import Mod
print("-------------------------------------------------------")
print("AÑOS BISIESTOS")
print("-------------------------------------------------------")

print("Ingrese el año:")
año = int(input())

if año % 400 == 0 or año % 4 == 0 and año % 100 != 0:
    print("El año ",año," es bisiesto")
else:
    print("El año ",año," no es bisiesto")