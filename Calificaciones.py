# Solicitar al usuario que ingrese tres calificaciones
calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))

# Calcular el promedio
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

# Mostrar el promedio
print(f"El promedio de las calificaciones es: {promedio:.2f}")