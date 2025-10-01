import random
from .maquinas import Maquina, Tarefa
from typing import List

class VNS:
    def __init__(self):
        pass

    def gera_solucao_maquinas(self, maquinas, tarefas) -> List[Maquina]:
        i = 0
        for maquina in maquinas:
            maquina.tarefas = tarefas[i::len(maquinas)-1]
            i += len(maquinas)
        return maquinas
    
    def custo(self, solucao):
        pass
        
    
    def vizinhanca_swap(self, solucao):
        novo = solucao[:]
        return novo
    
    def vizinhanca_reverso(self, solucao):
        novo = solucao[:]
        return novo
    
    # deixei um caso específico como exemplo. Esse resolveria um PCV
    def run(self, max_iter=100):
        pass
