# ANALIZADOR DE GASTOS PERSONALES (AGP)

## ¿Quién soy?

Mi nombre es Javier Mauricio Rueda Menco, tengo 18 años y me apasiona el análisis de datos, fintech y banca. Mi objetivo es ser Analista de Datos especializado en fraude y riesgo financiero. Actualmente estoy terminando mi técnico como Auxiliar Bancario Financiero en el Centro de Formación Bancaria y Financiera de Colombia. Este es mi primer proyecto combinando programación, fintech y análisis de datos.

## Descripción General

El analizador de gastos o AGP es una herramienta para registrar y visualizar gastos de forma clara, con persistencia de datos y validaciones robustas, diseñada como proyecto de aprendizaje en fintech y análisis de datos.

## Mi Motivación

Comencé este proyecto el 14 de febrero de 2026. Llevo aproximadamente 4 semanas aprendiendo a programar y me interesa mucho conocer los estándares de la industria en el desarrollo. Con cada versión, intento aplicar nuevos conceptos de desarrollo profesional, análisis de datos y finanzas para construir un proyecto robusto y que sea escalable en el futuro.

## Stack Tecnológico

- Lenguaje: Python 3.10+
- Librerías: sys, datetime, os, pathlib
- Persistencia: CSV (v1.1.0+)
- Control de versiones: Git

## Cómo Ejecutarlo

1. Clona o descarga el repositorio
2. Abre la terminal en la carpeta del proyecto
3. Instala las dependencias con: pip install -r requirements.txt
4. Ejecuta el programa: python src/main.py

## Roadmap de Versiones

- v1.0.0 - MVP: Registrar y mostrar gastos
- v1.1.0 - Persistencia CSV
- v1.2.0 - Modificar gastos
- v1.3.0 - Eliminar gastos
- v1.4.0 - Análisis básico
- v1.5.0+ - Filtros, validaciones avanzadas, Power BI

## Funcionalidades

### v1.0.0: MVP

- Registrar gastos: El programa pide al usuario nombre, monto, categoría y fecha, hace validación individual de cada campo antes de guardarlo
- Mostrar gastos: Visualiza todos los gastos que el usuario ha registrado con sus detalles 
- Menú : El usuario puede navegar por un menú escogiendo que quiere hacer
- Validación de datos: Verifica que lo que el usuario ingrese sea válido antes de procesarlo

### v1.0.1: Refactor

- Mismas funcionalidades de v1.0.0 pero con código refactorizado y mejor estructurado en modulos

### v1.1.0: Persistencia CSV

- Guardar gastos en archivo: Los gastos se guardan automáticamente en data/datos.csv después de cada registro
- Cargar datos al iniciar: El programa recupera automáticamente todos los gastos guardados cuando se abre
- Gestión de archivos: Crea la carpeta data/ y/o el archivo "datos.csv" si no existe 

## Conceptos Aprendidos

### v1.0.0: MVP

**Python:**
- Funcionamiento de diccionarios y navegación dentro de estos
- Diccionarios anidados como estructuras para guardar items con características
- Funciones que organizan procesos sin necesariamente retornar valores
- Ciclos for y while para tareas repetitivas
- Manejo de validaciones con try/except e if
- Librería datetime para manipular datos en formato de fechas
- Función len() para medir variables
- match y case para validar múltiples opciones eficientemente
- Librería sys y método exit() para cerrar el programa

**Buenas Prácticas:**
- Crear un MVP para validar si una idea es útil antes de invertir tiempo en esta
- Importancia del README para que usuarios no técnicos entiendan el proyecto
- Crear .gitignore para que git omita archivos innecesarios
- Crear requirements.txt para que otros puedan instalar las dependencias
- Nombres de funciones claros y sin ambigüedad
- Principio de responsabilidad única: una función hace una cosa bien
- Documentar el por qué de las decisiones técnicas

**Fintech/Análisis de Datos:**
- Llevar un orden claro de como va a ser la estructura de los datos  (nombre, monto, categoría, fecha)
- Los datos tienen que ser validos antes de manipularlos
- Visualización clara de datos registrados mediante iteración
- Categorizar los gastos para tener una mejor organizacion

---

### v1.0.1: Refactor y Modularización

**Python:**
- Refactorización de código en módulos específicos: validaciones.py, manejo_gastos.py, main.py
- Importaciones relativas (from .validaciones import...) vs absolutas (from funcionalidades.validaciones import...)
- Estructura de carpetas profesional con src/, data/, funcionalidades/
- Funciones auxiliares: sirven para hacer una subtarea dentro de la una funcion principal  
- Uso de f-strings para formateo de texto
- Utilizar siempre nombres claros para cada parte del programa 

**Buenas Prácticas:**
- Separación de responsabilidades: cada módulo tiene un propósito específico y claro
- Usar snake case para los nombres de las funciones 
- Pensar siempre en la estructura primero para poder agregar cosas en el futuro sin mayor problema 
- usar tags en git para marcar las versiones del proyecto

**Fintech/Análisis de Datos:**
- Validar los datos de manera robusta segun el tipo  float para montos, isalpha() para categorías, strptime() para fechas
- Generar automaticamente un id
- Estructura de datos bien pensada (diccionario con claves: nombre, monto, categoría, fecha)

### v1.1.0: Persistencia de Datos con CSV
   
**Python:**
- Rutas relativas con pathlib.Path para evitar errores en la portabilidad
- Lectura de archivos con with open() para que cierren automaticamente
- Escritura de archivos en modo "w" 
- Métodos de strings: strip() quita saltos de línea, split(",") segmenta por comas, join() concatena
- List comprehensions: [str(x) for x in valores_internos] convierte valores en otros de forma automáticamente
- Método .items() para iterar diccionarios anidados de forma eficiente
- os.makedirs() crea carpetas automáticamente si no existen

**Buenas Prácticas:**
- Arquitectura de capas: CSV (persistencia en disco) → RAM (diccionario en memoria) → Procesamiento lógico
- Docstrings en triple comilla para documentación oficial 
- Comentarios concisos para explicar que hace cada funcion
- Organización de código por secciones temáticas con comentarios para separalos 
- Variables constantes en mayúscula RUTA_CSV, RUTA_BASE para 
- Funciónes para organizar el flujo de una accion (diccionario_a_csv)
- Garantizar que archivos estén abiertos solo cuando se necesitan (with statement)

**Fintech/Análisis de Datos:**
- Recuperación completa de todas los datos al reiniciar la aplicación
- Formato CSV como estándar 
- Estructura de datos clara para su entendimiento practico

**Arquitectura implementada:**
- persistencia_csv.py: gestiona como se guardan los archivos en el dispositivo (crear, leer, escribir)
- manejo_gastos.py: bases de la aplicación agregar gastos y mostrar
- validaciones.py: Validación de inputs del usuario para evitar errores
- main.py: flujo principal del programa y control de menús
- Diccionario gastos = {} lugar donde se almacenan los datos mientras la aplicacion esta en uso 

## Ideas Futuras

- Estadísticas por categorías, recomendaciones, análisis de salud financiera
- Sistema de "bolsillos" (diferentes fuentes de dinero)
- Categorías predefinidas y personalizables
- Detección de anomalías y patrones de fraude
- Exportación a Excel/PDF
- Integración con Power BI para dashboards
- SQL para almacenamiento escalable