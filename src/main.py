#Modulos/Librerias
"""
sys: Utilizado para cerrar el programa cuando el usuario lo desee 
datetime: Usado para validar la fecha ingresada por el usuario  
"""
import sys 
from datetime import datetime
from manejo_gastos import gastos,agregar_gasto,mostrar_gastos


#Menus
menu_principal = {
    #Menu creado en diccionario para la facil actualizacion de cara a furturas versiones
    "1":"Ingresar un gasto",
    "2":"Mostrar gastos ",
    "3":"Salir",
}
#Funciones
def mostrar_menus(menu):
    #Imprime todos los elementos del menu ingresado 
    for opcion,descripcion in menu.items():
        print(f"{opcion}.{descripcion}")
def seleccion_menu(opcion):
    #Identifica que opcion escogio el usuario 
    match opcion:
        case "1":
            agregar_gasto()
        case "2":
            mostrar_gastos(gastos)
        case "3":
            print("buen dia")
            sys.exit()
    
#Programa
while True:
    mostrar_menus(menu_principal)
    opcion = input("Que quiere hacer hoy")
    seleccion_menu(opcion)