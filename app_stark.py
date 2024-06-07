from funciones_stark import *
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')  

def menu():
    print("Seleccione una opción:")
    print("1. nombres de los superhéroes")
    print("2. nombres y alturas de los superhéroes")
    print("3. superhéroe más alto")
    print("4. superhéroe más bajo")
    print("5. altura promedio de los superhéroes")
    print("6. superhéroe más pesado")
    print("7. superhéroe menos pesado")
    print("8. pasar al siguiente menu")

    opcion = input("Opción: ")
    return opcion

while True:
    clear_screen()
    opcion = menu()

    if opcion == "1":
        print("el nombre de los superhéroes son:")
        imprimir_nombres_superheroes(lista_personajes)
    elif opcion == "2":
        print("Nombres de los superhéroes con sus alturas:")
        imprimir_nombres_y_alturas(lista_personajes)
    elif opcion == "3":
        print("superhéroe más alto:")
        print(nombre_max_altura)
    elif opcion == "4":
        print("superhéroe más bajo:")
        print(nombre_min_altura)
    elif opcion == "5":
        print("Altura promedio de los superhéroes:", calcular_altura_promedio(lista_personajes))
    elif opcion == "6":
        print("Superhéroe más pesado:")
        print(superheroe_mas_pesado)
    elif opcion == "7":
        print("Superhéroe menos pesado:")
        print(superheroe_menos_pesado)
    elif opcion == "8":
        print("pasando al siguiente menu...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
    
    input("Presione Enter para continuar...")



#--------------------------------------------------------------------------------------------------------------------------------------






def menu():
    print ("Seleccione una opción:")
    print ("1. nombre de superhéroes masculinos")
    print ("2. nombre de superhéroes femeninos ")
    print ("3. superhéroe más alto")
    print ("4. superhéroina más alta")
    print ("5. superhéroe más bajo")
    print ("6. superhéroina más baja")
    print ("7. promedio de la altura de los superhéroes")
    print ("8. promedio de la altura de las superhéroinas")
    print ("9. cantidad de superhéreos por color de ojos")
    print("10. cantidad de superhéroes por color de pelo")
    print("11. cantidad de superhéreos por inteligencia")
    print("12. superhéroes listados por color de ojos")
    print("13. superhéroes listados por color de pelo")
    print("14. superhéroes listados por inteligencia")
    print("15. salir del programa")



    opcion = input("Opción: ")
    return opcion

while True:
    clear_screen()
    opcion = menu()

    if opcion == "1":
        print("nombre de los heroes:")
        for heroe in heroes:
            print(heroe["nombre"])
    elif opcion == "2":
        print("nombre de las heroinas :")
        for heroina in heroinas:
            print(heroina["nombre"])
    elif opcion == "3":
        print("el superhéroe mas alto es:",
            nombre_superhereo_alto)
    elif opcion == "4":
        print("la superhéroina mas alta es:",nombre_superheroina_alta)
    elif opcion == "5":
        print("el superhéroe mas bajo es:",nombre_superheroe_bajo)
    elif opcion == "6":
        print("la superhéroina mas baja es:",nombre_superheroina_baja)
    elif opcion == "7":
        print("el promedio de altura de los superhéroes es:", calcular_altura_promedio(heroes))
    elif opcion == "8":
        print("el promedio de altura de las superhéroinas es:", calcular_altura_promedio(heroinas))
    elif opcion == "9":
        contar_color_ojos(lista_personajes)
    elif opcion == "10":
        contar_color_pelo(lista_personajes)
    elif opcion == "11":
        contar_inteligencia(lista_personajes)
    elif opcion == "12":
        listar_superheroes_por_color_ojos(lista_personajes)
    elif opcion == "13":
        listar_superheroes_por_color_pelo(lista_personajes)
    elif opcion == "14":
        listar_superheroes_por_inteligencia(lista_personajes)
    elif opcion == "15":
        print("saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
    
    input("Presione Enter para continuar...")
