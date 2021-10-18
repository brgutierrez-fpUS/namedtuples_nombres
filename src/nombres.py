# -*- coding: utf-8 -*-
''' Análisis de frecuencias de nombres

AUTOR: José A. Troyano
REVISOR: Toñi Reina
ÚLTIMA MODIFICACIÓN: Belén Ramos 18/10/2021

En este proyecto trabajaremos con datos correspondientes a los nombres de las
personas nacidas en España desde 2002 a 2017. Los datos están tomados del Instituto
Nacional de Estadística (https://www.ine.es/), donde se pueden encontrar muchos datos interesantes
principalmente sobre la demografía, economía, y sociedad españolas. Representaremos 
la información de entrada mediante listas de tuplas, y a partir de esta estructura implementaremos
una serie de funciones que nos permitirán realizar varios tipos de consultas y generar visualizaciones.

FORMATO DE ENTRADA:
-------------------
Trabajaremos con ficheros en formato CSV. Cada registro del fichero de entrada ocupa
una línea y contiene cuatro informaciones sobre los nombres (anyo, nombre, frecuencia, genero). 
Estas son las primeras líneas de un fichero de entrada:

    anyo,Nombre,Frecuencia,Género
    2002,ALEJANDRO,8020,Hombre
    2002,PABLO,5799,Hombre
    2002,DANIEL,5603,Hombre
    2002,DAVID,5414,Hombre
    2002,ADRIAN,4949,Hombre
    2002,JAVIER,4909,Hombre
    2002,ALVARO,4595,Hombre
    2002,SERGIO,3744,Hombre

FUNCIONES A IMPLEMENTAR:
------------------------
- lee_registros(fichero):
    lee el fichero de registros y devuelve una lista de tuplas con nombre
- filtrar_por_genero(registros, genero):
    recibe una lista de tuplas y devuelve solo los registros del género recibido como parámetro
- calcular_nombres(registros, filtro=None):
    calcula el conjunto de nombres aplicando el filtro de género recibido como parámetro
- calcular_top_nombres_de_anyo(registros, anyo, limite=10, filtro=None):
    calcula los nombres más frecuentes de un anyo
- calcular_nombres_ambos_generos(registros):
    calcula el conjunto de nombres que han sido usados en ambos géneros
- calcular_nombres_compuestos(registros, filtro=None):
    calcula el conjunto de nombres con más de una palabra
- calcular_nombre_mas_frecuente_por_anyo(registros, filtro=None):
    calcula una lista de tuplas (anyo, nombre) con el nombre más frecuentes cada anyo
- calcular_frecuencia_por_anyo(registros, nombre):
    calcula una lista de tuplas (anyo, frecuencia) con las frecuencias de un nonmbre cada anyo
- mostrar_evolucion_por_anyo(registros, nombre):
    genera un gráfico con la evolución de la frecuencia de un nombre
- calcular_frecuencia_acumulada(registros, nombre):
    calcula la frecuencia acumulada de un nombre en todos los anyos
- calcular_frecuencias_por_nombre(registros):
    calcula un diccionario {nombre:frecuencia} con la frecuencia acumulada de cada nombre
- mostrar_frecuencias_nombres(registros, limite=10):
    genera un diagrama de barras con las frecuencias de los nombres más populares
'''

import csv
from collections import namedtuple
#from matplotlib import pyplot as plt

# EJERCICIO 1:
Registro = namedtuple('Registro', 'anyo, nombre, frecuencia, genero')


def leer_frecuencias_nombres(fichero):
    ''' Lee el fichero de registros y devuelve una lista de tuplas con nombre

    ENTRADA: 
       @param fichero: ruta del fichero csv que contiene los datos en codificación utf-8
       @type fichero: str
    SALIDA: 
       @return lista de registros 
       @rtype [Registro(int, str, int, str)]
    '''
    pass


# EJERCICIO 2:
def filtrar_por_genero(registros, genero):
    ''' Recibe una lista de tuplas y devuelve solo los registros del género recibido como parámetro

    ENTRADA: 
       @param registros: lista de registros 
       @type registros: [Registro(int, str, int, str)]
       @param genero: género del que se seleccionarán los registros 
       @type genero: str
    SALIDA: 
       @return lista de registros seleccionados 
       @rtype [Registro(int, str, int, str)]
    '''
    pass


# EJERCICIO 3:
def calcular_nombres(registros, filtro=None):
    ''' Calcula el conjunto de nombres aplicando el filtro de género recibido como parámetro 

    ENTRADA: 
       @param registros: lista de registros 
       @type registros: [Registro(int, str, int, str)]
       @param filtro: 'Hombre', 'Mujer', o None si no se aplica filtro
       @type filtro: str
    SALIDA: 
       @return conjunto de nombres encontrados 
       @rtype {str}
    '''
    pass


# EJERCICIO 4:
def calcular_top_nombres_de_anyo(registros, anyo, limite=10, filtro=None):
    ''' Calcula los nombres más frecuentes de un anyo

    ENTRADA: 
       @param registros: lista de registros 
       @type registros: [Registro(int, str, int, str)]
       @param anyo: del que se hace la consulta 
       @type anyo: int
       @param limite: número de nombres a recuperar 
       @type limite: int
       @param filtro: 'Hombre', 'Mujer', o None si no se aplica filtro
       @type filtro: str
    SALIDA: 
       @return lista de tuplas (nombre, frecuencia) ordenanda de mayor a menor frecuencia  
       @rtype [(str, int)]

    UNA PISTA: para ordenar la lista de tuplas usaremos expresiones lambda, tal como esta: resultado.sort(key=lambda x: x[1], reverse=True)

    '''
    pass


# EJERCICIO 5:
def calcular_nombres_ambos_generos(registros):
    ''' Calcula el conjunto de nombres que han sido usados en ambos géneros

    ENTRADA: 
       @param registros: lista de registros 
       @type registros: [Registro(int, str, int, str)]
    SALIDA: 
       @return conjunto de nombres comunes a ambos géneros  
       @rtype {str}

    UNA PISTA: para obtener los elementos comunes a dos conjuntos utilizamos la función intersection (intersección de conjuntos) -> nombres_hombres.intersection(nombres_mujeres)
    '''
    pass


# EJERCICIO 6:
def calcular_nombres_compuestos(registros, filtro=None):
    ''' Calcula el conjunto de nombres con más de una palabra

    ENTRADA: 
       @param registros: lista de registros 
       @type registros: [Registro(int, str, int, str)]
       @param filtro: 'Hombre', 'Mujer', o None si no se aplica filtro
       @type filtro: str
    SALIDA: 
       @return conjunto de nombres con más de una palabra 
       @rtype {str}

    UNA PISTA: Podemos saber que un nombre es compuesto cuando contiene un espacio
    '''
    pass


# EJERCICIO 7:
def calcular_nombre_mas_frecuente_por_anyo(registros, filtro=None):
    ''' Calcula una lista de tuplas (anyo, nombre) con el nombre más frecuentes cada anyo

    ENTRADA: 
       @param registros: lista de registros 
       @type registros: [Registro(int, str, int, str)]
       @param filtro: 'Hombre', 'Mujer', o None si no se aplica filtro
       @type filtro: str
    SALIDA: 
       @return lista de tuplas (anyo, nombre, frecuencia) ordenanda por anyo  
       @rtype [(int, str, int)]

    Se calculará en primer lugar la lista de anyos y, posteriormente, se buscará el nombre
    más frecuente para cada anyo.

    UNA PISTA: para encontrar el más frecuente utilizaremos la función max -> anyo_registro, nombre, frecuencia, genero = max(registros_anyo, key=lambda r: r.frecuencia)

    '''
    pass


# EJERCICIO 8:
def calcular_frecuencia_por_anyo(registros, nombre):
    ''' Calcula una lista de tuplas (anyo, frecuencia) con las frecuencias de un nonmbre cada anyo

    ENTRADA: 
        @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
        @param nombre: nombre del que se hace la consulta 
        @type nombre: str
    SALIDA: 
       @return lista de tuplas (anyo, frecuencia) ordenanda por anyo  
       @rtype [(int, int)]

    En el caso de que un nombre se use para hombres y mujeres, se sumarán ambas frecuencias
    '''
    pass


# EJERCICIO 9:
def mostrar_evolucion_por_anyo(registros, nombre):
    ''' Genera un gráfico con la evolución de la frecuencia de un nombre

    ENTRADA: 
       @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
        @param nombre: nombre del que se hace la consulta 
        @type nombre: str
    SALIDA EN PANTALLA: 
       - curva con la evolución de la frecuencia del nombre

    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.plot(anyos, frecuencias)
        plt.title("Evolución del nombre '{}'".format(nombre)
        plt.show()
    Donde 'anyos' y 'frecuencias' se extraen del resultado de la función
    'calcular_frecuencia_por_anyo'
    '''
    # anyos_frecuencias = calcular_frecuencia_por_anyo(registros, nombre)
    # anyos = [anyo for anyo, frecuencia in anyos_frecuencias]
    # frecuencias = [frecuencia for anyo, frecuencia in anyos_frecuencias]
    # plt.plot(anyos, frecuencias)
    # plt.title("Evolución del nombre '{}'".format(nombre))
    # plt.show()


# EJERCICIO 10:
def calcular_frecuencia_acumulada(registros, nombre):
    ''' Calcula la frecuencia acumulada de un nombre en todos los anyos

    ENTRADA: 
        @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
        @param nombre: nombre del que se hace la consulta 
        @type nombre: str
    SALIDA: 
       @return suma de las frecuencias del nombre en todos los anyos  
       @rtype int
    '''
    pass


# EJERCICIO 11:
def calcular_frecuencias_por_nombre(registros):
    ''' Calcula un diccionario {nombre:frecuencia} con la frecuencia acumulada de cada nombre

    ENTRADA: 
        @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
    SALIDA: 
       @return diccionario con la frecuencia acumulada de cada nombre 
       @rtype {str:int}

    Hay dos posibles soluciones: (1) invocando a funciones que hemos implementado en los ejercicios anteriores y (2) haciendo uso de defaultdict, que en este caso es más eficiente

    '''
    pass


# EJERCICIO 12:
def mostrar_frecuencias_nombres(registros, limite=10):
    ''' Genera un diagrama de barras con las frecuencias de los nombres más populares

    ENTRADA: 
        @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
        @param limite: número de nombres a mostrar 
        @type limite: int
    SALIDA EN PANTALLA: 
       - diagrama de barras con las frecuencias de los nombres más populares

    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.bar(nombres, frecuencias)
        plt.xticks(rotation=80)
        plt.title("Frecuencia de los {} nombres más comunes".format(limite))
        plt.show()

    Donde 'nombres' y 'frecuencias' se extraen del resultado de la función
    'calcular_frecuencias_por_nombre'. El cálculo de los nombres más populares se puede
        realizar ordenando las claves del diccionario devuelto por 'calcular_frecuencias_por_nombre'
        en función de sus valores asociados.
    '''
    # frecuencias_nombres = calcular_frecuencias_por_nombre(registros)
    # nombres = sorted(frecuencias_nombres,
    #                  key=frecuencias_nombres.get, reverse=True)[:limite]
    # frecuencias = [frecuencias_nombres[nombre] for nombre in nombres]

    # plt.bar(nombres, frecuencias)
    # plt.xticks(rotation=80)
    # plt.title("Frecuencia de los {} nombres más comunes".format(limite))
    # plt.show()
