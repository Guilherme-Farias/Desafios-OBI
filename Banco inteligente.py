saque = int(input())
l = [[],[],[],[],[],[]]
doisn, cincon, dezn, vinten, cinquentan, cemn = map(int, input().split())
l[0], l[1], l[2], l[3], l[4], l[5] = (2,doisn),(5,cincon),(10,dezn),(20,vinten),(50,cinquentan),(100,cemn)
valor = [1] + [0] * saque

for notas in l:
    ltemp = valor[:]
    qtd = 0
    for i in range(notas[0], saque + 1):
        ltemp[i] += ltemp[i - notas[0]]
        if i < notas[0] * (notas[1] + 1):
            tem_nota = 0       
        else:
            tem_nota = ltemp[i-(notas[0]*(notas[1]+1))]
        valor[i] += ltemp[i- notas[0]] - tem_nota
print(valor[-1])

