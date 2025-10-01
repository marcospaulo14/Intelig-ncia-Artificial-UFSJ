
class Tarefa:
    def __init__(self, tempo, requisitos=None):
        self.tempo = tempo
        self.requisitos = requisitos if requisitos else []
    
class Maquina:
    def __init__(self, capacidade):
        self.tarefas = []
        self.capacidade = capacidade
    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
    
    def tempo_total(self):
        return sum(tarefa.tempo for tarefa in self.tarefas)


if __name__ == "__main__":
    OpenCNS.read_csv('data.csv')