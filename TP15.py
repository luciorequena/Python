print("-------------------------------------------------------")
print("POR O IMPAR")
print("-------------------------------------------------------")

print("Ingrese un número entre 0 y 10")
num = int(input())

if num<0 or num>10:
    print("Escriba un nùmero entre 0 y 10.")
else:
    if num<=10 and num % 2 != 0:
        print("El número es impar.")
    else:
        if num<=10 and num % 2 == 0:
            print("El número es par.")