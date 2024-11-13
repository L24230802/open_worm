suma = 0
contador = 0

for i in range(1, 11):
    valor = float(input(f"Ingresa el valor {i}: "))
    
    if 5 <= valor <= 2500:
        suma += valor  
        contador += 1  

if contador > 0:
    promedio = suma / contador
    print(f"\nEl promedio de los valores entre 5 y 2500 es: {promedio}")
else:
    print("\nNo se ingresaron valores entre 5 y 2500.")
