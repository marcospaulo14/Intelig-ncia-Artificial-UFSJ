import random
import csv
import time
from pathlib import Path

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
    def __init__(self, tarefas, maquinas, tempo_max=1000):
        self.tarefas = tarefas
        self.maquinas = maquinas
        self.n_maquinas = len(maquinas)
        self.melhor_solucao = None
        self.melhor_tempo = float('inf')
        
    def solucao_inicial(self):
        return [random.randint(0, self.n_maquinas - 1) for _ in self.tarefas]
    
    def tempo(self, solucao):
        fim_tarefa = [0] * len(self.tarefas)
        tempos_maquina = [0] * self.n_maquinas

        for tarefa_idx, maquina in enumerate(solucao):
            tarefa = self.tarefas[tarefa_idx]

            if tarefa.dependencias:
                fim_dependencias = max(fim_tarefa[dep] for dep in tarefa.dependencias)
            else:
                fim_dependencias = 0

            inicio = max(fim_dependencias, tempos_maquina[maquina])
            fim = inicio + tarefa.tempo

            fim_tarefa[tarefa_idx] = fim
            tempos_maquina[maquina] = fim

        return max(fim_tarefa)

    def print_solucao(self, solucao=None):
        if not solucao:
            solucao = self.melhor_solucao
            if not solucao:
                solucao = self.solucao_inicial()

        cores = ["\033[94m", "\033[92m", "\033[93m", "\033[95m", "\033[96m"]  # azul, verde, amarelo, magenta, ciano
        fim_cor = "\033[0m"

        maquinas_tarefas = {i: [] for i in range(self.n_maquinas)}
        for tarefa_idx, maquina in enumerate(solucao):
            maquinas_tarefas[maquina].append(tarefa_idx)

        print(f"\n{'='*50}")
        print(f"\033[1mMelhor solução encontrada\033[0m")
        print(f"\033[1mTempo total: {self.tempo(solucao)}\033[0m")
        print(f"{'='*50}")

        for m, tarefas in maquinas_tarefas.items():
            cor = cores[m % len(cores)]
            print(f"\n{cor}Máquina {m}:{fim_cor}")
            print(f"Tarefas: {', '.join(str(t+1) for t in tarefas)}")
        print(f"{'='*50}\n")



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
    
    def run(self, max_iter=10000):
        solucao = self.solucao_inicial()
        self.melhor_solucao = solucao
        self.melhor_tempo = self.tempo(solucao)

        for _ in range(max_iter):
            if random.random() < 0.5:
                candidato = self.mover_tarefa(solucao)
            else:
                candidato = self.trocar_tarefas(solucao)
            
            tempo_candidato = self.tempo(candidato)

            if tempo_candidato < self.melhor_tempo:
                self.melhor_solucao = candidato
                self.melhor_tempo = tempo_candidato
    
def ler_tarefas(caminho_arquivo):
    tarefas = []
    with open(caminho_arquivo, newline="") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for row in leitor:
            tarefa = Tarefa(int(row["ID_Tarefa"]) - 1,
                            int(row["Tempo_Processamento"]))
            
            dep_raw = row.get("Tarefas_Prioridade", "").strip()
            if dep_raw:
                dependencias = [int(dep) - 1 for dep in dep_raw.split(";")]
                tarefa.dependencias = dependencias
            else:
                tarefa.dependencias = []

            tarefas.append(tarefa)
    return tarefas

def ler_maquinas(caminho_arquivo, tempo_maximo=100):
    maquinas = []
    with open(caminho_arquivo, newline="") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        colunas = leitor.fieldnames or []
        tem_capacidade = "Capacidade" in colunas

        for row in leitor:
            if tem_capacidade:
                capacidade = row.get("Capacidade")
            if not capacidade:
                capacidade = tempo_maximo
            maquinas.append(int(capacidade))

    return maquinas
                
if __name__ == "__main__":
    #FACIL
    caminho_arquivo = Path("arquivos_csv") / "tarefas_facil.csv"
    tarefas = ler_tarefas(caminho_arquivo)
    maquinas = [100] * 5
    print(f"\nPROBLEMA FACIL")
    vns = VNS(tarefas, maquinas)
    vns.run()
    vns.print_solucao()

    #MEDIO
    caminho_arquivo = Path("arquivos_csv") / "tarefas_medio.csv"
    tarefas = ler_tarefas(caminho_arquivo)
    caminho_arquivo = Path("arquivos_csv") / "maquinas_medio.csv"
    maquinas = ler_maquinas(caminho_arquivo)
    print(f"\nPROBLEMA MEDIO")
    vns = VNS(tarefas, maquinas)
    vns.run()
    vns.print_solucao()

    #DIFICIL
    caminho_arquivo = Path("arquivos_csv") / "tarefas_dificil.csv"
    tarefas = ler_tarefas(caminho_arquivo)
    maquinas = [100] * 5
    print(f"\nPROBLEMA DIFICIL")
    vns = VNS(tarefas, maquinas)
    vns.run()
    vns.print_solucao()