#Modulos/Librerias
"""
sys: Utilizado para cerrar el programa cuando el usuario lo desee 
datetime: Usado para validar la fecha ingresada por el usuario  
"""
import sys 
from datetime import datetime
from funcionalidades.manejo_gastos import gastos,agregar_gasto,mostrar_gastos
from funcionalidades.persistencia_datos.persistencia_csv import existe_carpeta, crear_carpeta,existe_csv, crear_csv,csv_a_dicionario,diccionario_a_csv

#Menus: aqui se almacena todos los menus que el usuario ve
menu_principal = {
    #Menu creado en diccionario para la facil actualizacion de cara a furturas versiones
    "1":"Ingresar un gasto",
    "2":"Mostrar gastos ",
    "3":"Salir",
}
#Funciones
def mostrar_menus(menu):
    #Recorre cada una de las partes del menu ingresado, imprimiendolo en pantalla en cada iteracion  
    for opcion,descripcion in menu.items():
        print(f"{opcion}.{descripcion}")
#Seleccion del menu: cada funcion de esta seccion identifica que accion quiere hacer el usuario cuando se muestra el menu
def seleccion_menu_principal(opcion):
    #Analiza 
    match opcion:
        case "1":
            agregar_gasto()
        case "2":
            mostrar_gastos(gastos)
        case "3":
            diccionario_a_csv()
            print("buen dia")
            sys.exit()
    
#Programa
while True:
    if not existe_carpeta():
        crear_carpeta()
    if not existe_csv():    
        crear_csv()
    csv_a_dicionario()
    mostrar_menus(menu_principal)
    opcion = input("Que quiere hacer hoy")
    seleccion_menu_principal(opcion)