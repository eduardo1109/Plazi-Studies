import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('elig un numero: '))
    while numero_aleatorio != numero_elegido:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas alto')
        else:
            print('Busca un numero mas pequeño')
        numero_elegido = int(input('elig un numero: '))
    print('Ganaste?')

if __name__ =='__main__':
    run()