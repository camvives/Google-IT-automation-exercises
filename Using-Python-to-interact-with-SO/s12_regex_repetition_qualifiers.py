'''
Uso de expresiones regulares - Repetition Qualifiers
'''
import re

# Buscar PY seguido del mayor numero cualquier carracter y que termine con n
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))

# + --> una o más ocurrencias del caracter anterior
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

# ? --> 0 o 1 ocurrencia
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))