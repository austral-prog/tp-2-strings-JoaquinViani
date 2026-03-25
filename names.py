def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    
    Nombre = input("Ingresa su nombre: ")
    Apellido = input("Ingresa su apellido: ")

    print(f"{Nombre.lower()} {Apellido.lower()}") 
    print(f"{Nombre.title()} {Apellido.title()}") 
    print(f"{Nombre.upper()} {Apellido.upper()}") 
    print(f"    {Nombre.lower()} {Apellido.lower()}") 
