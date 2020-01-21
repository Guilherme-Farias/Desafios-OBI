senha = input()
texto = input()
alfabeto, solucao = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], ""
for letra in texto:
    solucao += alfabeto[senha.find(letra)]
print(solucao)
