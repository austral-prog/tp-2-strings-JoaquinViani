def change():
    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)

    print("Dinero recibido")
    dinero = int(input())
    print(dinero)

    vuelto = dinero - gasto

    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
