"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.DataStructures import listiterator as it
import math
assert cf
import time
import tracemalloc

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'category': None,
               }

    catalog['videos'] = lt.newList('SINGLE_LINKED', comparevideos)
    catalog['category'] = mp.newMap(10000,
                                   maptype=tipo,
                                   loadfactor=6.00,
                                   comparefunction=compareMapBookIds)
    return catalog

def comparevideos(id1, id2):
    if (id1.lower() in id2['video_id'].lower()):
        return 0
    return -1

def addVideos(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    mp.put(catalog['category'], video['category_id'], video)
    addVideoCategory(catalog, video)


def addVideoCategory(catalog, video):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    try:
        category = catalog['category']
        if (video['category_id'] != ''):
            pubcategory = video['category_id']
            pubcategory = pubcategory
       
        existyear = mp.contains(category, pubcategory)
        if existyear:
            entry = mp.get(category, pubcategory)
            category_1 = me.getValue(entry)
        else:
            category_1 = newYear(pubcategory)
            mp.put(category, pubcategory, category_1)
        lt.addLast(category_1['videos'], video)
    except Exception:
        return None

def newYear(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "books": None}
    entry['year'] = pubyear
    entry['books'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry
# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compareMapBookIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0


def n_videos_by_category(category_name, country, num_vids, lista, categorias)->list:
    resultado = []
    for i in categorias:
        if categorias[i] == category_name:
            numero_categoria = int(i)

    
    iterador = it.newIterator(lista)
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        menor = math.inf
        contador2 = 0
        if (str(elemento['country']) == country) and numero_categoria == int(elemento['category_id']): 
            if len(resultado) < num_vids:
                resultado.append({"trending_date": elemento["trending_date"], "title": elemento["title"], "channel title": elemento["channel_title"], 
                "publish time": elemento["publish_time"], "views": elemento["views"], "likes": elemento["likes"], "dislikes": elemento["dislikes"]})
            else:
                while contador2 < len(resultado):
                    if float(resultado[contador2]["views"]) < menor:
                        menor = float(resultado[contador2]["views"])
                        posicion = contador2
                    contador2 += 1
                if float(elemento['views']) > menor:
                    resultado.pop(posicion)
                    resultado.append({"trending_date": elemento["trending_date"], "title": elemento["title"], "channel title": elemento["channel_title"], 
                    "publish time": elemento["publish_time"], "views": elemento["views"], "likes": elemento["likes"], "dislikes": elemento["dislikes"]})
    
    return resultado 

def video_trending_pais(country, lista,)->dict:
    mayor = 0 
    aux =[] 
    dict_final = {}      
    iterador = it.newIterator(lista)
    contador2 = 0
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        centinela = True  
        contador = 0     

        if (str(elemento['country'])) == country:
            while contador < len(aux):
                if (elemento['video_id']== aux[contador]["video_id"]):
                    aux[contador]["numero de dias"] += 1
                    centinela = False
                contador +=1

            if centinela == True:
                aux.append({"title": elemento["title"], "channel_title": elemento["channel_title"], 
                "country": elemento["country"], "video_id": elemento["video_id"], "numero de dias": 1})

    while contador2 < len(aux):
        if int(aux[contador2]["numero de dias"]) >= mayor:
            dict_final["title"] = aux[contador2]["title"]
            dict_final["channel_title"] = aux[contador2]["channel_title"]
            dict_final["country"] = country
            dict_final["numero de dias"] = aux[contador2]["numero de dias"]
            mayor = aux[contador2]["numero de dias"]

        contador2 +=1
    return dict_final 

def video_trending_categoria(category_name, lista, categorias)->dict:
    for i in categorias:
        if categorias[i] == category_name:
            numero_categoria = int(i)

    mayor = 0 
    aux =[] 
    dict_final = {}      
    iterador = it.newIterator(lista)
    contador2 = 0
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        centinela = True  
        contador = 0     

        if numero_categoria == int(elemento['category_id']):
            while contador < len(aux):
                if (elemento['title']== aux[contador]["title"]):
                    aux[contador]["numero de dias"] += 1
                    centinela = False
                contador +=1

            if centinela == True:
                aux.append({"title": elemento["title"], "channel_title": elemento["channel_title"], 
                "category_id": elemento["category_id"], "numero de dias": 1, "dates": str(elemento["trending_date"])})

    while contador2 < len(aux):
        if int(aux[contador2]["numero de dias"]) > mayor:
            dict_final["title"] = aux[contador2]["title"]
            dict_final["channel_title"] = aux[contador2]["channel_title"]
            dict_final["category_id"] = numero_categoria
            dict_final["numero de dias"] = aux[contador2]["numero de dias"]
            mayor = int(aux[contador2]["numero de dias"])

        contador2 +=1
    return dict_final

def n_videos_by_tag(tag, country, num_vids, lista)->list:
    resultado = []
    
    iterador = it.newIterator(lista)
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        menor = math.inf
        contador2 = 0
        if (str(elemento['country']) == country) and tag in str(elemento["tags"]).lower(): 
            if len(resultado) < num_vids:
                resultado.append({"title": elemento["title"], "channel title": elemento["channel_title"], "publish time": elemento["publish_time"], 
                "views": elemento["views"], "likes": elemento["likes"], "dislikes": elemento["dislikes"], "tags": elemento["tags"]})
            else:
                while contador2 < len(resultado):
                    if float(resultado[contador2]["likes"]) < menor:
                        menor = float(resultado[contador2]["likes"])
                        posicion = contador2
                    contador2 += 1
                if float(elemento['likes']) > menor:
                    resultado.pop(posicion)
                    resultado.append({"title": elemento["title"], "channel title": elemento["channel_title"], "publish time": elemento["publish_time"],
                    "views": elemento["views"], "likes": elemento["likes"], "dislikes": elemento["dislikes"], "tags": elemento["tags"]})
    return resultado
