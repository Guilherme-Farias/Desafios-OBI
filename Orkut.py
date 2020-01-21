class Node:
    def __init__(self, key, prox = None, ant = None):
        self.key = key
        self.nextNo = prox
        self.antNo = ant
    
    def getData(self):
        return self.key
    
    def getNextNode(self):
        return self.nextNo
        
    def setNextNode(self,valor):
        self.nextNo = valor;

class List:
    def __init__(self, x = None, y = None):
        self.raiz = x
        self.final = y
    
    def __len__(self):
        noatual = self.raiz
        cont = 0
        while noatual is not None:
            cont += 1
            noatual = noatual.getNextNode()
        return cont

    def chegafila(self, value):
        novono = Node(value)
        if self.isEmpty() == True:
            self.raiz = self.final = novono
        else:
            self.final.setNextNode(novono)
            self.final=novono
            
    def andaFila(self):
        if self.isEmpty() == True:
            return None
        raizValue = self.raiz.getData()
        if self.raiz is self.final:#só tinha uma pessoa na fila
            self.raiz = self.final = None
        else:
            self.raiz = self.raiz.getNextNode()
        return raizValue
        
    def isEmpty(self):
        return self.raiz == None

    def getraiz(self):
        return self.raiz

class Fila(List):
    def pop(self):
        return self.andaFila()
    def push(self,data):
        self.chegafila(data)

    
n = int(input())#primeira entrada
test = 0#marcador
while True:#um while que só para com 0 no    
    posicao = {}
    dependencia = {}   
    fila = Fila()
    test += 1  
    resp = []

    nomes = list(input().split())

    for i in range(n):
        posicao[nomes[i]] = []
        dependencia[nomes[i]] = 0
    for i in range(n):
        entrada = input().split()
        querAdicionar = entrada[0]
        friends = entrada[2:]
        dependencia[querAdicionar] += int(entrada[1])
        for friend in friends:
            posicao[friend].append(querAdicionar)
    for i in range(n):
        if (dependencia[nomes[i]] == 0) and True:
            fila.push(nomes[i])
    while len(fila) > 0:
        u = fila.pop()
        resp.append(u)
        for filho in posicao[u]:
            dependencia[filho] -= 1
            if (dependencia[filho] == 0) and True:
                fila.push(filho)
    print("Teste {}".format(test))
    if len(resp) == n: print(*resp)
    else: print("impossivel")
    n = int(input())
    if (n != 0): print()
    else: break
