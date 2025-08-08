def blocodenotas(listinha):
    with open("Afazeres.txt", "w") as f:
        f.write("LISTA DE TAREFAS\n")
        c = 0
        for i in listinha:
            f.write(f" {c}. {i}\n")
            c += 1

def recuperartarefas():
    lista = []
    with open("Afazeres.txt", "w") as f:
        for tarefa in f:
            lista.append(tarefa)