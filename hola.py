cadena="Hola Mundo!"
print(cadena)
cadena="Hola otra vez!"
print (cadena)

#ej3
peso =int(input("¿Que peso en Kg usted tiene? "))
altura=float(input("¿Que altura usted tiene en metros? "))
result=peso//(altura**2)
print("Su indice de masa corporal es :"+ str(result))

#ej4
lista=range(1,101)
for numero in reversed(lista):
    print (numero)

#ej5
def aBisiesto(numero):
    if(numero%4==0):
        print("El numero es bisiesto")
    else:
        print("no es un numero bisiesto")


entrada=int(input("entre un número"))
aBisiesto(entrada)