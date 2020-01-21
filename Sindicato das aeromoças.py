
def menorMaiorCaminho(matriz, distancias, visitados):
  for k in range(len(distancias)):
      distancias[k] = 0
      while True:
          if True not in visitados:
              break
          noAtual = 0
          andou = float('inf')
          for i,k in enumerate (distancias):
              if visitados[i]==True:
                  if k < andou:
                      andou = k
                      noAtual = i
          visitados[noAtual]= False
          for i,k in enumerate (matriz[noAtual]):
              if k[0]=="x":
                  peso = k.split()
                  if distancias[noAtual]+int(peso[1])<distancias[i]:
                      distancias[i]= distancias[noAtual]+int(peso[1])
      finalList.append(max(distancias))
      for i in range(len(visitados)):
          visitados[i]= True
          distancias[i] = float('inf')


          
inp = list(map(int, input().split()))
matriz = []
visitados= []
linhas = inp[0]
distancias = []
for k in range(linhas):
    matriz.append([False]*linhas)
    visitados.append(True)
    distancias.append(float('inf'))


    
for i in range(linhas):
    for j in range(linhas):
        matriz[i][j] = "0"

        
for i in range(inp[1]):
    inp2 = list(map(int, input().split()))
    text = str(inp2[2])
    matriz[inp2[1]][inp2[0]]="x "+text
    matriz[inp2[0]][inp2[1]]="x "+text

    
finalList = []
menorMaiorCaminho(matriz, distancias, visitados)


minimo = float('inf')
for menor in finalList:
  if menor < minimo:
    minimo = menor
print(minimo)
