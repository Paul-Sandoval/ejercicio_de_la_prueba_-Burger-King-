
simple = 1.50
doble = 2.50
triple = 3.25

print("****** BIENVENIDO A BURGER KING ******")
print("Ingrese los datos para la factura electrónica")
print("")
nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su número de cédula: ")
correo = input("Ingrese su correo electrónico: ")

print("Ingrese uno de los siguientes tipos de hamburguesas (solo ingrese el número, no palabras): ")
print("1) sencilla")
print("2) doble")
print("3) triple")

tipo_hamburguesa = input("Ingrese la opción: ").strip()

match tipo_hamburguesa:
    case '1':
        precio_hamburguesa = simple
        nombre_hamburguesa = "sencilla"
    case '2':
        precio_hamburguesa = doble
        nombre_hamburguesa = "doble"
    case '3':
        precio_hamburguesa = triple
        nombre_hamburguesa = "triple"
    case _:
        print("Tipo de hamburguesa no existente.")
        exit()

cantidad = int(input("Ingrese la cantidad de hamburguesas que va a adquirir: "))
print("Ingrese su forma de pago")
print("1) Tarjeta de crédito")
print("2) Efectivo")

forma_pago = input("Ingrese la opción: ").strip()
match forma_pago:
    case '1':
        recargo = 0.05
        metodo_pago = "tarjeta de crédito"
    case '2':
        recargo = 0.00
        metodo_pago = "efectivo"
    case _:
        print("Tipo de pago no existente.")
        exit()
        
costo_base = precio_hamburguesa * cantidad
costo_final = costo_base * (1 + recargo)
print()
print("****** FACTURA ******")
print(f"Nombre: {nombre}")
print(f"Cédula: {cedula}")
print(f"Correo: {correo}")
print(f"Hamburguesas adquiridas: {cantidad} ({nombre_hamburguesa})")
print(f"Forma de pago: {metodo_pago}")
print(f"Precio final: ${costo_final:.2f}")
print("La factura electronica se enviará a su correo.")
print(f"Muchas gracias por preferirnos, {nombre}.")
