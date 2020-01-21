tamanho = int(input())
listaPecas = list(map(int, input().split()))
somaCerta = (tamanho * (1 + tamanho))/2
print(int(somaCerta - sum(listaPecas)),end="")
