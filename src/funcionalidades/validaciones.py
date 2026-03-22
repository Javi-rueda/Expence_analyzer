from datetime import datetime

def validador_monto():
    """Valida que el usuario ingrese un número válido en formato decimal (ej: 11000.50)."""
    while True:
        monto = input("Cuanto se gasto ejemplo: 11000.50")
        try:
            monto = float(monto)
        except:
            print("Digite un numero en el formato mostrado") 
            continue  
        return monto

def validador_categoria():
    """Verifica que la categoría contenga solo letras, sin números ni caracteres especiales."""
    while True:
        categoria = input("¿A que categoria pertenece su gasto? \n Ejemplo: transporte, comida, recreación ")
        categoria_limpia = categoria.replace(" ","")
        if not categoria_limpia.isalpha():
            print("Digite una categoria valida, no use numeros")   
            continue
        return categoria

def validador_fecha():
    """Convierte y valida que el input sea una fecha en formato día/mes/año usando datetime."""
    while True:
        fecha = input("¿Cuando realizo su gasto? Ejemplo: 11/11/2025")
        try:
            fecha = datetime.strptime(fecha, "%d/%m/%Y")
        except:
            print("Digite la fecha en un formato correcto")   
            continue
        return fecha

def validar_nombre():
    """Asegura que el nombre del gasto solo contenga letras, sin números."""
    while True:
        nombre = input("¿Qué compraste?")
        nombre_limpio = nombre.replace(" ","")
        if not nombre_limpio.isalpha():
            print("Digite un nombre valido, no use numeros")   
            continue
        return nombre