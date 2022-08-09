print("-------------------------------------------------------")
print("Calificación")
print("-------------------------------------------------------")

print("Ingrese la calificación del alumno")
calif = float(input())

if calif > 10 or calif == 10:
    print("Alumno aprobado.")
else:
    if calif < 10:
        print("Alumno desaprobado.")
