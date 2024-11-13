
Cal1 = float(input("Ingresa la primera calificación: "))
Cal2 = float(input("Ingresa la segunda calificación: "))
Cal3 = float(input("Ingresa la tercera calificación: "))

promedio = (Cal1 + Cal2 + Cal3) / 3

if promedio >= 7:
    print("Aprobaste el trimestre con un promedio de:", promedio)
else:
    print("Debes recuperar. Tu promedio fue de:", promedio)
