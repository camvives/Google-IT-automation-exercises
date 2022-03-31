'''
Iterar por líneas de archivos
'''

# Cuando se lee línea por línea, en cada una existe un \n, por eso se crean espacios
with open("spider.txt", encoding="UTF-8") as file:
    for line in file:
        print(line.upper())

# Se puede usar `strip()` para eliminar los saltos de línea
with open("spider.txt", encoding="UTF-8") as file:
    for line in file:
        print(line.strip().upper())

# También se puede iterar con listas
file = open("spider.txt", encoding="UTF-8")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

## NOTA: si el archivo es muy grande es conveniente leerlo ##
##   	 línea por línea para no sobrecargar la memoria    ##
