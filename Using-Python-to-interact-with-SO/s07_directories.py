'''
Manejo de directorios
'''
import os

# Cambiar de directorio
os.chdir("Using-Python-to-interact-with-SO")

# Imprime directorio actual
print(os.getcwd())

# Crea un directorio
os.mkdir("new_dir")
os.mkdir("newer_dir")

os.chdir("new_dir")
os.mkdir("sub_dir")
open("hello.txt", 'a', encoding="utf-8").close()
os.chdir("..")

# Elimina el directorio (solo si está vacío)
os.rmdir("newer_dir")

# Mostrar archivos y subdirectorios
print(os.listdir("new_dir"))

#Indica si es directorio o carpeta
DIR = "new_dir"
for name in os.listdir(DIR):
    fullname = os.path.join(DIR, name) #agrega el separador según SO
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")
