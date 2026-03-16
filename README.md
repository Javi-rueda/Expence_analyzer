# ANALIZADOR DE GASTOS PERSONALES MVP (PRODUCTO MINIMO VIABLE)

## ¿QUIEN SOY?
Mi nombre es javier mauricio rueda menco, actualmente tengo 18 años me apaciona el mundo de el analisis de datos, el fintech y la banca, en un futuro quiero ser analista de datos, cuento con mucho interes en el analisis de fraude y riesgo financiero, a dia de hoy estoy terminando mi tecnico como auxiliar bancario financiero en el Centro de Formacion Bancaria y Financiera de Colombia, estoy aprendiendo a usar Python, este es mi primer proyecto mesclando todos mis intereses en un solo lugar.
## DESCRIPCION GENERAL
El Analizador de Gastos Personales, tambien conocido como "AGP" es una herramienta de uso personal que sirve para registrar los gastos personales de cada persona y visualizarlos de manera clara para asi llevar un control de el dinero gastado
## MI MOTIVACION
Ya llevo 4 semanas aprendiendo a programar, me interesa mucho conocer los estandares de la industria en el desarrollo y hacer las cosas bien, por eso empiezo este proyecto con una MVP, dentro de este proyecto espero poder aplicar diferentes conceptos que vaya aprendiendo, tanto del desarrollo como de la analitica de datos, ademas de hacer uso de los conocimientos que tengo de la banca y las finansas 
## TECNOLOGIAS USADAS 
Para esta versión se utilizó Python 3.10+ junto a las librerias estandar sys y datetime.
## COMO EJECUTARLO
para ejecutar el programa se requiere de tener instalado cualquier version de python 3.10 o superior.
- Descargue el archivo o clone el repositorio
- Abra la terminal en la carpeta del proyecto
- Instale las dependencias con "pip install -r requirements.txt"
- Ejecuta el archivo principal con Python
## FUNCIONALIDADES
Para esta versión el AGP cumple con su funcion principal, registrar gastos y mostrarlos al usuario 
-Registrar gastos: El programa le pide a el usuario el nombre, el monto, la fecha, y la categoria para guardando en sus gastos,cuando recibe cada uno de los valores hace una pequeña validación individual antes de ingresarlo a sus gastos 
## APRENDISAJES 
### PYTHON
- Funcionamiento de un dicionario y como moverse adentro de este 
- Los dicionarios anidados son estructuras que sirven para guardar items con caracteristicas
- Las Funciones no siempre tienen que devolver algo, pueden simplemente organizar como se realiza un proceso
- Uso del ciclo for y del ciclo while para realizar tareas repetitivas como imprimir varias lineas o pedir un imput nuevamente despues de un intento invalido 
- Manejo de validaciones con try y except o con if 
- Manejo de la libreria datetime para manipular datos en formato de fechas
- Uso de len para medir variables 
- Uso de mach y case para validar muchas opciones de manera eficiente
- Uso de la libreria sys y el metodo exit() para cerrar el programa  

### BUENAS PRACTICAS 
- Realizar un MVP para probar si una idea es util
- Un README es importante para que alguien no tecnico entienda como funciona el proyecto 
- Crear el archivo ".gitignore" para que git omita los archivos que no queremos que se suban
- Crear el archivo "requirement.txt" para que el que vaya a usar el programa pueda instalar todas las librerias y dependecias que se utilizan en el programa  
- Las funciones tienen que tener nombres claros, nada de ambiguedad 
- Una funcion solo tiene que hacer una cosa y tiene que hacerla bien 
- Siempre comentar el porque se hizo algo de alguna manera o que hace en el caso de las funciones

## PROXIMAS MEJORAS
para la version tengo pensado incluir siguientes funcionalidades:
- Modificar los gastos agregados: muestra los gastos que tiene el usurio y le permite modificar algun valor erroneo
- Estadistica basica/ Analisis: le muestra al usuario cual es el gasto mas grande y el gasto mas pequeño que tiene, al igual que la suma de todos los gastos 
- Diferentes filtros: El programa le muestra a el usuario sus gastos dependiendo como las quiera ver, orden y la condicion ejemplo fecha 
- Validaciones mas robustas: utilizar el modulo RegEx para mejores validaciones  
-Guardar los datos del usuario en un csv


## IDEAS FUTURAS 
Aqui algunas ideas que se me ocurren que podrian estar interesantes de incluir al programa:
- Estadistica: estadistica por categorias, recomendaciones, Salud financiera 
- Bolsillos: diferentes lugares de donde salio el dinero para hacer el gasto
- Categorias predefinidas y personalizables
