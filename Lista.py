import time
escolha = 0
primeira = input("Olá, gostaria de fazer uma lista de afazeres? (S/N) ").upper()
if primeira == "S":
    Listadetarefas = []
while True:

    if escolha == 0:
        folha = print ("""    ____________________________________
    |                                  |
    |      Nova lista de Afazeres      | 
    |__________________________________|
    |                                  |
    |   1. Inserir Tarefas             |
    |                                  |
    |   2. Listar Tarefas              |
    |                                  |
    |   3. Marcar como Concluído       |
    |                                  |
    |   4. Excluir Tarefas             |
    |                                  |
    |   5. Sair                        |
    |__________________________________|
    """)
    escolha = int(input("O quê você deseja fazer? "))
    if escolha == 1:
        tarefa = input("Tudo bem, o quê gostaria de adicionar na lista de tarefas? ")
        while True:
            Listadetarefas.append(tarefa)
            continuar = input("Quer adicionar mais alguma coisa? (S/N) ").upper()
            if continuar == "N":
                print("Tudo bem!")
                escolha = 0
                time.sleep(1)               
                break
            else:
                tarefa = input("O quê você gostaria de adicionar na lista de tarefas? ")


    elif escolha == 2:
        c = 0
        for i in Listadetarefas:
            print (f" {c}. {i}")
            c += 1
        input ("Aperte ENTER para continuar.")
        escolha = 0
        time.sleep(1)

    elif escolha == 3:
        c = 0
        for i in Listadetarefas:
            print (f" {c}. {i} ")
            c += 1
        pergunta = (input("Gostaria de concluir algum item da lista? (S/N) ")).upper()
        if pergunta == "S":
            n = int(input("Qual item? "))
            Listadetarefas[n] = Listadetarefas[n] + " ☑"
            print ("Item marcado!")
            time.sleep(1)
        else:
            escolha = 0
            time.sleep(1)


    elif escolha == 4:
        c = 0
        for i in Listadetarefas:
            print (f" {c}. {i} ")
            c += 1
        pergunta = (input("Gostaria de excluir algum item da lista? (S/N) ")).upper()
        if pergunta == "S":
            n = int(input("Qual item? "))
            Listadetarefas.pop(n)
            c = 0
            for i in Listadetarefas:
                print (f" {c}. {i} ")
                c += 1
            print ("Item excluido!")
            input ("Aperte ENTER para continuar.")
            escolha = 0
            time.sleep(1)
        else:
            escolha = 0
            time.sleep(1)


    elif escolha == 5:
        print("Ok, até mais!")
        time.sleep(1)
        quit()