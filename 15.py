contador_menor_10 = 0
contador_entre_10_y_100 = 0
contador_mayor_100 = 0
contador_negativo = 0
contador_igual_a_0 = 0

for i in range(1, 101):
    valor = float(input(f"Ingresa el valor {i}: "))
    
    if 0 < valor < 10:
        contador_menor_10 += 1
    elif 10 <= valor <= 100:
        contador_entre_10_y_100 += 1
    elif valor > 100:
        contador_mayor_100 += 1
    elif valor < 0:
        contador_negativo += 1
    elif valor == 0:
        contador_igual_a_0 += 1

print(f"\nValores mayor a 0 y menor a 10: {contador_menor_10}")
print(f"Valores entre 10 y 100 (inclusive): {contador_entre_10_y_100}")
print(f"Valores mayores a 100: {contador_mayor_100}")
print(f"Valores negativos: {contador_negativo}")
print(f"Valores iguales a 0: {contador_igual_a_0}")
