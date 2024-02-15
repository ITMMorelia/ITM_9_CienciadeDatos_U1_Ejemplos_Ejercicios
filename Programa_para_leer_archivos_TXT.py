# Importar el módulo os para acceder a funcionalidades dependientes del sistema operativo
import os

# Definir el nombre del archivo externo a leer
archivo_externo = "texto_005_fragmento_en_paz_amado_nervo.txt"

# Abrir el archivo en modo lectura y asignarlo a la variable archivo_en_memoria
archivo_en_memoria = open(archivo_externo)

# Abrir el archivo en modo lectura utilizando el contexto de with, asignarlo a la variable archivo_en_memoria y leer su contenido
with open(archivo_externo) as archivo_en_memoria:
    texto = archivo_en_memoria.read()

# Imprimir el nombre del archivo
print("\nNombre del archivo: ", archivo_externo)

# Imprimir el texto completo del archivo
print("\nTexto completo: \n", texto)

# Imprimir la cantidad de caracteres en el texto
print("\nCantidad de caracteres: ", len(texto))

# Imprimir el tamaño del archivo en bytes utilizando la función getsize del módulo os
print("\nTamaño del archivo: ", os.path.getsize(archivo_externo), "\n")
