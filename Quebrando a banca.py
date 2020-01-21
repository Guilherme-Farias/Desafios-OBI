while True:
    try:
        quantidade, vaiTirar = map(int, input().split())
        lista = " ".join(input()).split(" ")
        inicio = 0
        fim = quantidade - (quantidade - vaiTirar)
        numeroFinal = ""
        pulei = 0
        while len(numeroFinal) != quantidade - vaiTirar:
            maior = max(lista[inicio:fim + 1])
            numeroFinal += maior
            pulei += lista[inicio:fim+1].index(maior) + 1
            inicio = pulei
            fim +=1
        print(numeroFinal)
    except EOFError:
        break
