'''
Uso de expresiones regulares - Escaping Characters
'''
import re

# Si se intenta buscar algo con . lo reconoce como caracter especial
print(re.search(r".com", "welcome"))
# Para eso hay que usar \ como escape character
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com "))

# \w coincide con letras, numeros y guiones bajos
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

# 