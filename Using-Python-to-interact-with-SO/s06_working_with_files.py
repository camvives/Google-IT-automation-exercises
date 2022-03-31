'''
Manejo de archivos en diferentes SO
'''
import os
# El modulo os es multiplataforma, pero los paths pueden ser diferentes
# en cada sistema
import datetime

# verificar que existe
if os.path.exists("novel.txt"):
    # Renombrar
    os.rename("novel.txt", "finished_masterpiece.txt")
    # Tamaño en bytes
    print(os.path.getsize("finished_masterpiece.txt"))
    # Última modificación en timestamp
    timestamp = os.path.getmtime("finished_masterpiece.txt")
    print(datetime.datetime.fromtimestamp(timestamp))
    # Path absoluto
    print(os.path.abspath("finished_masterpiece.txt"))

    os.rename("finished_masterpiece.txt", "novel.txt")

# Eliminar
os.remove("novel.txt")
