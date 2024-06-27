
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
print("Opcion 1- Ver saldo De Clientes")
print("Opcion 2- Ver a un cliente cliente")
print("Opcion 3- Agregar saldo al clientes")
print("Opcion 4- Modicar lista Vase a saldo")
print("Opcion 5- Salir del programa")

def generardor_de_saldos_Aleatorios():
    return [random.randint(100, 10000000)]

def Definir_Saldo(saldos):
    Rango = {"Menor": (1000, 30000), "Regular": (35000, 100000), "Mayor": (150000, 10000000)}
    clasificar = {"Menor": [], "Regular": [], "Mayor": []}

with open('datos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(clientes)
    
print("Archivo CSV 'datos.csv' guardado correctamente")

with open('datos.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    row = list(reader)
    