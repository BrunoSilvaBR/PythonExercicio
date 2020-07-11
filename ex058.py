from random import randint
computador = randint(1,5)
print("Descubra o que o computador está pensando")
n = False
while not n:
    jogador = int(input("Escolha um número!"))
    if computador == jogador:
        n = True
    elif computador != jogador:
        print("Você erro")
        if computador > jogador:
            print("Maior")
        elif computador < jogador:
            print("Menor")
print("Fim!")
