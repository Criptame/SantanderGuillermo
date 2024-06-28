
import csv
import random

clientes = [
    ['Nombre',  'Dinero'],
    ['Juan Aguuirres', ],
    ['Ana Maria', ],
    ['Luis Ector',],
    ['Diego Causa', ],
    ['Kevin levin', ],
    ['Daniel Mandarina',],
    ['Rocio Andrades', ],
    ['Abraham Explocivo', ],
    ['Simba Scar',],
    ['Jose Castro',],
]

print("Elija una opcion")
print("Opcion 1- Dar dinero a Clientes con monto alazar")
print("Opcion 2- Ver saldo De Clientes")
print("Opcion 3- Asignar saldo a Todos los clientes")
print("Opcion 4- Hordenar de mayor a menor")
print("Opcion 5- Hordenar de menor a mayor")
print("Opcion 6- Salir del programa")

def generardor_de_saldos_Aleatorios():
    return [random.randint(100, 10000000)]

def Definir_Saldo(saldos):
    saldos = [generardor_de_saldos_Aleatorios() for _ in range(len(clientes)-1)]
    clientes[1][1:] = saldos[0]
    Rango = {"Menor": (1000, 30000), "Regular": (35000, 100000), "Mayor": (150000, 10000000)}
    clasificar = {"Menor": [], "Regular": [], "Mayor": []}
    for saldo in saldos:
        for rango in Rango:
            if Rango[rango][0] <= saldo <= Rango[rango][1]:
                clasificar[rango].append(saldo)
                break
    return clasificar

def Medida_Geometrica(saldos):
    producto = 1
    for saldo in saldos:
        producto *= saldo
    return producto ** (1/len(saldos))

# Asignar Saldo a los Clientes
saldos = [generardor_de_saldos_Aleatorios() for _ in range(len(clientes)-1)]
clientes[1][1:] = saldos[0]

# Ver saldo de los clientes
def ver_saldo_clientes(clientes):
    for cliente in clientes:
        print(f"Nombre: {cliente[0]}, Saldo: ${''.join(map(str, cliente[1:]))}")

def ver_cliente_especifico(clientes, nombre):
    for cliente in clientes:
        if cliente[0] == nombre:
            print(f"Nombre: {cliente[0]}, Saldo: ${''.join(map(str, cliente[1:]))}")
            return

#Generar las opciones

while True:
    opcion = int(input())
    if opcion == 1:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        ver_cliente_especifico(clientes, nombre_cliente)
    elif opcion == 2:
        ver_saldo_clientes(clientes)
    elif opcion == 3:
        saldo_nuevo = int(input("Ingrese el nuevo saldo: "))
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        for cliente in clientes:
            if cliente[0] == nombre_cliente:
                cliente[1:] = [saldo_nuevo]
                print(f"El saldo de {nombre_cliente} se ha actualizado correctamente.")
                break
        else:
            print(f"No se encontró al cliente {nombre_cliente}")
    elif opcion == 4:
        saldos_clasificados = Definir_Saldo(saldos[0])
        print("Clientes por rango de saldo:")
        for rango in saldos_clasificados:
            print(f"{rango}: {len(saldos_clasificados[rango])}")
    elif opcion == 5:
        saldos_clasificados = Definir_Saldo(saldos[0])
        saldos_ordenados = sorted(saldos_clasificados["Menor"] + saldos_clasificados["Regular"] + saldos_clasificados["Mayor"], reverse=True)
        print("Clientes ordenados por saldo (mayor a menor):")
        for saldo in saldos_ordenados:
            for cliente in clientes:
                if cliente[1:] == [saldo]:
                    print(f"Nombre: {cliente[0]}, Saldo: ${''.join(map(str, cliente[1:]))}")
    elif opcion == 6:
        print("Me despido de usted , tenga buen dia")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

# Additional code that is executed only once after the user has chosen their option
def ver_cliente_especifico(clientes, nombre):
    for cliente in clientes:
        if cliente[0] == nombre:
            print(f"Nombre: {cliente[0]}, Saldo: ${''.join(map(str, cliente[1:]))}")
            return
    print(f"No se encontró al cliente {nombre}")

with open('datos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(clientes)

print("Archivo CSV 'datos.csv' guardado correctamente")

with open('datos.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    row = list(reader)