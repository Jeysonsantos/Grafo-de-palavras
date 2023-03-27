from manipular_dados import criar_grafo, formar_frase_antes, formar_frase_depois, freq_palavras, print_frequencia_palavras, tratar_dados
from manipular_dados import vertices_invertidos

def main():
    global grafo
    global vertices_invertidos
    global frequencia_palavras
    global freq_palavras

    dataset_list = tratar_dados()
    grafo = criar_grafo(dataset_list)
    frequencia_palavras = freq_palavras(dataset_list)
    vertices_invertidos = vertices_invertidos()

    palavra=""
    while(palavra!="exit"):
        palavra = str(input("Digite uma palavra:"))
        print()
        try:
            frase_antes = formar_frase_antes(palavra)
            frase_depois = formar_frase_depois(palavra)
            frase = frase_antes + frase_depois
            print(frase)
            
        except:
            print("Palavra não encontrada")
    
    #print_frequencia_palavras(frequencia_palavras,10) # Mostra na tela as 10 primeiras palavras com maior frequencia


main()
