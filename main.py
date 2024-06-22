import csv

clientes = [
    "Maria Carmen",
    "Eduardo Perez",
    "Felipe Gonzales",
    "Diego Causa",
    "Kevin levin",
    "Daniel Mandarina",
    "Rocio Andrades",
    "Abraham Explocivo",
    "Simba Scar",
    "Jose Antonio",
    ]

with open('datos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(clientes)
    
print("Archivo CSV 'datos.csv' guardado correctamente")

with open('datos.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    row = list(reader)

