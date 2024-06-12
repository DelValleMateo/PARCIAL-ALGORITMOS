# parámetro que es la lista de elementos. 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
# a) Contar cuantas especies hay;
# b) Determinar cuantos descubridores distintos hay;
# c) Mostrar todos los dinosaurios que empiecen con T;
# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;


dinosaurios = [
    {
        "nombre": "Tyrannosaurus Rex",
        "especie": "Theropoda",
        "peso": "7000 kg",
        "descubridor": "Barnum Brown",
        "ano_descubrimiento": 1902
    },
    {
        "nombre": "Triceratops",
        "especie": "Ceratopsidae",
        "peso": "6000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1889
    },
    {
        "nombre": "Velociraptor",
        "especie": "Dromaeosauridae",
        "peso": "15 kg",
        "descubridor": "Henry Fairfield Osborn",
        "ano_descubrimiento": 1924
    },
    {
        "nombre": "Brachiosaurus",
        "especie": "Sauropoda",
        "peso": "56000 kg",
        "descubridor": "Elmer S. Riggs",
        "ano_descubrimiento": 1903
    },
    {
        "nombre": "Stegosaurus",
        "especie": "Stegosauridae",
        "peso": "5000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Spinosaurus",
        "especie": "Spinosauridae",
        "peso": "10000 kg",
        "descubridor": "Ernst Stromer",
        "ano_descubrimiento": 1912
    },
    {
        "nombre": "Allosaurus",
        "especie": "Theropoda",
        "peso": "2000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Apatosaurus",
        "especie": "Sauropoda",
        "peso": "23000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Diplodocus",
        "especie": "Sauropoda",
        "peso": "15000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1878
    },
    {
        "nombre": "Ankylosaurus",
        "especie": "Ankylosauridae",
        "peso": "6000 kg",
        "descubridor": "Barnum Brown",
        "ano_descubrimiento": 1908
    },
    {
        "nombre": "Parasaurolophus",
        "especie": "Hadrosauridae",
        "peso": "2500 kg",
        "descubridor": "William Parks",
        "ano_descubrimiento": 1922
    },
    {
        "nombre": "Carnotaurus",
        "especie": "Theropoda",
        "peso": "1500 kg",
        "descubridor": "José Bonaparte",
        "ano_descubrimiento": 1985
    },
    {
        "nombre": "Styracosaurus",
        "especie": "Ceratopsidae",
        "peso": "2700 kg",
        "descubridor": "Lawrence Lambe",
        "ano_descubrimiento": 1913
    },
    {
        "nombre": "Therizinosaurus",
        "especie": "Therizinosauridae",
        "peso": "5000 kg",
        "descubridor": "Evgeny Maleev",
        "ano_descubrimiento": 1954
    },
    {
        "nombre": "Pteranodon",
        "especie": "Pterosauria",
        "peso": "25 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1876
    },
    {
        "nombre": "Quetzalcoatlus",
        "especie": "Pterosauria",
        "peso": "200 kg",
        "descubridor": "Douglas A. Lawson",
        "ano_descubrimiento": 1971
    },
    {
        "nombre": "Plesiosaurus",
        "especie": "Plesiosauria",
        "peso": "450 kg",
        "descubridor": "Mary Anning",
        "ano_descubrimiento": 1824
    },
    {
        "nombre": "Mosasaurus",
        "especie": "Mosasauridae",
        "peso": "15000 kg",
        "descubridor": "William Conybeare",
        "ano_descubrimiento": 1829
    },

]


class Stack:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamaño(self):
        return len(self.items)


# a) Contar cuantas especies hay;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO A")
print(" ")


def cantidad_especies(dinosaurios):
    especies_unicas = Stack()
    for dino in dinosaurios:
        especie = dino["especie"]
        if not existe(especies_unicas, especie):
            especies_unicas.apilar(especie)
    return especies_unicas.tamaño()


def existe(pila, elemento):
    encontrado = False
    pila_aux = Stack()
    while not pila.esta_vacia():
        item = pila.desapilar()
        pila_aux.apilar(item)
        if item == elemento:
            encontrado = True
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    return encontrado


numero_especies = cantidad_especies(dinosaurios)
print(f"Cantidad de especies: {numero_especies}")


# b) Determinar cuantos descubridores distintos hay;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO B")
print(" ")


def cantidad_descubridores(dinosaurios):
    descubridores_unicos = Stack()
    for dino in dinosaurios:
        descubridor = dino["descubridor"]
        if not existe(descubridores_unicos, descubridor):
            descubridores_unicos.apilar(descubridor)
    return descubridores_unicos.tamaño()


num_descubridores = cantidad_descubridores(dinosaurios)
print(f"Número de descubridores distintos: {num_descubridores}")


# c) Mostrar todos los dinosaurios que empiecen con T;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO C")
print(" ")


def dinosaurios_con_T(dinosaurios):
    dinosaurios_T = Stack()

    for dino in dinosaurios:
        if dino["nombre"].startswith("T"):
            dinosaurios_T.apilar(dino)

    return dinosaurios_T


dinosaurios_T = dinosaurios_con_T(dinosaurios)

print("Los Dinosaurios que empiezan con T son:")
while not dinosaurios_T.esta_vacia():
    dino = dinosaurios_T.desapilar()
    print(dino["nombre"])

# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO D")
print(" ")


def dinosaurios_menos_275kg(dinosaurios):
    dino_menos_275kg = Stack()

    for dino in dinosaurios:
        peso_str = dino["peso"].split()[0]
        peso = int(peso_str)
        if peso < 275:
            dino_menos_275kg.apilar(dino)

    return dino_menos_275kg


dinosaurios_ligeros = dinosaurios_menos_275kg(dinosaurios)

print("Los dinosaurios que pesan menos de 275 kg son:")
while not dinosaurios_ligeros.esta_vacia():
    dino = dinosaurios_ligeros.desapilar()
    print(f'{dino["nombre"]} - {dino["peso"]}')

# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO E")
print(" ")


def dino_con_a_q_s(dinosaurios):
    letras_dino = Stack()

    for dino in dinosaurios:
        nombre = dino["nombre"]
        primera_letra = nombre[0].upper()
        if primera_letra in ["A", "Q", "S"]:
            letras_dino.apilar(dino)

    return letras_dino


dinosaurios_aparte = dino_con_a_q_s(dinosaurios)

print("Los dinosaurios que comienzan con A, Q o S son:")
while not dinosaurios_aparte.esta_vacia():
    dino = dinosaurios_aparte.desapilar()
    print(dino["nombre"])
