# Solicita el sueldo base y los años de antigüedad al usuario
sueldo = float(input("Ingresa el sueldo base del empleado: "))
años_trabajados = int(input("Ingresa los años de antigüedad del empleado: "))

# Determina el porcentaje de antigüedad según los años trabajados
if años_trabajados < 5:
    porcentaje_antiguedad = 0.30
else:
    porcentaje_antiguedad = 0.50

# Calcula el sueldo a cobrar
sueldo_a_cobrar = sueldo + (sueldo * porcentaje_antiguedad)

# Muestra el sueldo a cobrar
print("El sueldo a cobrar es:", sueldo_a_cobrar)
