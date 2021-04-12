"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time
import string


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar catalogo")
    print("2- Cargar información en el catálogo")
    print("3- Cargar los n videos con mas likes para el nombre de una categoria especifica")


def initCatalog(tipo):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tipo)

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def loadCategories():
    return controller.loadCategories()

def showCategories():
    return controller.showCategories()
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.initCatalog('CHAINING')

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        answer = controller.loadData(cont)
        print("Videos cargados: ", lt.size(cont['videos']))
        print("categorias cargadas: ")
        showCategories()
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
        
    elif int(inputs[0]) == 3:
        category_name = str(input("ingrese el nombre de la categoria que desea buscar")).translate({ord(c): None for c in string.whitespace})
        country = str(input("ingrese el nombre del pais por el que desea buscar"))
        num_vids = int(input("ingrese el numero de videos que desea listar"))
        a = controller.req1(category_name, country, num_vids, catalog['videos'], loadCategories())
        print(a)

    else:
        sys.exit(0)
sys.exit(0)
