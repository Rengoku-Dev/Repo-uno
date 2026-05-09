# Algoritmo para sumar 2 números distintos de 0

num1 = int(input("Ingrese el primer : "))
num2 = int(input("Ingrese el segundo : "))

if num1 != 0 and num2 != 0:
    suma = num1 + num2
    print("La suma es:", suma)
else:
    print("Los números no deben ser 0")