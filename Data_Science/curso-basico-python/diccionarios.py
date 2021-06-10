def run():
    # mi_diccionario = {
    #     'llave1' : 1,
    #     'llave2' : 2,
    #     'llave3' : 3,
    # }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])
    poblacion_paises = {
    'Chile': 20000000,
    'Argentina': 44000000,
    'Brasil': 210000000
    }

    # # print(poblacion_paises)
    # for pais in poblacion_paises.keys():
    # #     print(pais)
    # for pais in poblacion_paises.values():
    #     print(pais)
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene' + str(poblacion) + ' habitantes')
if __name__ =='__main__':
     run()