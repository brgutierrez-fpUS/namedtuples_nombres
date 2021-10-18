
from collections import namedtuple


def mostrar_numerado(coleccion):
    i = 0
    for p in coleccion:
        i = i+1
        print(i, p)
    print("\n")


# EJERCICIO 1: Crea un namedtuple de paises, que incluya los atributos nombre, población (en millones), capital, superficie
paises = []

# EJERCICIO 2: Crea las instancias de los siguientes paises, y agrégalos en una lista:
# 'España', 47, 'Madrid', 505370
# 'Finlandia', 5, 'Helsinki', 338145
# 'Estados Unidos', 328, 'Washington D. C.', 9147593
# 'Indonesia', 256, 'Yakarta', 1904569
# 'Japón', 126, 'Tokio', 377975


# EJERCICIO 3: Crea una función que reciba la lista de tuplas que representen los paises, y devuelva la lista de nombres ordenados alfabéticamente de manera inversa
def paises_ordenados_inversa(paises):
    pass


mostrar_numerado(paises_ordenados_inversa(paises))


# EJERCICIO 4: Crea una función que reciba una lista de tuplas que representen los paises, y devuelva el pais con mayor población
def pais_mayor_poblacion(paises):
    pass


p_max_pob = pais_mayor_poblacion(paises)
print('El país con mayor población es: ', p_max_pob)

# EJERCICIO 5: Crea una función que reciba una lista de tuplas que representen los paises, y dos valores.
# La función recorrerá la lista y devolverá aquellos paises cuya superficie esté dentro del intervalo dado como parámetro.


def paises_poblacion_intervalo(paises, minimo, maximo):
    pass


paises_intervalo = paises_poblacion_intervalo(paises, 4, 50)
mostrar_numerado(paises_intervalo)
