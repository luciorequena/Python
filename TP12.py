print("-------------------------------------------------------")
print("AUMENTO DE SUELDO")
print("-------------------------------------------------------")

print("Ingrese su sueldo:")
suel = float(input("$"))


if suel<1000:
    aument = suel*0.15
    suel = suel+aument

    print("Sueldo nuevo: $",suel)
else:
    print("los sueldos iguales o mayores a 1000 no reciben un aumento.")

