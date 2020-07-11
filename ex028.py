'''from random import uniform
p = int(input("Escreva um número de 0 a 5! "))
n = int(uniform(0, 6))
#print("O número é {}".format(n))
if p == n:
    print("Você Acerto o número!")
    print("Parabéns!")
else:
    print("Você ERRO o número!")
    print("Boa Sorte na proxima!")
    print("O número era {}.".format(n))'''

from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "pensar"
print("-=-" * 20)
print("Vou pensar em um númeo entre 0 e 5. Tente adivinhar ...")
print("-=-" * 20)
jogador = int(input("Em que número pensei?")) # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("Parabéns! Você conseguiu me vencer")
else:
    print("Ganhei! Eu pensei no número {} e não no {}!".format(computador,jogador))









