def ordenaPoder(jogador, tamanho, item):
    maximo = item
    filho_esquerda = (item * 2) + 1
    filho_direita = (item * 2) + 2  
    # ve se tem o filho da esquerda e se tiver ele compara
    if filho_esquerda < tamanho and jogador[item][1] < jogador[filho_esquerda][1]:
        maximo = filho_esquerda      
    #ve se tem o filho da direita e se tiver ele compara
    if filho_direita < tamanho and jogador[maximo][1] < jogador[filho_direita][1]:
        maximo = filho_direita  
    #modifica para colocar o pai sendo o maior
    if maximo != item:
        jogador[item], jogador[maximo] = jogador[maximo], jogador[item]
        ordenaPoder(jogador, tamanho, maximo)
        
def ordenaNome(time, tamanho, item):
    maximo = item
    filho_esquerda = (item * 2) + 1
    filho_direita = (item * 2) + 2
    if filho_esquerda < tamanho:
        for indexletra in range(len(time[filho_esquerda])):
            if indexletra > len(time[item]) - 1:
                maximo = filho_esquerda
                break
            if time[filho_esquerda][indexletra] > time[item][indexletra]:
                maximo = filho_esquerda
                break
            elif time[filho_esquerda][indexletra] < time[item][indexletra]:
                break
    if filho_direita < tamanho:
        for indexletra in range(len(time[filho_direita])):
            if indexletra > len(time[maximo]) - 1:
                maximo = filho_direita
                break
            if time[filho_direita][indexletra] > time[maximo][indexletra]:
                maximo = filho_direita
                break
            elif time[filho_direita][indexletra] < time[maximo][indexletra]:
                break
    if maximo != item:
        time[item], time[maximo] = time[maximo], time[item]
        ordenaNome(time, tamanho, maximo)


def separaTimes(jogador):
    global array, times
    tamanho = len(jogador)
    for item in range(tamanho, -1, -1):
        ordenaPoder(jogador, tamanho, item)        
    for index in range(tamanho - 1, 0, -1):
        jogador[index], jogador[0] = jogador[0], jogador[index]
        matriz_times[array%times].append(jogador[index][0])
        array += 1
        ordenaPoder(jogador, index, 0)
    matriz_times[(array)%times].append(jogador[0][0])

def ordemAlpha(time):
    tamanho = len(time)
    for item in range(tamanho, -1, -1):
        ordenaNome(time, tamanho, item)
    for index in range(tamanho - 1, 0, -1):
        time[index], time[0] = time[0], time[index]
        ordenaNome(time, index, 0)




        
array = 0
alunos, times = map(int, input().split())
jogador = []
matriz_times =[[] for x in range(times)]
#pega itens
for aluno in range(alunos):
    nome, poder = input().split()
    jogador.append([nome,int(poder)])
#separa times   
separaTimes(jogador)

n = 1
for time in matriz_times:
    ordemAlpha(time)
    print("Time {}".format(n))
    for aluno in time:
        print(aluno)
    #if n != times:
    print()
    n+=1
