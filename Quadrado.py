tamanho = int(input())
matriz = []
comparadorLinha = []
colunas = [[] for x in range(tamanho)]
for entrada in range(tamanho):
    matriz.append(list(map(int,input().split())))
    comparadorLinha.append(sum(matriz[entrada]))
    for coluna in range(tamanho):
        colunas[coluna].append(matriz[entrada][coluna])
comparadorColuna = []
for coluna in range(tamanho):
    comparadorColuna.append(sum(colunas[coluna]))

    
if comparadorLinha.count(max(comparadorLinha))==1:
    somaErrada = max(comparadorLinha)
    somaCerta = min(comparadorLinha)
    linhaErrada = comparadorLinha.index(somaErrada)
else:
    somaCerta = max(comparadorLinha)
    somaErrada = min(comparadorLinha)
    linhaErrada = comparadorLinha.index(somaErrada)
    
if comparadorColuna.count(max(comparadorColuna))==1:
    colunaErrada = comparadorColuna.index(max(comparadorColuna))
else:
    colunaErrada = comparadorColuna.index(min(comparadorColuna))

errado = matriz[linhaErrada][colunaErrada]
certo = errado + somaCerta - somaErrada
print(certo,errado)
