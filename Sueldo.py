# Solicitar al usuario que ingrese las horas trabajadas
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))

# Establecer la tarifa por hora
tarifa_normal = 100  # tarifa por hora normal
tarifa_extra = 200   # tarifa por hora extra
horas_normales = 8   # horas normales

# Calcular el sueldo
if horas_trabajadas <= horas_normales:
    sueldo = horas_trabajadas * tarifa_normal
else:
    horas_extras = horas_trabajadas - horas_normales
    sueldo = (horas_normales * tarifa_normal) + (horas_extras * tarifa_extra)

# Mostrar el sueldo calculado
print(f"El sueldo correspondiente es: ${sueldo:.2f}")