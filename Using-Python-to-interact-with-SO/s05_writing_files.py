'''
Escribir archivos
'''

# Crea el archivo (si no existe) y escribe una línea
# si se ejecuta más de 1 vez reemplaza la línea anterior
with open("novel.txt","w", encoding="UTF-8") as file:
    file.write("It was a dark and stormy night")

## NOTAS: r read only
#        w write only
#        a append
#        r+ read-write
# Si se abre un archivo en modo escritura (w) y ya existe, se borra el contenido
# cuando se abre
