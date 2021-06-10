import random

def key_generator():
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','Y','Z']
    minusculas = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','y','z']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    simbolos =['!','@','(',')','=','?','¿','¡','"','ª','#','*','^','+',']',':','.',';','<','>','~','{','¬','&','%','·','|','Ç','-','_']

    caracteres = mayusculas + minusculas + numeros + simbolos

    key = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        key.append(caracter_random)

    key = "".join(key) 
    return key  
def run():
    key = key_generator()
    print('Tu nueva contraseña es: ' + key)

if __name__ == '__main__':
  run()