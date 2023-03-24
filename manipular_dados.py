import pandas as pd
import random
from typing import List
from nltk.tokenize import word_tokenize

from estrutura_dados import Grafo

#------------------------------------------------------------------------------------------------------

def criar_grafo(frases: List[List[str]]) -> Grafo:
    global grafo
    grafo = Grafo()
    for frase in frases:
        for i, palavra in enumerate(frase[:-1]):
            grafo.adicionar_aresta(palavra, frase[i+1])
    return grafo

#------------------------------------------------------------------------------------------------------

def tokenizar(frase):
    stop_words ={',','´-','-Os','1','1-','A','diz','No','Os','As','Com','Para','Se','¿landing','uns','um','uma','collar¿foi','O','E','É','Em','Foi','Esse','Este','Estes','Esses','Na','Nas','Ao','Apos','Após','.','(',')','{','}','[',']','-','!','@','#','$','%','&','*',';',':','/','=','_','estiver', 'estivemos', 'houver', 'forem', 'tínhamos', 'fora', 'terei', 'teve', 'dele', 'houveram', 'éramos', 'foi', 'haver', 'essa', 'pelas', 'tivesse', 'tive', 'ou', 'tivera', 'as', 'qual', 'hão', 'tem', 'a', 'é', 'no', 'estejam', 'estivera', 'estivermos', 'minha', 'estivéssemos', 'houvéssemos', 'mas', 'mesmo', 'à', 'nas', 'são', 'aqueles', 'tua', 'estavam', 'somos', 'entre', 'houvemos', 'haja', 'não', 'estivéramos', 'aquele', 'houverei', 'nossas', 'uma', 'os', 'estive', 'nosso', 'terão', 'tivéssemos', 'houveriam', 'eram', 'seus', 'houvesse', 'quem', 'aos', 'estivesse', 'lhes', 'muito', 'ao', 'delas', 'esta', 'estejamos', 'depois', 'estas', 'fôramos', 'de', 'que', 'esteve', 'ela', 'mais', 'seríamos', 'lhe', 'terá', 'com', 'pelos', 'tivemos', 'nos', 'fomos', 'sou', 'temos', 'tivéramos', 'nossa', 'há', 'vocês', 'estão', 'me', 'tenho', 'estivessem', 'teu', 'era', 'eles', 'para', 'estiverem', 'você', 'houveríamos', 'fosse', 'seu', 'houverem', 'tiveram', 'esteja', 'sem', 'tenham', 'ser', 'tenha', 'do', 'nós', 'numa', 'tu', 'estamos', 'deles', 'sejamos', 'estava', 'isso', 'seremos', 'vos', 'num', 'houvessem', 'esses', 'até', 'houveria', 'houve', 'teremos', 'hajamos', 'essas', 'suas', 'tivermos', 'sua', 'ele', 'o', 'foram', 'tivessem', 'houvéramos', 'se', 'também', 'está', 'pelo', 'meus', 'estiveram', 'sejam', 'tiverem', 'como', 'dos', 'fossem', 'das', 'houvermos', 'elas', 'formos', 'já', 'hei', 'tinha', 'pela', 'isto', 'houverão', 'meu', 'estar', 'quando', 'nossos', 'teríamos', 'aquilo', 'eu', 'nem', 'na', 'teria', 'tiver', 'teus', 'aquela', 'houvera', 'for', 'serei', 'e', 'por', 'seja', 'só', 'fui', 'da', 'tinham', 'havemos', 'te', 'houveremos', 'estes', 'teriam', 'tuas', 'estou', 'será', 'fôssemos', 'hajam', 'um', 'serão', 'este', 'aquelas', 'houverá', 'tém', 'estávamos', 'em', 'dela', 'minhas', 'às', 'tenhamos', 'esse', 'seria', 'seriam'
    }
    word_tokens = word_tokenize(frase)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            if (w != "''") and (w!="``"):
                filtered_sentence.append(w)
    return filtered_sentence

#------------------------------------------------------------------------------------------------------

def tratar_dados():
    dataset = pd.read_excel("C:\\Users\\Teteu\\Desktop\\arvore-python\\licoes_aprendidas.xlsx")
    
    dataset = dataset.drop_duplicates()
    dataset = dataset.dropna()
    dataset_list = dataset['textos'].tolist()
    for indice, frase in enumerate(dataset_list):
        dataset_list[indice] = tokenizar(frase)
    for lista in dataset_list:
        for i in range(len(lista)):
            lista[i] = lista[i].lower()
    return dataset_list

#------------------------------------------------------------------------------------------------------

def formar_frase_antes(palavra):
    frase = "(" + palavra + ")" 
    palavras_utilizadas = [palavra]
    cont1 = 0
    while True:
        if palavra == "" or cont1==30:
            break
        palavras_anteriores = vertices_invertidos[palavra]
        if(palavras_anteriores):
            try:
                palavra_anterior = max(palavras_anteriores, key=palavras_anteriores.get)
            except:
                palavra_anterior,freq = random.choice(list(palavras_anteriores.items()))
            while palavra_anterior in palavras_utilizadas:
                del palavras_anteriores[palavra_anterior]
                try:
                    palavra_anterior = max(palavras_anteriores, key=palavras_anteriores.get)
                except:
                    try:
                        palavra_anterior,freq = random.choice(list(palavras_anteriores.items()))
                    except:
                        break

            frase = palavra_anterior + " " + frase
            palavras_utilizadas.append(palavra_anterior)
            palavra = palavra_anterior
        cont1 += 1
    
    return frase
#------------------------------------------------------------------------------------------------------

def formar_frase_depois(palavra):
    frase = " "
    palavras_utilizadas = [palavra]
    cont1 = 0
    while True:
        if palavra == "" or cont1==30:
            break
        palavras_seguintes = grafo.vertices[palavra]
        if(palavras_seguintes):
            try:
                palavra_seguinte = max(palavras_seguintes, key=palavras_seguintes.get)
            except:
                palavra_seguinte,freq = random.choice(list(palavras_seguintes.items()))
            while palavra_seguinte in palavras_utilizadas:
                del palavras_seguintes[palavra_seguinte]
                try:
                    palavra_seguinte = max(palavras_seguintes, key=palavras_seguintes.get)
                except:
                    palavra_seguinte,freq = random.choice(list(palavras_seguintes.items()))
            frase = frase + palavra_seguinte + " "
            palavras_utilizadas.append(palavra_seguinte)
            palavra = palavra_seguinte
        cont1 += 1
    
    return frase

#------------------------------------------------------------------------------------------------------
def vertices_invertidos():
    global vertices_invertidos
    vertices_invertidos = {}
    for palavra in grafo.vertices:
        for palavra_adjacente in grafo.vertices[palavra]:
            if palavra_adjacente not in vertices_invertidos:
                vertices_invertidos[palavra_adjacente] = {}
            vertices_invertidos[palavra_adjacente][palavra] = grafo.vertices[palavra][palavra_adjacente]
    return vertices_invertidos

#------------------------------------------------------------------------------------------------------
