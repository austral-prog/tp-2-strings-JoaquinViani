def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre_completo = input("Ingresa su nombre y apellido: ")
    email = input("Ingresa su email: ")
    nota_1 = int(input ("Ingresa tu primera nota: "))
    nota_2 = int(input ("Ingresa tu segunda nota: "))
    nota_3 = int(input ("Ingresa tu tercera nota: "))
    nombre_limpio = nombre_completo.strip().title()
    pos_espacio = nombre_limpio.find(" ")
    iniciales = nombre_limpio[0] + nombre_limpio[pos_espacio + 1]
    nombre_limpio = nombre_completo.strip().title()
    nombre = nombre_limpio[:pos_espacio]
    apellido = nombre_limpio[pos_espacio + 1:]
    usuario = (apellido + "." + nombre).lower()
    email_limpio = email.lower()
    email_valido = "@" in email_limpio
    pos_arroba = email_limpio.find("@")
    dominio = email_limpio[pos_arroba + 1:]
    nombre_archivo = nombre_limpio.replace(" ", "_")
    cantidad_a = nombre_limpio.lower().count("a")
    codigo = nombre_limpio[::-1].upper()
    suma = nota_1 + nota_2 + nota_3
    promedio = suma / 3
    promedio_entero = suma // 3

    
    print("======================== \n  FICHA DEL ALUMNO\n========================")


    print (f"Nombre: {nombre_completo.title()}")
    print (f"Email: {email.lower()}")
    print (f"Cantidad de caracteres: {len(nombre_completo)}")
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

