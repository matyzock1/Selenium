nombre = 'Matías'

for x in range(0,10):
    print(nombre)


colores = ['rojo', 'verde', 'azul', 'amarillo']

for color in colores:
    print(color.upper())

#imprimirá del 1 al 100 de 5 en 5
for y in range(1,100,7):
    if y >= 75:
        break
    print(y)



#Imprimirá del 1 al 10, pero no imprimirá el 3
for num in range(10):
    if num == 3 or num == 5:
        continue
    print(num)
