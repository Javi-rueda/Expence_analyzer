import os 
from pathlib import Path
#crear la ruta para el csv
RUTA_BASE = Path(__file__).parent.parent.parent 
RUTA_CSV = RUTA_BASE / "data" / "datos.csv"
#Dicionario principal
gastos = {}

#Verificar si existe la carpeta donde deberia estar datos.csv y si no crear carpeta y datos.csv 
def existe_carpeta():
    """Verifica si la carpeta donde se van a guardar los datos del usuario está creada."""
    return os.path.exists(RUTA_CSV.parent)

def crear_carpeta():
    """Crea la carpeta "data" donde se van a guardar los datos del usuario."""
    os.makedirs(RUTA_CSV.parent)

def existe_csv():
    """Verifica si el archivo "datos.csv" donde se van a guardar los datos del usuario esta creado."""
    return os.path.exists(RUTA_CSV)

def crear_csv():
    """Crea el archivo "datos.csv" con el header inicial."""
    with open(RUTA_CSV,"w") as archivo:
        archivo.write("codigo,nombre,monto,categoria,fecha\n")

#Pasar los datos de datos.csv al dicionario gastos en Python
def csv_a_dicionario():
    """Organiza la manera en la que los datos se pasan del archivo "gastos.csv" a el dicionario de Python "gastos"."""
    gastos = leer_csv()
    for gasto in gastos[1:]:
        gasto_limpio = limpiar_gasto_csv(gasto)
        gasto_segmentado = segmentar_gasto(gasto_limpio)
        clave = separar_clave(gasto_segmentado)
        detalles_gasto = crear_subdicionario(gasto_segmentado)
        agregar_dicionario_principal(clave,detalles_gasto)

def leer_csv():
    """Lee linea por linea los datos guardados en el archivo CSV."""
    with open(RUTA_CSV,"r") as archivo:
        gasto = archivo.readlines()
    return(gasto) 

def limpiar_gasto_csv(gasto):       
    """Quita saltos de linea y espacios innecesarios al inicio y final de cada linea."""
    gasto_limpio = gasto.strip()
    return(gasto_limpio)

def segmentar_gasto(gasto_limpio):
    """Divide la linea por comas para separar cada campo del gasto."""
    gasto_segmentado = gasto_limpio.split(",")
    return(gasto_segmentado)

def separar_clave(gasto_segmentado):
    """Extrae el primer valor de la linea que corresponde a la clave identificadora del gasto."""
    clave = gasto_segmentado[0]
    return(clave)

def crear_subdicionario(gasto_segmentado):
    """Introduce los datos de cada gasto en un diccionario con las claves nombre, monto, categoria y fecha."""
    detalles_gasto = {
        "nombre": gasto_segmentado[1],
        "monto":gasto_segmentado[2],
        "categoria":gasto_segmentado[3],
        "fecha":gasto_segmentado[4]
    }
    return(detalles_gasto)

def agregar_dicionario_principal(clave,destalles_gasto):
    """Inserta el gasto en el diccionario principal usando la clave como identificador."""
    gastos[clave] = destalles_gasto 
    return (gastos)

#Pasar datos del dicionario gastos en Python a el archivo datos.csv
def diccionario_a_csv():
    """Organiza la conversion del diccionario de gastos a formato CSV y lo guarda en el archivo."""
    archivo = abrir_csv()
    escribir_header(archivo)
    for llave,dicionario_interno in gastos.items():
        valores_internos = lectura_diccionario(dicionario_interno)
        llave_str,valores_internos_str = gasto_a_str(llave,valores_internos)
        gasto_agrupado = agrupar_gasto_formato_csv(llave_str, valores_internos_str)
        gasto_consolidado = consolidar_linea_gasto(gasto_agrupado)
        agregar_al_csv(archivo,gasto_consolidado)
    archivo.close()

def abrir_csv():
    """Abre el archivo "datos.csv" en modo escritura para guardar los datos."""
    return open(RUTA_CSV,"w") 

def escribir_header(archivo):
    """Escribe el header del archivo CSV con las columnas: codigo, nombre, monto, categoria, fecha."""
    return  archivo.write("codigo,nombre,monto,categoria,fecha\n")

def lectura_diccionario(dicionario_interno):
    """Extrae los valores del subdiccionario de cada gasto, devolviendo unicamente los valores."""
    valores_internos =[]
    for valor_interno in dicionario_interno.values():
        valores_internos.append(valor_interno)
    return valores_internos

def agrupar_gasto_formato_csv(llave, valores_internos):
    """Junta la clave del gasto con sus valores correspondientes en una sola lista."""
    return  [llave] + valores_internos

def gasto_a_str (llave,valores_internos):
    """Convierte la clave y todos los valores del gasto a strings para poder escribir en CSV."""
    llave_str = str(llave)
    valores_internos_str = [str(x) for x in valores_internos]
    return (llave_str,valores_internos_str)

def consolidar_linea_gasto(gasto_agrupado_str):
    """Convierte la lista de valores a una linea en formato CSV separada por comas con salto de linea."""
    return ",".join(gasto_agrupado_str) + "\n"

def agregar_al_csv(archivo,gasto_consolidado):
    """Escribe la linea del gasto en formato CSV al archivo."""
    archivo.write(gasto_consolidado)