#Modulos/Librerias
"""
sys: Utilizado para cerrar el programa cuando el usuario lo desee 
datetime: Usado para validar la fecha ingresada por el usuario  
"""
import sys 
from datetime import datetime

#Menus
menu_principal = {
    #Menu creado en diccionario para la facil actualizacion de cara a furturas versiones
    "1":"Ingresar un gasto",
    "2":"Mostrar gastos ",
    "3":"Salir",
}
#Datos 
#Dicionario principal donde se guardan los gastos ingresado por el usuario 
gastos = {}
#Funciones
def mostrar_menus(menu):
    #Imprime todos los elementos del menu ingresado 
    for opcion,descripcion in menu.items():
        print(f"{opcion}.{descripcion}")
def agregar_gasto():
    #Organiza el orden en el que se añande un gasto a los datos del usuario
    nombre = validar_nombre()
    monto = validador_monto()
    categoria = validador_categoria()
    fecha = validador_fecha()
    clave = generador_claves(gastos)
    datos_gasto = crear_diccionario(monto,categoria,fecha,nombre)
    acoplar_gasto(gastos,clave,datos_gasto)
    print("Su gasto fue agregado correctamente")
def validador_monto():
    #Valida que el monto que el usuario ingreso sea un dato valido, es decir un numero 
    while True:
        monto = input("Cuanto se gasto ejemplo: 11000.50")
        try:
            monto = float(monto)
        except:
            print("Digite un numero en el formato mostrado") 
            continue  
        return(monto)
def validador_categoria():
    #Valida que el dato que el usuario ingreso no contenga ningun numero 
    while True:
        categoria = input("¿A que categoria pertenece su gasto? \n Ejemplo: transporte, comida, recreación ")
        categoria_limpia = categoria
        categoria_limpia = categoria_limpia.replace(" ","")
        if not categoria_limpia.isalpha():
            print("Digite una categoria valida, no use numeros")   
            continue
        return(categoria)
def validador_fecha():
    #Valida que el dato que el usaurio ingreso este el formato de fecha, aqui usa el modulo datetime para esto
    while True:
        fecha = input("¿Cuando realizo su gasto? Ejemplo: 11/11/2025")
        try:
            fecha = datetime.strptime(fecha,"%d/%m/%Y")
        except:
            print("Digite la fecha en un formato correcto")   
            continue
        return(fecha)
def validar_nombre():
    #Valida que el nombre del gasto no contenga numeros
    while True:
        nombre = input("¿Qué compraste?")
        nombre_limpio = nombre
        nombre_limpio = nombre_limpio.replace(" ","")
        if not nombre_limpio.isalpha():
            print("Digite un nombre valido, no use numeros")   
            continue
        return(nombre)
def id_gasto(dicionario) :
    #Enumera el gasto
    numero_gasto = len(dicionario) + 1
    return(numero_gasto)
def generador_claves(gastos):
    #Crea las claves del dicionario utilizadas en el diccionari principal
    clave = f"gasto_{id_gasto(gastos)}"
    return(clave)
def crear_diccionario(monto,categoria,fecha,nombre):
    #Crea el diccionario donde se guardan los datos de cada gasto 
    datos_gasto = {
        "nombre": nombre,
        "monto": monto,
        "categoria":categoria,
        "fecha":fecha
    }
    return(datos_gasto)
def acoplar_gasto(gastos,clave,datos_gasto):
    #Introduce el nuevo gasto del usuario en el diccionario de todos los gastos 
    gastos[clave] = datos_gasto
def mostrar_gastos(gastos):
    #Muestra todos los gastos introducidos en el diccionario principal
    for gasto,descripcion in gastos.items():
        print(f"{gasto}")
        for caracteristica,valor in descripcion.items():
            print(f"{caracteristica}:{valor}")
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
