# 3. Realice un programa que calcule la suma de los numeros hasta el valor ingresado.
# Ejemplo : Si ingresa 5 se tendra que calcular 1+2+3+4+5

x = 1
suma = 0
n = int(input("Ingrese un valor: "))
while(x<=n):   
    print(f'{x}', end=' ')   
    suma = suma + x
    x+=1
print()
print(f'El resultado de la suma de la serie de números es:{suma}')