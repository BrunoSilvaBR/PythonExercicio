'''n1 = 0
while n1 != 4:
    n = int(input("Escreva um número:"))
    n1 = int(input(''''''' Você quer fazer
    [1] Média
    [2] MAIOR
    [3] MENOR
    [4] DESLIGAR
    Digite:''' '''))
    if n1 == 1:
        m = (n + n) / n
        print("A média é {}".format(m))
    elif n2 == 2:
        maior = n > n
        maior = n
        print("o MAIOR É {}".format(maior))
    elif n3 == 3:
        menor = n < n
        menor = n
        print("O MENOR É {}".format(menor))
    else:
        print("Desliga")
print("Fim")'''

resp = "S"
soma = quant = média = maior = menor = 0
while resp in "Ss":
    núm = int(input("Digite um número:"))
    soma +=núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
média = soma / quant
print("Você digitou {} números e a média foi {}".format(quant, média))
print("O maior valor foi {} e o menor valor foi {}".format(maior, menor))

