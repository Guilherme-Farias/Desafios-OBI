while True:
    LinhasDaMatriz, ColunasDaMatriz, intrucao = map(int, input().split())
    if LinhasDaMatriz == 0 and ColunasDaMatriz == 0 and intrucao == 0: break
    matriz = []
    figurinhas = 0
    for linha in range(LinhasDaMatriz):
        matriz.append("_".join(input()).split("_"))
        if "N" in matriz[linha] or "S" in matriz[linha] or "L" in matriz[linha] or "O" in matriz[linha]:
            if "N" in matriz[linha]:
                x, y = linha, matriz[linha].index("N")
                frente = 0
            elif "S" in matriz[linha]:
                x, y = linha, matriz[linha].index("S")
                frente = 2
            elif "L" in matriz[linha]:
                x, y = linha, matriz[linha].index("L")
                frente = 1
            elif "O" in matriz[linha]:
                x, y = linha, matriz[linha].index("O")
                frente = 3
    movimentos = input()
    for movimento in movimentos:
        if movimento == "D":
            frente += 1
            if frente == 4: frente = 0
        elif movimento == "E":
            frente -= 1
            if frente == -1: frente = 3
        elif movimento == "F":
            if frente == 0:
                #norte
                if x != 0 and matriz[x - 1][y] != "#":
                    x -= 1                       
            elif frente == 3:
                #oeste
                if y != 0 and matriz[x][y - 1] != "#":
                    y -= 1               
            elif frente == 2:
                #sul
                if x != LinhasDaMatriz - 1 and matriz[x + 1][y] != "#":
                    x +=1 
            else:
                #leste
                if y != ColunasDaMatriz - 1 and matriz[x][y + 1] != "#":
                    y += 1
            if matriz[x][y] == "*":
                figurinhas+=1
                matriz[x][y]="."
    print(figurinhas)
