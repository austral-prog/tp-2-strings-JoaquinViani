def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"

    primero_3_caracteres = print(texto.lower()[0:3])
    posicion_2_al_4 = print(texto.lower()[2:5])
    completo = print(texto.lower()[0:])

