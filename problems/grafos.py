class Grafo:
    def __init__(self, n, direcionado=False):
        self.n = n
        self.direcionado = direcionado
        self.adjacencia = {i: [] for i in range(n)}
    
    def add_aresta(self, origem, destino, peso=1):
        self.adjacencia[origem].append((destino, peso))
        if not self.direcionado:
            self.adjacencia[destino].append((origem, peso))
    
    def rmv_aresta(self, origem, destino, peso=1):
        if (destino, peso) in self.adjacencia[origem]:
            self.adjacencia[origem].remove((destino, peso))
        if not self.direcionado and (origem, peso) in self.adjacencia[destino]:
            self.adjacencia[destino].remove((origem, peso))

    def lista_adj(self):
        return self.adjacencia
    
    def __str__(self):
        linhas = ["Lista de adjacência:\n"
                  "nó origem: (nó destino, peso), ...\n"]
        for i in self.adjacencia:
            linhas.append(f"{i}: {self.adjacencia[i]}")
        return "\n".join(linhas)
    
    def matriz_adj(self):
        matriz = [[0] * self.n for _ in range(self.n)]
        for linha in self.adjacencia:
            for coluna, peso in self.adjacencia[linha]:
                matriz[linha][coluna] = peso
            return matriz
    
    def custo_rota(self, rota, ciclo=True):
        custo = 0
        for i in range(len(rota) - 1):
            atual, proximo = rota[i], rota[i+1]
            for vizinho, peso in self.adjacencia[atual]:
                if vizinho == proximo:
                    custo += peso
                    break
        if ciclo:
            atual, proximo = rota[-1], rota[0]
            for vizinho, peso in self.adjacencia[atual]:
                if vizinho == proximo:
                    custo += peso
                    break
        return custo
    
