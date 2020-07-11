'''from random import randrange
#n = str(input("papel, tesoura ou  pedra?")).strip()
jogo = randrange ('papel','tesoura','pedra')
print("O computador escolheu {}".format(jogo))
n1 = "papel" < "tesoura" and "papel" > "pedra"
n2 = "tesoura" > "papel" and "tesoura" < "pedra"
n3 = "pedra" > "tesoura" and "pedra" < "papel"
if n1 == jogo or n2 == jogo or n3 == jogo:
    print("Isso foi um empate")
if n1 > n2 and n3:
    print("Papel ganho")
elif n2 > n1 and n3:
    print('Tesoura ganho')
else:
    print("Pedra ganho")'''

from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO !!!")
print("-=" * 11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-=" * 11)
if computador == 0:#computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCEU")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1:#computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2:#computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")

    else:
        print("JOGADA INVÁLIDA")
'''print("O computador escolheu {}".format(itens[computador]))#Ele escreve os itens e faz um sorteio'''



