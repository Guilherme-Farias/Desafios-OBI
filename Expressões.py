class NovoNo():
    def __init__(self, data, prox = None, ant = None):
        self._data = data
        self._prox = prox
        self._ant = ant

    def getData(self):
        return self._data

    def getProx(self):
        return self._prox

    def getAnt(self):
        return self._ant

    def setProx(self, data):
        self._prox = data

    def setAnt(self, data):
        self._ant = data
  
class pilhaDLL():
    def __init__(self, inicio=None, fim=None):
        self._inicio = inicio
        self._fim = fim

    def isVazia(self):
        return self._inicio == None

    
    def inserirNoInicio(self, dado):
        novono = NovoNo(dado)
        if not self.isVazia():
            novono.setProx(self._inicio)
            self._inicio.setAnt(novono)
        self._inicio = novono

    def removerDoInicio(self):
        i = self._inicio
        if i is not None:
            if self._inicio.getProx() is not None:
                self._inicio.getProx().setAnt(None)
        self._inicio = self._inicio.getProx()





d = {")": "(", "]": "[", "}": "{"}
a = {0: "N", 1: "S"}
N = int(input())
for i in range(N):
    x = 1
    pilha = pilhaDLL()
    entrada = input()
    for i in entrada:
        if i == "(" or i == "[" or i  == "{":
            pilha.inserirNoInicio(i)
        else:
            if pilha.isVazia():
                x = 0
                break
            else:
                if pilha._inicio._data == d[i]:
                    pilha.removerDoInicio()
                else:
                    x = 0
                    break
    if x == 1:
        if pilha.isVazia():
            x = 1
        else:
            x = 0
    print(a[x])
