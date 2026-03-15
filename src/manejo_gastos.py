#MODULOS
import datetime 
from validaciones import validar_nombre,validador_monto,validador_categoria,validador_fecha
#Datos 
#Dicionario principal donde se guardan los gastos ingresado por el usuario 
gastos = {}
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