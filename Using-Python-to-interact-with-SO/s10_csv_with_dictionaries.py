'''
Leer y escribir archivos que contienen nombres de columna
'''
import csv

# Leer archivos con diccionario
with open('software.csv', encoding="utf-8") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users.").format(row["name"], row["users"]))

# Escribir archivos de un diccionario
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
{"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
{"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w', encoding="utf-8") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
