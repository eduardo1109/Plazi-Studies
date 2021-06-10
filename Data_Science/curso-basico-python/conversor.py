# menu = """ 
# Bienvenido al conversor de monedas

# 1-pesos chilenos
# 2-pesos colombianos 
# 3-pesos argentinos 

# Elige una opcion"""

# opcion = int(input(menu))
# if opcion == 1:
#     pesos = input("¡Cuantos pesos chilenos tienes ?: ")
#     pesos = float(pesos)
#     valor_dolar = 735
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("tienes $" + dolares + "dolares")
# elif opcion == 2:
#     pesos = input("¡Cuantos pesos colombianos tienes ?: ")
#     pesos = float(pesos)
#     valor_dolar =3709
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("tienes $" + dolares + "dolares")

# elif opcion == 3:
#     pesos = input("¡Cuantos pesos argentinos tienes ?: ")
#     pesos = float(pesos)
#     valor_dolar = 94
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("tienes $" + dolares + "dolares")
# else:
#     print("ingresa una opcion")

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¡Cuantos pesos" + tipo_pesos + "chilenos tienes ?: " )
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " " + "dolares")
menu = """ 
Bienvenido al conversor de monedas

1-pesos chilenos
2-pesos colombianos 
3-pesos argentinos 

Elige una opcion"""
opcion = int(input(menu))
if opcion == 1:
   conversor("peso chileno", 735)
elif opcion == 2:
   conversor("peso colombiano", 3709)
elif opcion == 3:
   conversor("peso argentino", 94)
else:
    print("ingresa una opcion")
