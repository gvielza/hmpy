from unittest import result


cadena="Hola Mundo!"
print(cadena)
cadena="Hola otra vez!"
print (cadena)

#ej3
peso =int(input("¿Que peso en Kg usted tiene?"))
altura=float(input("¿Que altura usted tiene en metros?"))
result=peso//(altura**2)
print("Su indice de masa corporal es :"+ str(result))
