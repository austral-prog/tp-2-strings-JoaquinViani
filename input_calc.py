def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base = int(input("Base: "))
    altura = int(input("Altura: "))

    Area = base * altura
    perimetro = base * 2 + altura*2

    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {Area}")
    print(f"Perimetro: {perimetro}")
