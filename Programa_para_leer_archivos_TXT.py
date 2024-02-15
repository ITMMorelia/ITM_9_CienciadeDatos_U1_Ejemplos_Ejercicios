import os
archivo_externo =  "texto_005_fragmento_en_paz_amado_nervo.txt"
archivo_en_memoria = open(archivo_externo)

with open(archivo_externo) as archivo_en_memoria:
    texto = archivo_en_memoria.read()

print("\nNombre del archivo: ", archivo_externo)
print("\nTexto completo: \n", texto)
print("\nCantidad de caracteres: ", len(texto))
print("\nTamaño del archivo: ",os.path.getsize(archivo_externo),"\n")