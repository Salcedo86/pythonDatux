# 4.Realizar un programa que permita saber si un usario puede obtener un tarjeta de credito
# condiciones : ser mayor de 18 años , un ingreso mensual de 1000 soles mensual.
# si cumple con las 2 condiciones imprimir que tipo de tarjeta puede obtener
# si su ingreso mensual es de 1000 hasta 3000 soles es tarjeta de clasica , mayor a ello tarjeta dorada.

nombres = input("Hola ingresa tus nombres: ")
edad = int(input("Ingrese su edad: "))
if( edad > 0 and edad <18):
     print(f"Lo siento {nombres} no cuenta con la edad sufiente")

else:    
    sueldo = float(input("¿Cuanto es el sueldo que dispone? "))
if((edad >= 18) and (sueldo>=1000)):
    if(sueldo>=1000 and sueldo<=3000):
        print(f"Felicidades {nombres}, usted podra tener una tarjeta Clasica")
    elif(sueldo > 3000):
        print(f"Felicidades {nombres}, usted podra tener una tarjeta Dorada")
elif((edad >= 18) and sueldo<1000):
    print(f'Lo siento {nombres}, no cuenta con el saldo sufiente')

   
        
    

    