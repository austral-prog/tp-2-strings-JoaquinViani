def casting():
    precio = int(input())
    descuento = float(input())
    cantidad = int(input())

    precio_desc = precio * (1 - descuento / 100)
    total = precio_desc * cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_desc}")
    print(f"Total: {total}")

