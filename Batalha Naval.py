import sys



def verificaNavio(linha, coluna):
    global explodiu
    if matriz[linha][coluna] == "." or matriz[linha][coluna] == "o" \
       or matriz[linha][coluna] == 0:
        return
    if matriz[linha][coluna] == "#":
        explodiu = False
        return
    matriz[linha][coluna] = "o"
    verificaNavio(linha - 1, coluna)
    verificaNavio(linha, coluna + 1)
    verificaNavio(linha + 1, coluna)
    verificaNavio(linha, coluna - 1)


sys.setrecursionlimit(1000000)


linhas, colunas = map(int, input().split())
matriz = []

#qual é melhor ? tamanho ou sem tamanho ?/com cerca por fora ou sem? os if custam mais doq isso ?
tamanho = list(0 for x in range(colunas + 2))
matriz.append(tamanho)
for linha in range(linhas):
    matriz.append([0]+" ".join(input()).split()+[0])
matriz.append(tamanho)



tiros = int(input())
for tiro in range(tiros):
    linha,coluna = map(int, input().split())
    if matriz[linha][coluna] == "#":
        matriz[linha][coluna] = "O"
navioDestruido = 0


for linha in range(1, linhas + 1):
    for coluna in range(1, colunas + 1):
        if matriz[linha][coluna] =="O":
            explodiu = True
            verificaNavio(linha,coluna)
            if explodiu:
                navioDestruido += 1
print(navioDestruido)





