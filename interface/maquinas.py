class Tarefa:
    def __init__(self, id, tempo, requisitos=None):
        self.id = id
        self.tempo = tempo
        self.requisitos = requisitos if requisitos else []
    
class Maquina:
    def __init__(self, id, capacidade):
        self.id = id
        self.tarefas = []
        self.capacidade = capacidade
    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
    
    def tempo_total(self):
        return sum(tarefa.tempo for tarefa in self.tarefas)
