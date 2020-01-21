import sys#provavelmente vai passar de tamanho de recursao
sys.setrecursionlimit(100000)#aloquei memoria para ele conseguir ser cabivel

def medeCaminho(dic, atual, final, dist = 0, ant = -100):#leva a listas de x = f(x)
    if atual == final:#se ele chegou onde queria print e return
        print(dist)
        return
    else:
        for natual in fxs[atual]:#ve os caminhos possiveis de onde pode ir
            if natual != ant: #n repete caminho
                if medeCaminho(dic, natual, final, dist + 1, atual):#empilha legal
                    return
        return




cidades, atual, final = map(int, input().split())#pega quantidade de casas
fxs = {}#pega o valor de x e de f(x) funciona como grafos
for i in range (1, cidades + 1): # prepara o dicionario
    fxs[i] = []
for i in range(cidades - 1):#pega as entradas e adiciona valores nos grafos
    x, fx = map(int, input().split())
    fxs[x].append(fx)#coloca que x vai para fx
    fxs[fx].append(x)# coloca que fx vai para x

medeCaminho(fxs, atual, final)# faz os testes empilhando para ve se encontra o caminho
