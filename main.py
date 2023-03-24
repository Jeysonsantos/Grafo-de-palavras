from manipular_dados import criar_grafo, formar_frase_antes, formar_frase_depois, tratar_dados
from manipular_dados import vertices_invertidos

def main():
    global grafo
    global vertices_invertidos
    
    dataset_list = tratar_dados()
    grafo = criar_grafo(dataset_list)
    vertices_invertidos = vertices_invertidos()
    palavra=""
    while(palavra!="exit"):
        palavra = str(input("Digite uma palavra:"))
        print()
        frase_antes = formar_frase_antes(palavra)
        frase_depois = formar_frase_depois(palavra)
        frase = frase_antes + frase_depois
        print(frase)
main()
