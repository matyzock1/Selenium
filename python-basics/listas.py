lenguajes = ['php', 'python', 'javascript', 'java', 'c#', 'c++']
print('Lenguaje seleccionado: ', lenguajes[1])

lenguajes[1] = 'python3'
print('Lenguaje seleccionado: ', lenguajes[1])

lenguajes.append('ruby')

print(lenguajes)

lenguajes.remove('java')
print(lenguajes)