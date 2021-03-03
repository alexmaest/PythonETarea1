print("Bienvenido")
Peso = float(input("Ingrese su Peso en (kg): "))
Altura = float(input("Ingrese su Altura en (m): "))

imc = (Peso / (Altura*Altura))
print("Su indice de masa corporal es ")
print(round(imc, 2))
