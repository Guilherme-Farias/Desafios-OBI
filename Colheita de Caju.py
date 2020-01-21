#pega a entrada
#vai armazenar os dados da colheita
#vai fazer as somas e armazenar para n ter que fazer dnv por exemplo de entrada
# 3 3 2 2
# 1 2 3
# 4 5 6
# 7 8 9
#ele faz a soma 1+2+4+5 e passa para o 2+3+4+5 so que ao inves de somar tudo dnv ele subtrai 1 + 4 e soma com o 3 + 6
#faz o tamanho da matriz de todas as somas com uma borda, pois as vezes o i ou c vai dar negativo e em python isso faz voce ir para os ultimos numeros do indice
#pega entradas e organiza o que já foi dito antes


valor_colheita_maximo = 0
linhas, colunas, tamanho_linha,tamanho_coluna = map(int, input().split())
matriz = []
soma = []

soma.append(list(0 for x in range(colunas + 2)))
for linha in range(linhas):
    matriz.append(list(map(int,input().split())))
    soma.append(list(0 for x in range(colunas + 2)))
soma.append(list(0 for x in range(colunas + 2)))


for linha in range(1, linhas + 1):
    for coluna in range(1,colunas + 1):
        soma[linha][coluna] = soma[linha - 1][coluna] + soma[linha][coluna - 1] - soma[linha - 1][coluna - 1] + matriz[linha - 1][coluna - 1]

        

for linha in range(tamanho_linha, linhas + 1):
    for coluna in range(tamanho_coluna, colunas + 1):
        ponto = soma[linha][coluna] - soma[linha - tamanho_linha][coluna] - soma[linha][coluna - tamanho_coluna] + soma[linha - tamanho_linha][coluna - tamanho_coluna]
        if ponto > valor_colheita_maximo:
            valor_colheita_maximo = ponto

print(valor_colheita_maximo)
    
