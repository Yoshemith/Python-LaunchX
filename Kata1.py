# Today's date
print("---- Imprime fecha de Hoy ----")
from datetime import date
print("La fecha de Hoy es: " + str(date.today()))
print(" ")
# Unit Converter
print("---- Convierte Parsecs a Años Luz ----")
parsec = input("Ingrese cantidad de Parsecs: ")
lightyears = 3.26156
result = (int(parsec) * float(lightyears))

print(str(parsec) + " parsecs son igual a " + str(result) + " Años Luz")