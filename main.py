import csv

import random
saldo = [0]

clientes = [
    ['Nombre'],
    ['Juan Aguuirres'],
    ['Ana Maria'],
    ['Luis Ector'],
    ['Diego Causa'],
    ['Kevin levin'],
    ['Daniel Mandarina'],
    ['Rocio Andrades'],
    ['Abraham Explocivo'],
    ['Simba Scar'],
    ['Jose Castro'],
    ]

print("Elija una opcion")
print("Opcion 1- Ver saldo De Clientes")
print("Opcion 2- Elejir cliente")
print("Opcion 3- Agregar saldo al clientes")

while True:
    opcion = int(input())
    if opcion == 1:
        print(clientes)
    elif opcion == 2:
        cliente = random.choice(clientes)
        print(cliente)
    elif opcion == 3:
            print("Ingrese el monto a agregar")
            monto = int(input())
            saldo.append(monto)
    else:
        print("Opcion no valida")
        print("Elija una opcion")
        print("Opcion 1- Ver saldo De Clientes")
        print("Opcion 2- Elejir cliente")
        continue
    break


with open('datos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(clientes)
    
print("Archivo CSV 'datos.csv' guardado correctamente")

with open('datos.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    row = list(reader)
    