from datetime import datetime
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