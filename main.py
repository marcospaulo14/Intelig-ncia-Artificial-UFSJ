from problems.maquinas import Maquina, Tarefa
from problems.vns import VNS
import pandas

if __name__ == "__main__":
    df = pandas.read_csv('tarefas.csv')
    column_id = df["ID_Tarefa"].tolist()
    column_time = df["Tempo_Processamento"].tolist()
    lista_tarefas = []
    for i in range (0, len(column_id)-1):
      lista_tarefas.append(Tarefa(column_id[i], column_time[i]))

    # df = pandas.read_csv('maquinas.csv')
    # column_id = df["ID_Maquina"].tolist()
    # column_capacidade = df["Capacidade"].tolist()
    lista_maquinas = []
    # for i in range (0, len(column_id)-1):
    #   lista_maquinas.append(Maquina(column_id[i], column_capacidade[i]))
    
    for i in range(1, 5):
       maquina = Maquina(i, -1)
       lista_maquinas.append(maquina)

    vns_executor = VNS()
    solucao = vns_executor.gera_solucao_maquinas(lista_maquinas, lista_tarefas)
    print(solucao)
