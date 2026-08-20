peliculas = []


def agregar_pelicula(nombre):
    peliculas.append(nombre)
    print("Pelicula agregada")


def mostrar_peliculas():
    if len(peliculas) == 0:
        print("No hay peliculas guardadas")
    else:
        print("\nMis peliculas:")
        for pelicula in peliculas:
            print("-", pelicula)
