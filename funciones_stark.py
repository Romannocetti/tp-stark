from data_stark import lista_personajes
import os

#desafio stark 00

#funcion A)
def imprimir_nombres_superheroes(lista_personajes):
    for personaje in lista_personajes:
        print(personaje["nombre"])

#funcion B)
def imprimir_nombres_y_alturas(lista_personajes):
    for personaje in lista_personajes:
        print(personaje["nombre"], "-", personaje["altura"])

#funcion C)
def encontrar_superheroe_mas_alto(lista_personajes):
    altura_maxima = 0
    superheroe_mas_alto = None
    for personaje in lista_personajes:
        altura_actual = float(personaje["altura"])
        if altura_actual > altura_maxima:
            altura_maxima = altura_actual
            superheroe_mas_alto = personaje
    return superheroe_mas_alto

#funcion D)
def encontrar_superheroe_mas_bajo(lista_personajes):
    altura_minima = float("inf")
    superheroe_mas_bajo = None
    for personaje in lista_personajes:
        altura_actual = float(personaje["altura"])
        if altura_actual < altura_minima:
            altura_minima = altura_actual
            superheroe_mas_bajo = personaje
    return superheroe_mas_bajo

#funcion E)
def calcular_altura_promedio(lista_personajes):
    suma_alturas = 0
    for personaje in lista_personajes:
        suma_alturas += float(personaje["altura"])
    altura_promedio = suma_alturas / len(lista_personajes)
    return altura_promedio

#funcion F)
def encontrar_superheroe_mas_pesado(lista_personajes):
    peso_maximo = 0
    superheroe_mas_pesado = None
    for personaje in lista_personajes:
        peso_actual = float(personaje["peso"])
        if peso_actual > peso_maximo:
            peso_maximo = peso_actual
            superheroe_mas_pesado = personaje
    return superheroe_mas_pesado

#funcion G)
def encontrar_superheroe_menos_pesado(lista_personajes):
    peso_minimo = float("inf")
    superheroe_menos_pesado = None
    for personaje in lista_personajes:
        peso_actual = float(personaje["peso"])
        if peso_actual < peso_minimo:
            peso_minimo = peso_actual
            superheroe_menos_pesado = personaje
    return superheroe_menos_pesado



#A)
superheroe_max_altura = encontrar_superheroe_mas_alto(lista_personajes)
nombre_max_altura = superheroe_max_altura["nombre"]

#B)
superheroe_min_altura = encontrar_superheroe_mas_bajo(lista_personajes)
nombre_min_altura = superheroe_min_altura["nombre"]

#C)
superheroe_mas_pesado = encontrar_superheroe_mas_pesado(lista_personajes)

#G)
superheroe_menos_pesado = encontrar_superheroe_menos_pesado(lista_personajes)

#desafio stark 01
def map_list(funcion, lista:list) -> list:
    lista_retorno = []   
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno

def filtrar_lista(funcion, lista:list) -> list:
    lista_retorno = []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)	
    return lista_retorno

def reduce_list(funcion, lista):
    ant = lista[0]
    for el in lista[1:]:
        ant = funcion(ant, el)
    return ant

#A)
heroes = filtrar_lista(lambda emp: emp ["genero"] == "M", lista_personajes)

#B)
heroinas = filtrar_lista(lambda emp: emp ["genero"] == "F", lista_personajes)

#C)
superheroe_mas_alto = reduce_list(lambda hero, hero2: hero if float(hero["altura"]) > float(hero2["altura"]) else hero2, heroes)
nombre_superhereo_alto = superheroe_mas_alto["nombre"]

#D)
superheroina_mas_alta = reduce_list(lambda hero, hero2: hero if float(hero["altura"]) > float(hero2["altura"]) else hero2, heroinas)
nombre_superheroina_alta = superheroina_mas_alta["nombre"]

#E)
superheroe_mas_bajo = reduce_list(lambda hero, hero2: hero if float(hero["altura"]) < float(hero2["altura"]) else hero2, heroes)
nombre_superheroe_bajo = superheroe_mas_bajo["nombre"]

#F)
superheroina_mas_baja = reduce_list(lambda hero, hero2: hero if float(hero["altura"]) < float(hero2["altura"]) else hero2, heroinas)
nombre_superheroina_baja = superheroina_mas_baja["nombre"]

#J)
def contar_color_ojos(color_ojos_superheroes):
    color_ojos_superheroes = map_list(lambda hero:hero.get("color_ojos"), lista_personajes)
    conteo_color_ojos = {}
    for color_ojos in color_ojos_superheroes:
        conteo_color_ojos[color_ojos] = conteo_color_ojos.get(color_ojos, 0) + 1


    print("Cantidad de superhéroes por color de ojos:")
    for color_ojos in conteo_color_ojos:
        cantidad = conteo_color_ojos[color_ojos]
        print(f"- {color_ojos}: {cantidad}")

#k)
def contar_color_pelo(color_pelo_superheroes):
    color_pelo_superheroes = map_list(lambda hero: hero.get("color_pelo"), lista_personajes)
    conteo_color_pelo = {}
    for color_pelo in color_pelo_superheroes:
        conteo_color_pelo[color_pelo] = conteo_color_pelo.get(color_pelo, 0) + 1

    print("Cantidad de superhéroes por color de pelo:")
    for color_pelo in conteo_color_pelo:
        cantidad = conteo_color_pelo[color_pelo]
        print(f"- {color_pelo}: {cantidad}")

#L)
def contar_inteligencia(lista_personajes):
    tipos_inteligencia = map_list(lambda hero: hero.get("inteligencia", "No Tiene"), lista_personajes)

    conteo_inteligencia = {}

    for inteligencia in tipos_inteligencia:
        if inteligencia == "":
            inteligencia = "No Tiene"
        conteo_inteligencia[inteligencia] = conteo_inteligencia.get(inteligencia, 0) + 1

    print("Cantidad de superhéroes por tipo de inteligencia:")
    for inteligencia in conteo_inteligencia:
        cantidad = conteo_inteligencia[inteligencia]
        print(f"- {inteligencia}: {cantidad}")

#M)
def listar_superheroes_por_color_ojos(lista_personajes):
    colores_ojos = map_list(lambda hero: hero.get("color_ojos", "Desconocido"), lista_personajes)

    colores_ojos_unicos = list(set(colores_ojos))

    superheroes_por_color_ojos = {}

    for color_ojos in colores_ojos_unicos:
        superheroes_color_actual = filtrar_lista(lambda hero: hero.get("color_ojos", "Desconocido") == color_ojos, lista_personajes)

        nombres_superheroes_color_actual = map_list(lambda hero: hero.get("nombre"), superheroes_color_actual)

        superheroes_por_color_ojos[color_ojos] = nombres_superheroes_color_actual

    print("Superhéroes agrupados por color de ojos:")
    for color_ojos in superheroes_por_color_ojos:
        nombres_superheroes = superheroes_por_color_ojos[color_ojos]
        print(f"- {color_ojos}: {nombres_superheroes}")

#N)
def listar_superheroes_por_color_pelo(lista_personajes):
    colores_pelo = map_list(lambda hero: hero.get("color_pelo", "Desconocido"), lista_personajes)

    colores_pelo_unicos = list(set(colores_pelo))

    superheroes_por_color_pelo = {}

    for color_pelo in colores_pelo_unicos:
        superheroes_color_actual = filtrar_lista(lambda hero: hero.get("color_pelo", "Desconocido") == color_pelo, lista_personajes)
        nombres_superheroes_color_actual = map_list(lambda hero: hero.get("nombre"), superheroes_color_actual)

        if color_pelo == "":
            color_pelo = "No Tiene"

        superheroes_por_color_pelo[color_pelo] = nombres_superheroes_color_actual

    print("Superhéroes agrupados por color de pelo:")
    for color_pelo in superheroes_por_color_pelo:
        nombres_superheroes = superheroes_por_color_pelo[color_pelo]
        print(f"- {color_pelo}: {nombres_superheroes}")

#O)
def listar_superheroes_por_inteligencia(lista_personajes):
    inteligencia = map_list(lambda hero: hero.get("inteligencia", "Desconocido"), lista_personajes)

    inteligencia_unica = list(set(inteligencia))

    superheroes_por_inteligencia = {}


    for inteligencia in inteligencia_unica:
        superheroes_inteligencia_actual = filtrar_lista(lambda hero: hero.get("inteligencia", "Desconocido") == inteligencia, lista_personajes)
        nombres_superheroes_inteligencia_actual = map_list(lambda hero: hero.get("nombre"), superheroes_inteligencia_actual)

        if inteligencia == "":
            inteligencia = "No Tiene"

        superheroes_por_inteligencia[inteligencia] = nombres_superheroes_inteligencia_actual

    print("Superhéroes agrupados por inteligencia:")
    for inteligencia in superheroes_por_inteligencia:
        nombres_superheroes = superheroes_por_inteligencia[inteligencia] 
        print(f"- {inteligencia}: {nombres_superheroes}")


