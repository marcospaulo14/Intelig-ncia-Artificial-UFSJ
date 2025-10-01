import pandas
class Tarefa:
    def __init__(self, id, tempo, requisitos=None):
        self.id = id
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
    df = pandas.read_csv('tarefas.csv')
    column_id = df["ID_Tarefa"]
    column_time = df["Tempo_Processamento"]
    lista_tarefas = []
    for i in range (0, len(column_id)-1):
      lista_tarefas.append(Tarefa(column_id[i], column_time[i]))
