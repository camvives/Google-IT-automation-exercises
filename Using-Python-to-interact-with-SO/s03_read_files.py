"""
Funciones para leer archivos.
"""
# El sistema operativo comprueba que tenemos permisos para acceder a
# ese archivo y luego le da a nuestro código un File descriptor.
file = open("spider.txt", encoding="UTF-8")

# Lee una sola línea del archivo
print(file.readline())
# Actualiza el estado actual y pasa a la segunda línea
print(file.readline())

#Continúa hasta el final desde donde está el puntero
print(file.read())

#Cierra el archivo para liberar el archivo y el File descriptor
file.close()

# 'with' permite crear un objeto temporal que cierra automaticamente el archivo
with open("spider.txt", encoding="UTF-8") as file:
    print(file.readline())
