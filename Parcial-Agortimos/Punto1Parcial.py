# Desarrollar una función recursiva que permita listar los elementos de vector/lista de
# manera inversa al que están cargados. Preferentemente la función solo debe tener un
# parámetro que es la lista de elementos.

def invertir_lista(lista):
    if len(lista) == 0:
        return

    invertir_lista(lista[1:])
    print(lista[0])


Lista = [1, 2, 3, 4, 5, 6]

print("La lista invertida seria:")
invertir_lista(Lista)
