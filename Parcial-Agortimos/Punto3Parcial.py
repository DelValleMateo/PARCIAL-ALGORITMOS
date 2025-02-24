# Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, colores de sable de luz usados y especie. implementar las funciones
# necesarias para resolver las actividades enumeradas a continuación:
# a) listado ordenado por nombre y por especie;
# b) mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d) mostrar los Jedi de especie humana y twi'lek;
# e) listar todos los Jedi que comienzan con A;
# f) mostrar los Jedi que usaron sable de luz de más de un color;
# g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
# i) Mostrar todos los Jedi que tengan el ranking de Grand Master.

jedis = [
    {
        "name": "Qui-Gon Jinn",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Tera Sinube/Count Dooku",
        "lightsaber_color": "Green",
        "homeworld": "Coruscant",
        "birth_year": "79ABY",
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Obi-Wan Kenobi",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Qui-Gon Jinn/Yoda",
        "lightsaber_color": "Blue",
        "homeworld": "Stewjon",
        "birth_year": "57ABY",
        "height": 1.82,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Anakin Skywalker/Darth Vader",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Obi-Wan Kenobi",
        "lightsaber_color": "Blue",
        "homeworld": "Tatooine",
        "birth_year": "41ABY",
        "height": 1.88,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Quinlan Vos",
        "rank": "Jedi Master",
        "species": "Human/Kiffar",
        "master": "Tholme",
        "lightsaber_color": "Green",
        "homeworld": "Kiffu",
        "birth_year": "59ABY",
        "height": 1.91,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Yoda",
        "rank": "Grand Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "896ABY",
        "height": 0.66,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Mace Windu",
        "rank": "Jedi Master/Master of the Order",
        "species": "Human",
        "master": "Cyslin Myr",
        "lightsaber_color": "Purple",
        "homeworld": "Haruun Kal",
        "birth_year": "72ABY",
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ki-Adi-Mundi",
        "rank": "Jedi Master",
        "species": "Cerean",
        "master": None,
        "lightsaber_color": "Purple/Blue",
        "homeworld": "Cerea",
        "birth_year": "92ABY",
        "height": 1.98,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Plo Koon",
        "rank": "Jedi Master",
        "species": "Kel Dor",
        "master": None,
        "lightsaber_color": "Yellow/Blue/Orange",
        "homeworld": "Dorin",
        "birth_year": "71ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Saesee Tiin",
        "rank": "Jedi Master",
        "species": "Iktotchi",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Iktotch",
        "birth_year": None,
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yaddle",
        "rank": "Jedi Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "509AYB",
        "height": 0.61,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Even Piell",
        "rank": "Jedi Master",
        "species": "Lannik",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Lannik",
        "birth_year": None,
        "height": 1.22,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Oppo Rancisis",
        "rank": "Jedi Master",
        "species": "Thisspiasian",
        "master": "Yaddle",
        "lightsaber_color": "Green",
        "homeworld": "Thisspias",
        "birth_year": "206ABY",
        "height": 1.38,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Adi Gallia",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.84,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yarael Poof",
        "rank": "Jedi Master",
        "species": "Quermian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Quermia",
        "birth_year": None,
        "height": 2.64,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Eeth Koth",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Iridonia",
        "birth_year": None,
        "height": 1.71,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Depa Billaba",
        "rank": "Jedi Master",
        "species": "Chalactan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Chalacta",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kit Fisto",
        "rank": "Jedi Master",
        "species": "Nautolan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Glee Anselm",
        "birth_year": None,
        "height": 1.96,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luminara Unduli",
        "rank": "Jedi Master",
        "species": "Mirialan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mirial",
        "birth_year": "58ABY",
        "height": 1.76,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Barriss Offee",
        "rank": "Padawan",
        "species": "Mirialan",
        "master": "Luminara Unduli",
        "lightsaber_color": "Blue",
        "homeworld": "Mirial",
        "birth_year": "40ABY",
        "height": 1.66,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Shaak Ti",
        "rank": "Jedi Master",
        "species": "Togruta",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Shili",
        "birth_year": None,
        "height": 1.87,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Coleman Trebor",
        "rank": "Jedi Master",
        "species": "Vurk",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Sembla",
        "birth_year": None,
        "height": 2.13,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Jocasta Nu",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.69,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Aayla Secura",
        "rank": "Jedi Knight",
        "species": "Twi'lek",
        "master": "Quinlan Vos",
        "lightsaber_color": "Blue",
        "homeworld": "Ryloth",
        "birth_year": "47ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Sifo-Dyas",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mundos Cassandranos",
        "birth_year": "75ABY",
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Count Dooku",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Yoda",
        "lightsaber_color": "Blue/Red",
        "homeworld": "Serenno",
        "birth_year": "102ABY",
        "height": 1.93,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Pablo-Jill",
        "rank": "Jedi Knight",
        "species": None,
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cúmulo Estelar Skustell",
        "birth_year": None,
        "height": 1.60,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bultar Swan",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Plo Koon",
        "lightsaber_color": "Green",
        "homeworld": "Kuat",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Agen Kolar",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Stass Allie",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Tholoth",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ahsoka Tano",
        "rank": "Padawan",
        "species": "Togruta",
        "master": "Anakin Skywalker",
        "lightsaber_color": "Green/Yellow/Blue/White",
        "homeworld": "Shili",
        "birth_year": "36ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Asajj Ventress",
        "rank": "Padawan",
        "species": "Dathomirian",
        "master": "Ky Narec",
        "lightsaber_color": "Yellow/Red",
        "homeworld": "Dathomir",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Ima-Gun Di",
        "rank": "Jedi Master",
        "species": "Nikto",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Nahdar Vebb",
        "rank": "Jedi Knight",
        "species": "Mon Calamari",
        "master": "Kit Fisto",
        "lightsaber_color": "Blue",
        "homeworld": "Dac",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bolla Ropal",
        "rank": "Jedi Master",
        "species": "Rodian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Rodia",
        "birth_year": None,
        "height": 1.75,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ord Enisence",
        "rank": "Jedi Master",
        "species": "Skrilling",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Agrimundo-2079",
        "birth_year": None,
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tera Sinube",
        "rank": "Jedi Master",
        "species": "Cosian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cosia",
        "birth_year": "102ABY",
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ky Narec",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Pong Krell",
        "rank": "Jedi Master",
        "species": "Besalisk",
        "master": None,
        "lightsaber_color": "Blue/Green",
        "homeworld": "Ojom",
        "birth_year": None,
        "height": 2.36,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Coleman Kcaj",
        "rank": "Jedi Master",
        "species": "Ongree",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Skustell",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplar",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplee",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tu-Anh",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": None,
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kanan Jarrus",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Depa Billaba",
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": "33ABY",
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ezra Bridger",
        "rank": "Padawan",
        "species": "Human",
        "master": "Kanan Jarrus",
        "lightsaber_color": "Blue",
        "homeworld": "Lothal",
        "birth_year": "19ABY",
        "height": 1.65,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luke Skywalker",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Obi-Wan Kenobi/Yoda",
        "lightsaber_color": "Green/Blue",
        "homeworld": "Tatooine",
        "birth_year": "19ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Leia Organa",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Blue",
        "homeworld": "Alderaan",
        "birth_year": "19ABY",
        "height": 1.50,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ben Solo/Kylo Ren",
        "rank": "Padawan",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Green/Blue",
        "homeworld": "Chandrila",
        "birth_year": "5DBY",
        "height": 1.89,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Rey Skywalker",
        "rank": "Jedi Sentinel",
        "species": "Human",
        "master": "Luke Skywalker/Leia Organa",
        "lightsaber_color": "Blue/Green/Yellow",
        "homeworld": "Jakku",
        "birth_year": "15DYB",
        "height": 1.70,
        "to_darkside": None,
        "come_lightside": None
    }
]

# a) listado ordenado por nombre y por especie;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO A")
print(" ")

print("La lista ordenada por nombre y especie es:")


def ordenar_por_nombre_y_especie(jedis):
    def sort_key(jedi):
        return (jedi["name"], jedi["species"])

    return sorted(jedis, key=sort_key)


jedis_ordenados = ordenar_por_nombre_y_especie(jedis)
for jedi in jedis_ordenados:
    print(jedi["name"], jedi["species"])


# b) mostrar toda la información de Ahsoka Tano y Kit Fisto;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO B")
print(" ")


def Ahsoka_Tano():
    Ahsoka_info = {}
    for jedi in jedis:
        if jedi['name'] == 'Ahsoka Tano':
            Ahsoka_info['nombre'] = jedi["name"]
            Ahsoka_info['rango'] = jedi["rank"]
            Ahsoka_info['especie'] = jedi["species"]
            Ahsoka_info['master'] = jedi["master"]
            Ahsoka_info['color del sable'] = jedi["lightsaber_color"]
            Ahsoka_info['casa'] = jedi["homeworld"]
            Ahsoka_info['cumpleaños'] = jedi["birth_year"]
            Ahsoka_info['altura'] = jedi["height"]
            Ahsoka_info['lado oscuro'] = jedi["to_darkside"]
            Ahsoka_info['come_lightside'] = jedi["come_lightside"]

    return Ahsoka_info


print("La informacion de Ahsoka Tano es:")
a = Ahsoka_Tano()
print(a)


def Kit_Fisto():
    Kit_Fisto_info = {}
    for jedi in jedis:
        if jedi['name'] == 'Kit Fisto':
            Kit_Fisto_info['nombre'] = jedi["name"]
            Kit_Fisto_info['rango'] = jedi["rank"]
            Kit_Fisto_info['especie'] = jedi["species"]
            Kit_Fisto_info['master'] = jedi["master"]
            Kit_Fisto_info['color del sable'] = jedi["lightsaber_color"]
            Kit_Fisto_info['casa'] = jedi["homeworld"]
            Kit_Fisto_info['cumpleaños'] = jedi["birth_year"]
            Kit_Fisto_info['altura'] = jedi["height"]
            Kit_Fisto_info['lado oscuro'] = jedi["to_darkside"]
            Kit_Fisto_info['come_lightside'] = jedi["come_lightside"]

    return Kit_Fisto_info


print("La informacion de Kit Fisto es:")
b = Kit_Fisto()
print(b)

#  c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO C")
print(" ")


def padawan_yoda():
    yoda_padawan = []
    for jedi in jedis:
        if jedi["master"] == "Yoda":
            yoda_padawan.append(jedi['name'])

    return yoda_padawan


c = padawan_yoda()
print(f"Los padawanes Yoda fueron {c}")


def padawan_Luke():
    luke_padawan = []
    for jedi in jedis:
        if jedi["master"] == "Luke Skywalker":
            luke_padawan.append(jedi['name'])

    return luke_padawan


d = padawan_Luke()
print(f"Los padawanes de Luke Skywalker fueron {d}")

# d) mostrar los Jedi de especie humana y twi'lek;

print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO D")
print(" ")


def especies_humana():
    especie_humana = []
    for jedi in jedis:
        if jedi["species"] == "Human":
            especie_humana.append(jedi["name"])

    return especie_humana


e = especies_humana()
print(f"Los jedi de especie humana son {e}")


def especies_twi_lek():
    especie_twi_lek = []
    for jedi in jedis:
        if jedi["species"] == "Twi'lek":
            especie_twi_lek.append(jedi["name"])

    return especie_twi_lek


f = especies_twi_lek()
print(f"Los jedi de especie Twi'lek son {f}")

# e) listar todos los Jedi que comienzan con A;

print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO E")
print(" ")


def jedis_con_a():
    comienzan_con_A = []
    for jedi in jedis:
        if jedi["name"][0] == "A":
            comienzan_con_A.append(jedi["name"])

    return comienzan_con_A


g = jedis_con_a()
print(f"Los jedis que comienzan con A son {g}")

# f) mostrar los Jedi que usaron sable de luz de más de un color;

print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO F")
print(" ")


def color_sable():
    sablecolores = []
    for jedi in jedis:
        if jedi["lightsaber_color"] is not None and "/" in jedi["lightsaber_color"]:
            sablecolores.append(jedi["name"])
    return sablecolores


h = color_sable()
print(f"Los jedis que usaron sable de luz de más de un color son: {h}")

# g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO G")
print(" ")


def sable_violeta_amarillo():
    sable_amarillo_violeta = []
    for jedi in jedis:
        if "lightsaber_color" in jedi:
            if jedi["lightsaber_color"] is not None and ("Yellow" in jedi["lightsaber_color"] or "Purple" in jedi["lightsaber_color"]):
                sable_amarillo_violeta.append(jedi["name"])

    return sable_amarillo_violeta


i = sable_violeta_amarillo()
print(f"Los jedis que usaron sable de luz amarillo o violeta fueron {i} ")

# h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO H")
print(" ")


def padawans_de_Qui():
    padawansmaestro = []
    for jedi in jedis:
        if 'master' in jedi:
            if jedi["master"] is not None and "Qui-Gon Jin" in jedi["master"]:
                padawansmaestro.append(jedi["name"])

    return padawansmaestro


def padawans_de_Mace():
    maestropadawan = []
    for jedi in jedis:
        if 'master' in jedi:
            if jedi["master"] is not None and "Mace Windu" in jedi["master"]:
                maestropadawan.append(jedi["name"])
            else:
                print("no tiene padawan")
                break
    return maestropadawan


j = padawans_de_Qui()
print(f"Los padawan de Qui-Gon Jin son {j} ")

k = padawans_de_Mace()
print(f"Los padawan de Mace Windu son {k}")

# i) Mostrar todos los Jedi que tengan el ranking de Grand Master.
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO I")
print(" ")


def grand_master():
    jedis_grandmaster = []
    for jedi in jedis:
        if "rank" in jedi:
            if jedi["rank"] is not None and "Grand Master" in jedi["rank"]:
                jedis_grandmaster.append(jedi["name"])

    return jedis_grandmaster


l = grand_master()
print(f"Los jedis grand master son {l}")
