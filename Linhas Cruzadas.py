#inversão é tu achar uma tupla dada por uma comparação - (x,y) tal que x>y
#quando o merge joga o elemento da partição da direita para a esquerda
#é porque ele achou um x>y então para todo elemento que resta na partição da esquerda x<=y

#básicamente nós contamos todas as inversões feitas em todas as partições, pois se observar cada inversão na lista seria para deixar as "retas não se cruzarem", logo se as retas não se cruzam é pq n vai ter inversão e está em ordem
#fazemos o merge para ver se está ordenado ou não, e odenar vendo quantas vezes é necessário inverter (x,y) sendo x>=y

def Merge(l):
    global inv#coloca a variavel para sempre ser levada 
    if len(l) > 1:#menor sessão possível
        meio = len(l)//2#divide sessão
        filho_direita = l[meio:]
        filho_esquerda = l[:meio]

        Merge(filho_esquerda)#vai até só ter um elemento//Sempre será maior ou igual em tamanho
        Merge(filho_direita)#vai até só ter um elemento

        vetorL = 0
        vetorR = 0

        sessao = 0#vai colocando os valores na ordem

        for vetorL in range(len(filho_esquerda)):#ve cada item da esquerda
            while vetorR < len(filho_direita) and filho_esquerda[vetorL] > filho_direita[vetorR]:#compara com o da direita, caso seja maior, troca
                l[sessao] = filho_direita[vetorR]
                vetorR += 1
                sessao += 1
                inv += len(l)//2 -vetorL 
            l[sessao] = filho_esquerda[vetorL] #independete de ser maior ou não o filho da esquerda sempre será colocado após a primeira pergunta   
            sessao += 1

        while vetorR < len(filho_direita):#quando acabar o vetorL ele continua colocando o resto do vetorR
            l[sessao] = filho_direita[vetorR]
            vetorR += 1
            sessao += 1
    return inv#retorna o valor de inv para ser printado

inv = 0
entrada = int(input())
print(Merge(list(map(int, input().split()))))
