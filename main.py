archiveToCompact = "teste.txt" # Esse arquivo é utilizado para debugging
#archiveToCompact = "compactacao1M.txt"

# Compactação por frequência de caracteres
import charFrequency as CF
CF.compress(archiveToCompact)

# ===================================================================================

# Compactação por árvore de Huffman
from ArvoreDeHuffman import ArvoreDeHuffman
from NodoDaArvore import NodoDaArvore
from ordenador import Ordenator

ordenador = Ordenator()

def SelecionaNodoMenorChave(array_nodos):
    menor_nodo = array_nodos[0]
    for nodo in array_nodos:
        if(nodo.frequencia < menor_nodo.frequencia):
            menor_nodo = nodo
    
    return menor_nodo

arquivo = open(archiveToCompact, encoding='latin-1')

dicionario_frequencia ={}

for linha in arquivo:
    for caractere in linha:
        if caractere not in dicionario_frequencia.keys():
            dicionario_frequencia[caractere]=1
        elif caractere in dicionario_frequencia.keys():
            dicionario_frequencia[caractere]+=1

array_nodos = []

for chave in dicionario_frequencia.keys():
    nodo = NodoDaArvore(chave, dicionario_frequencia[chave])
    array_nodos.append(nodo)

arvoreHuffman = ArvoreDeHuffman()

ordenador.insercao(array_nodos)
while len(array_nodos)!=1:
    menor_nodo = array_nodos[0]
    segundo_menor_nodo = array_nodos[1]
    novo_nodo = NodoDaArvore(None, menor_nodo.frequencia+segundo_menor_nodo.frequencia)
    
    novo_nodo.esquerdo = menor_nodo
    novo_nodo.direito = segundo_menor_nodo
    
    menor_nodo.pai = novo_nodo
    segundo_menor_nodo.pai = novo_nodo
    
    array_nodos.remove(menor_nodo)
    array_nodos.remove(segundo_menor_nodo)
    array_nodos.append(novo_nodo)

    ordenador.insercao(array_nodos)

arvoreHuffman.raiz = array_nodos[0]

arvoreHuffman.printArvore(arvoreHuffman.raiz)

arvoreHuffman.compactaArquivo(archiveToCompact, "arquivo_saida.txt")
arvoreHuffman.converteBinario("arquivo_saida.txt")