import csv

import random
saldo = [0]

clientes = [
    ['Nombre',  'Dinero'],
    ['Juan Aguuirres', '10000'],
    ['Ana Maria',  '10000'],
    ['Luis Ector',  '5000'],
    ['Diego Causa',  '9000'],
    ['Kevin levin',  '20000'],
    ['Daniel Mandarina',  '2000'],
    ['Rocio Andrades',  '30000'],
    ['Abraham Explocivo',  '5000'],
    ['Simba Scar',  '10000'],
    ['Jose Castro',  '30000'],
    ]

print("Elija una opcion")
print("Opcion 1- Ver saldo De Clientes")
print("Opcion 2- Elejir cliente")
print("Opcion 3- Agregar saldo al clientes")
print("Opcion 4- Modicar lista Vase a saldo")
print("Opcion 5- Salir del programa")

while True:
    opcion = int(input())
    if opcion == 1:
        print(clientes)
    elif opcion == 2:
        cliente = random.choice(clientes)
        print(cliente)
    elif opcion == 3:
            print("Ingrese al cliente")
            selecion_cliente = int(input())
            print("Ingrese el monto a agregar")
            monto = int(input())
            saldo.append(monto)
            print("Haora {selecion_cliente} tiene {monto} en su cuenta")
    elif opcion == 4:
        print("Ingrese el indice del cliente a modificar")
        indice = int(input())
        print("Ingrese el nuevo saldo")
        monto = int(input())
        saldo[indice] = monto
        print("Saldo modificado correctamente")
    elif opcion == 5:
        print("Gracias por usar nuestro programa")
        break
    else:
        print("Opcion no valida")
        print("Elija una opcion")
        print("Opcion 1- Ver saldo De Clientes")
        print("Opcion 2- Elejir cliente")
        print("Opcion 3- Agregar saldo al clientes")
        print("Opcion 4- Modicar lista Vase a saldo")
        print("Opcion 5- Salir del programa")
        continue
    break


with open('datos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(clientes)
    
print("Archivo CSV 'datos.csv' guardado correctamente")

with open('datos.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    row = list(reader)
    