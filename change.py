def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresa gasto:")
    gasto = int(input ())
    print(gasto)
    print("Dinero recibido:")
    dinero_recibido = input()
    print(dinero_recibido)

    Total = (dinero_recibido - gasto)
    vuelto_pesos = int(Total)
    vuelto_centavos = int((Total - vuelto_pesos)*100)
    print("vuelto\n")
    print(f"pesos:\n{vuelto_pesos}")
    print(f"centavos:\n{vuelto_centavos}")
