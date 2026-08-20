def contar_peliculas(lista):
    return len(lista)


def buscar_pelicula(lista, nombre):
    if nombre.lower() in [p.lower() for p in lista]:
        return True
    return False
