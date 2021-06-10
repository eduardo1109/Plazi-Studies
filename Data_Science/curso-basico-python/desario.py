def run():
    # word = input('escribe una palabra: ')

    # for i in range(10):
    #     print(word)

    # for i in range(10):
    #     print(i)

    # LIMITE = 1000
    # contador = 0
    # multiplicador = 5
    # while contador < LIMITE:
    #     print(contador * multiplicador) 
    # #     contador = contador + 1 
     
    # edad = int(input('dinos tu edad: '))
    # for i in range(edad):
    #     print(' has cumplido' + ' ' + str(i+1) + ' ' + 'años')

    # numero = int(input('dinos un numero positivo: '))
    # for i in range(1, numero+1, 2):
    #     print(i, end=",")

    # inversion = float(input('cuanto vas a invertir?: '))
    # interes_anual = float(input('cual es el interes que quieres?: '))
    # años = int(input('a cuantos años quieres el retorno?: '))
    # for i in range(años):
    #     inversion *= 1 + interes_anual / 100
    #     print('capital' + str(i+1) + 'años' + str(round(inversion, 2)))

    # numero = int(input('introsuce el alto del triangulo: '))
    # for i in range(numero):
    #     print("*"*(i+1))

    
    for i in range(1, 12):
        for j in range (1, 12):
            print(i*j, end="\t")
        print("")    
if __name__ == '__main__':
    run()