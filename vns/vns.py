import random
from problems.grafos import Grafo
from problems.maquinas import Maquina, Tarefa

class VNS:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.matriz = grafo.matriz_adj
        self.n = grafo.n

    def gera_solucao_maquinas(self, maquinas):
        for maquina in maquinas:
            

    def gera_solucao_inicial(self):
        solucao = list(range(self.n))
        random. shuffle(solucao)
        return solucao
    
    def custo(self, solucao):
        return self.grafo.custo_rota(solucao)
    
    def vizinhanca_swap(self, solucao):
        novo = solucao[:]
        i, j = random.sample(range(self.n), 2)
        novo[i], novo[j] = novo[j], novo[i]
        return novo
    
    def vizinhanca_reverso(self, solucao):
        novo = solucao[:]
        i, j = sorted(random.sample(range(self.n), 2))
        novo[i:j] = reversed(novo[i:j])
        return novo
    
    # deixei um caso específico como exemplo. Esse resolveria um PCV
    def run(self, max_iter=100):
        melhor = self.gera_solucao_inicial()
        melhor_custo = self.custo(melhor)

        for _ in range(max_iter):
            if random.random() < 0.5:
                candidato = self.vizinhanca_swap(melhor)
            else:
                candidato = self.vizinhanca_reverso(melhor)

            custo_candidato = self.custo(candidato)
            if custo_candidato < melhor_custo:
                melhor, melhor_custo = candidato, custo_candidato
        
        return melhor, melhor_custo
