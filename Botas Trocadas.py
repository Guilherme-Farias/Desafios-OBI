def Merge(l):
    if len(l) > 1:
        meio = len(l)//2
        filho_direita = l[meio:]
        filho_esquerda = l[:meio]

        Merge(filho_esquerda)
        Merge(filho_direita)

        vetorL = 0
        vetorR = 0

        sessao = 0

        for vetorL in range(len(filho_esquerda)):
            while vetorR < len(filho_direita) and filho_esquerda[vetorL][0] > filho_direita[vetorR][0]:
                l[sessao] = filho_direita[vetorR]
                vetorR += 1
                sessao += 1
            l[sessao] = filho_esquerda[vetorL]
            sessao += 1

        while vetorR < len(filho_direita):
            l[sessao] = filho_direita[vetorR]
            vetorR += 1
            sessao += 1

N = int(input())
elementos=[]


for elemento in range(N):
    elementos.append(input().split())
Merge(elementos)



index = 0
soma = 0
while index < len(elementos) - 1 :
    E, D = 0, 0
    tamanho = elementos[index][0]
    for item in range(index, len(elementos)):
        if elementos[item][0] != tamanho:
            break
        elif elementos[item][1] == "E":
            E += 1
        else:
            D += 1
    index = item
    
    soma += min(E, D)  
print(soma)
