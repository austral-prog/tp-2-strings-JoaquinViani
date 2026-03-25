def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre = input("Ingresa su nombre: ")
    nombre_minuscula = nombre.lower()

    A = ("a" in nombre_minuscula)
    E = ("e" in nombre_minuscula)
    I = ("i" in nombre_minuscula)
    O = ("o" in nombre_minuscula)
    U = ("u" in nombre_minuscula)

    print (f"Contiene a: {A}")
    print (f"Contiene a: {E}")
    print (f"Contiene a: {I}")
    print (f"Contiene a: {O}")
    print (f"Contiene a: {U}")
