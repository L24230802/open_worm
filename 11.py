for i in range(1, 11):
    print(f"\nIntento {i}:")
    numero = float(input("Ingresa un valor: "))

    if numero < 10:
        print("El número es menor que 10.")
    elif 10 <= numero <= 100:
        print("El número está entre 10 y 100.")
    else:
        print("El número es mayor a 100.")
