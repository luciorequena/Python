print("-------------------------------------------------------")
print("OFERTA POR ARTÍCULO")
print("-------------------------------------------------------")

print("Ingrese el costo del artículo: ")
costo = float(input("precio: $"))

print("Ingrese la marca:")
mar = input("marca: ")

if costo>=2000 and mar == "nosy":
    pa=costo*0.90
    pt=pa*0.95

    print("Usted pagara: ",pt," soles")
else:
    if costo<=2000 and mar == "nosy":
        pa=costo*0.95
        pt=pa+pa*0.20

        print("Usted pagara: ",pt," soles")
    else:
        if costo<2000 and mar!="nosy":
            pt=costo*1.20

            print("Usted pagara: ",pt," soles")
