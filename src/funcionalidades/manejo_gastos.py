#MODULOS
import datetime 
from .validaciones import validar_nombre,validador_monto,validador_categoria,validador_fecha
from funcionalidades.persistencia_datos.persistencia_csv import gastos

def agregar_gasto():
    """Orquesta el flujo completo para agregar un gasto: pide datos validados, genera clave única y guarda el gasto."""
    nombre = validar_nombre()
    monto = validador_monto()
    categoria = validador_categoria()
    fecha = validador_fecha()
    clave = generador_claves(gastos)
    datos_gasto = crear_diccionario(monto,categoria,fecha,nombre)
    incertar_gasto(gastos,clave,datos_gasto)
    print("Su gasto fue agregado correctamente")
#Funciones estructurales.
def enumeracion_del_gasto(dicionario):
    """Calcula el siguiente ID disponible basado en la cantidad de gastos que ya ha introducido el usuario."""
    numero_gasto = len(dicionario) + 1
    return(numero_gasto)

def generador_claves(gastos):
    """Genera una clave única con formato "gasto_N" donde N es el numero dado por la funcion enumeracion_del_gasto."""
    clave = f"gasto_{enumeracion_del_gasto(gastos)}"
    return(clave)

def crear_diccionario(monto,categoria,fecha,nombre):
    """Estructura los datos del gasto en un diccionario con claves consistentes."""
    datos_gasto = {
        "nombre": nombre,
        "monto": monto,
        "categoria":categoria,
        "fecha":fecha
    }
    return(datos_gasto)
def incertar_gasto(gastos,clave,datos_gasto):
    """Inserta el nuevo gasto en el diccionario principal usando la clave como identificador."""
    gastos[clave] = datos_gasto
#Visualizacion.
def mostrar_gastos(gastos):
    """Recorre todos los gastos e imprime cada uno con sus detalles formateados en cada iteracion."""
    for gasto,descripcion in gastos.items():
        print(f"{gasto}")
        for caracteristica,valor in descripcion.items():
            print(f"{caracteristica}:{valor}")