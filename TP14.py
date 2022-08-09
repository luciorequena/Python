print("-------------------------------------------------------")
print("FUNCIÓN")
print("-------------------------------------------------------")

print("Ingrese los valores")
num = int(input("Tipo de calculo: "))
v = int(input("Ingrese V: "))

Funcion = {
1 : 100*v,
2 : 100**v,
3 : 100/v
}

val = Funcion.get(num,0)

print(val)