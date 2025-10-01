import random
import csv
import time

class Tarefa:
    def __init__(self, id, tempo, dependencias=None):
        self.id = id
        self.tempo = tempo
        self.precedencias = []
        self.dependencias = dependencias if dependencias else []

    def adicionar_precedencia(self, tarefa):
        self.precedencias.append(tarefa)

    def __str__(self):
        return f"Tarefa {self.id}: Tempo {self.tempo}, Dependencias {self.dependencias}"

class VNS:
    def __init__(self, tarefas, maquinas):
        self.tarefas = tarefas
        self.maquinas = maquinas
        self.n_maquinas = len(maquinas)
        self.melhor_solucao = None
        self.melhor_tempo = float('inf')
        
    def solucao_inicial(self):
        return [random.randint(0, self.n_maquinas - 1) for _ in self.tarefas]
    
    def tempo(self, solucao):
        tempos = [0] * self.n_maquinas
        penalidade = 0

        for i, maquina in enumerate(solucao):
            tempos[maquina] += self.tarefas[i].tempo
            for dependencia in self.tarefas[i].dependencias:
                if solucao[dependencia] == maquina:
                    penalidade += 1000
        return max(tempos) + penalidade

    def print_solucao(self, solucao=None):
        if not solucao:
            if self.melhor_solucao:
                solucao = self.melhor_solucao
            else:
                solucao = self.solucao_inicial()
            
        maquinas_tarefas = {i: []  for i in range(self.n_maquinas)}
        for tarefa, maquina in enumerate(solucao):
            maquinas_tarefas[maquina].append(tarefa)
        for maquina, tarefas in maquinas_tarefas.items():
            print(f"Máquina {maquina}: Tarefas {tarefas}")

    def mover_tarefa(self, solucao):
        nova = solucao[:]
        i = random.randint(0, len(nova) - 1)
        nova[i] = random.randint(0, self.n_maquinas - 1)
        return nova
    
    def trocar_tarefas(self, solucao):
        nova = solucao[:]
        i, j = random.sample(range(len(nova)), 2)
        nova[i], nova[j] = nova[j], nova[i]
        return nova
    
    def run(self, max_iter=1000):
        solucao = self.solucao_inicial()
        self.melhor_solucao = solucao
        self.melhor_tempo = self.tempo(solucao)

        for _ in range(max_iter):
            candidato = self.mover_tarefa(solucao)
            tempo_candidato = self.tempo(solucao)

            if tempo_candidato < self.melhor_tempo:
                self.melhor_solucao = candidato
                self.melhor_tempo = tempo_candidato
    
def ler_tarefas(caminho_arquivo):
    precedencias ={}
    tarefas = []

    with open(caminho_arquivo, newline="") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        colunas = leitor.fieldnames or []
        tem_dependencias = "Dependencias" in colunas
        
        for row in leitor:
            tarefa = Tarefa(int(row["ID_Tarefa"]) - 1,
                      int(row["Tempo_Processamento"]))
            

            if tem_dependencias and row["Dependencias"]:
                dependencias = [
                    int(dep) - 1 for dep in row["Dependencias"].split(",")
                    ]
                tarefa.dependencias = dependencias
            tarefas.append(tarefa)
    return tarefas

def ler_maquinas(caminho_arquivo):
    maquinas = []
    with open(caminho_arquivo, newline="") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for row in leitor:
            capacidade = row.get("Capacidade")
            if capacidade:
                maquinas.append(int(capacidade))
    return maquinas
                
if __name__ == "__main__":
    tarefas = ler_tarefas("tarefas.csv")
    maquinas = ler_maquinas("maquinas.csv")

    print("Tarefas:")
    for tarefa in tarefas:
        print(tarefa)

    print("\nMáquinas:", maquinas)

    vns = VNS(tarefas, maquinas)
    vns.run()
    vns.print_solucao()
    print(vns.melhor_tempo)