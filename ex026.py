'''n = str(input("Digite seu nome"))
frase = n
frase.count("a")
frase.find("a")'''

n = str(input("Digite uma frase:")).upper().strip()
print("A letra a aparece {} vezes na frase".format(n.count('A')))
print("A primeira letra A apareceu na posição {}".format(n.find('A')+1))
print("A última letra A apareceu na posição {}".format(n.rfind('A')+1))









