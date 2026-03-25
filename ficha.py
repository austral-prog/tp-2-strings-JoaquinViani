def ficha():
    nombre_completo = input()
    email = input()
    nota_1 = int(input())
    nota_2 = int(input())
    nota_3 = int(input())

    nombre_limpio = nombre_completo.strip().title()
    email_limpio = email.lower()

    pos_espacio = nombre_limpio.find(" ")
    nombre = nombre_limpio[:pos_espacio]
    apellido = nombre_limpio[pos_espacio + 1:]

    iniciales = nombre[0] + apellido[0]
    usuario = (apellido + "." + nombre).lower()

    email_valido = "@" in email_limpio
    dominio = email_limpio[email_limpio.find("@") + 1:]

    nombre_archivo = nombre_limpio.replace(" ", "_")
    cantidad_a = nombre_limpio.lower().count("a")
    codigo = nombre_limpio[::-1].upper()

    suma = nota_1 + nota_2 + nota_3
    promedio = suma / 3
    promedio_entero = suma // 3

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")

    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email_limpio}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {email_valido}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_archivo}")
    print(f"Cantidad de a: {cantidad_a}")
    print(f"Codigo secreto: {codigo}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")

    print("=" * 24)
