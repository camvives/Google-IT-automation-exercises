'''
Manejo de archivos csv
'''
import csv

f = open("csv_file.txt",encoding="utf-8")
csv_f = csv.reader(f)

for row in csv_f:
    name, phone, role = row
    print(f"Name: {name}, Phone: {phone}, Role: {role}")

f.close()
