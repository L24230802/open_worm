suma = 0

for i in range(1, 11):
    valor = float(input(f"Ingresa el valor {i}: "))
    suma += valor  # Acumula el valor ingresado

promedio = suma / 10

print(f"\nLa suma de los 10 valores es: {suma}")
print(f"El promedio de los 10 valores es: {promedio}")
