# NOMBRE (Tanguila, Johanna):

# Carga de librerías necesarias


def download_pubmed( keyword ): 
    """
   La frase de busqueda es la función input, donde muestra el resultado de la lista id de la busqueda en pubmed
    
    
    """
    
    from Bio import Entrez
    from Bio import SeqIO
    from Bio import GenBank 
    
    Entrez.email = 'gA.N.Other@example.com'
    handle = Entrez.esearch(db='pubmed',
                        sort='relevance',
                        retmax='200',
                        retmode='xml',
                        term=keyword)
    results = Entrez.read(handle)
    id_list = results["IdList"]
    ids = ','.join(id_list)
    Entrez.email = 'gA.N.Other@example.com'
    handle = Entrez.efetch(db='pubmed',
                       retmode='xml',
                       id=ids)
    lista_id = ids.split(",")
    return (lista_id) 


import csv 
import re
import pandas as pd 
from collections import Counter
   



def science_plots(archivo):
    """
descripcion de la funcion
    """
    
     AD = []
    pa1 = []
    pa2 = []
    pa3 = []
    pa4 = []
    pa5 = []
    pa6 = []
    pa7 = []
    pa8 = []
    pa9 = []
    pa10 = []
    pa_T = []
    
    
    for line in lista.splitlines():
        if line.startswith("AD  -"):
            AD.append(line[:])
    for line in lista.splitlines():
        if line.startswith("AD  -"):
            AD = line[:]
            p1 = re.findall(r'\,\s(\w{2,16})\.', AD)
            pa1.append(p1)
            
            p2 = re.findall(r'\,\s(\w{2,16}[^0-9\,]\s\w{2,16}[^0-9])\.', AD)
            pa2.append(p2)
            
            p3 = re.findall(r'\,\s(\w{3,16}[^0-9\,]\s\w{2,3}[^0-9\,]\s\w{3,16}[^0-9\,])\.', AD)
            pa3.append(p3)

            p4 = re.findall(r'\,\s(\w{2,16})\.\s[a-z0-9_\.-]+@[\da-z\.-]+\.[a-z\.]{2,6}', AD)
            pa4.append(p4)

            p5 = re.findall(r'\,\s(\w{2,16}[^0-9\,]\s\w{2,16}[^0-9])\.\s[a-z0-9_\.-]+@[\da-z\.-]+\.[a-z\.]{2,6}', AD)
            pa5.append(p5)

            p6 = re.findall(r'\,\s(\w{3,16}[^0-9\,]\s\w{2,3}[^0-9\,]\s\w{3,16}[^0-9\,])\.\s[a-z0-9_\.-]+@[\da-z\.-]+\.[a-z\.]{2,6}', AD)
            pa6.append(p6)
 
            p7 = re.findall(r'\,\s(\w{2,16})\. Electronic address:\s[a-z0-9_\.-]+@[\da-z\.-]+\.[a-z\.]{2,6}\.', AD)
            pa7.append(p7)

            p8 = re.findall(r'\,\s(\w{2,16}[^0-9\,]\s\w{2,16}[^0-9])\. Electronic address:\s[a-z0-9_\.-]+@[\da-z\.-]+\.[a-z\.]{2,6}\.', AD)
            pa8.append(p8)

            p9 = re.findall(r'\,\s(\w{3,16}[^0-9\,]\s\w{2,3}[^0-9\,]\s\w{3,16}[^0-9\,])\. Electronic address:\s[a-z0-9_\.-]+@[\da-z\.-]+\.[a-z\.]{2,6}\.', AD)
            pa9.append(p9)

            p10 = re.findall(r'\,\s\w{3,9}[0-9\-]\,\s(\w{2,16})\.', AD)
            pa10.append(p10)

            pa_T=pa1+pa2+pa3+pa4+pa5+pa6+pa7+pa8+pa9+pa10

    pa_T= list(itertools.chain.from_iterable(pa_T))
    len(pa_T)

    unique_pa_T = list(set(pa_T))
    unique_pa_T.sort()
    len(unique_pa_T)

    import csv
    
    coordenadas = {}
    with open('data/ubipais.txt') as f:
        csvr = csv.DictReader(f)
        for row in csvr:
            coordenadas[row['Name']] = [row['Latitude'], row['Longitude']]
    country = []
    longitude = []
    latitude = []
    almacen = []
    for z in unique_pa_T:
        if z in coordenadas.keys():
            country.append(z)
            latitude.append(float(coordenadas[z][0]))
            longitude.append(float(coordenadas[z][1]))
            almacen.append(pa_T.count(z))
    df_pa_T = pd.DataFrame()
    df_pa_T["Pais"] = country 
    df_pa_T["Numero de autores"] = almacen
   
    return (df_pa_T)
    
    
    
    
    
   
    