def Suma(a, b):
    print(a + b)

Suma(10, 20)

def NombreCompleto(nombre, apellido):
    print(nombre + " " + apellido)


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

NombreCompleto(nombre, apellido)

def sumita(*args):
    resultado = 0
    for i in args:
        resultado += i
    return print(resultado)


sumita(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)