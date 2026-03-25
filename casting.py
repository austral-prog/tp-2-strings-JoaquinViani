def casting():
    precio = int(input())
    descuento = float(input())
    cantidad = int(input())

    precio_desc = round(precio - (precio * descuento / 100), 1)
    total = round(precio_desc * cantidad, 1)

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_desc}")
    print(f"Total: {total}")
