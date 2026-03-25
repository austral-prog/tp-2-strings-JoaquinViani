def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = int(input("Ingresa el precio: "))
    descuento = float(input("Ingresa el descuento: "))
    cantidad = int(input("cantidad de veces: "))

    print(f"\nPrecio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio - descuento}")
    print(f"Total: {(precio - descuento)*3}")
