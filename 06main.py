import peliculas
import calculos
import mensajes


def menu():
    while True:
        mensajes.bienvenida()

        print("1. Agregar pelicula")
        print("2. Mostrar peliculas")
        print("3. Contar peliculas")
        print("4. Buscar pelicula")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            nombre = input("Nombre de la pelicula: ")
            peliculas.agregar_pelicula(nombre)

        elif opcion == "2":
            peliculas.mostrar_peliculas()

        elif opcion == "3":
            cantidad = calculos.contar_peliculas(peliculas.peliculas)
            print("Tienes", cantidad, "peliculas guardadas")

        elif opcion == "4":
            nombre = input("Pelicula que quieres buscar: ")

            if calculos.buscar_pelicula(peliculas.peliculas, nombre):
                print("La pelicula si esta en la lista")
            else:
                mensajes.no_encontrada()

        elif opcion == "5":
            mensajes.despedida()
            break

        else:
            print("Opcion incorrecta")


if _name_ == "_main_":
    menu()
