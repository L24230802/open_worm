total_alumnos = 24

for i in range(1, total_alumnos + 1):
    print(f"\nAlumno {i}")
    apellido = input("Ingresa el apellido del alumno: ")
    nombre = input("Ingresa el nombre del alumno: ")
    nota = float(input("Ingresa la nota del examen: "))
    
    print(f"\nAlumno {i}: {apellido} {nombre}, Nota: {nota}")
