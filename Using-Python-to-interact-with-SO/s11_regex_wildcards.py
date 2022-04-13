'''
Uso de expresiones regulares - Wildcards y Character Classes
'''
import re

# La r indica que es un rawstring, y python no tiene que interpretar
# caracteres especiales. Se debe usar siempre en regex
result = re.search(r"aza", "plaza")
print(result)

# ^ --> comienzan con
print(re.search(r"^x", "xenon"))

# . --> wildcard
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))

# No distinguir entre mayusculas y minusculas
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

# Secuencia o rango de caracteres
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"cloud[a-zA-z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

# Elementos que no están contenidos
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# Un elemento u otro
print(re.search(r"cat|dog", "I like cats"))
print(re.search(r"cat|dog", "I like dogs"))
print(re.search(r"cat|dog", "I like both dogs and cats")) #Solo obtiene el primer match
print(re.findall(r"cat|dog", "I like both dogs and cats")) #Todas las ocurrencias
