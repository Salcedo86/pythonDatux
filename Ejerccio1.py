#nomenclatura de archivos python
nombre = input('Ingrese su nombre: ')
capital = float(input(f"{nombre} Ingrese su capital: "))
tiempo = int(input("Ingresa la cantidad de años: "))

capital_final = capital*(1+(5/100))**tiempo
print(f'Hola {nombre} su capital final es {round(capital_final,2)}')