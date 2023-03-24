from typing import List
class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, palavra: str) -> None:
        if palavra not in self.vertices:
            self.vertices[palavra] = {}

    def adicionar_aresta(self, palavra1: str, palavra2: str) -> None:
        self.adicionar_vertice(palavra1)
        self.adicionar_vertice(palavra2)
        if palavra2 not in self.vertices[palavra1]:
            self.vertices[palavra1][palavra2] = 0
        self.vertices[palavra1][palavra2] += 1

    def obter_adjacentes(self, palavra: str) -> List[str]:
        return list(self.vertices.get(palavra, {}).keys())

    def obter_porcentagem_entre_duas_palavras(self, palavra1: str, palavra2: str) -> float:
        freq = self.vertices.get(palavra1, {}).get(palavra2, 0) / sum(self.vertices.get(palavra1, {}).values())
        return freq * 100