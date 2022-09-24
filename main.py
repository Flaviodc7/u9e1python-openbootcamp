lst = input("Ingrese paises separados con coma:\n").split(',')
stripped = list(set(list(map(str.strip, lst))))
stripped.sort()
print(stripped)