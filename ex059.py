c = 1
n1 = int(input("Qual é o primeiro número? "))
n2 = int(input("Qual é o segundo número? "))
while c !=5:
    print('''Escolha uma das opções :
        [1] Adição
        [2] Multiplicação
        [3] Maior
        [4] Novos números
        [5] Desligar''')
    c = int(input("Qual é o número?"))
    if  c == 1:
        n =  n1 + n2
        print("A soma vai ser {}".format(n))
    elif c ==2:
        n = n1 * n2
        print("A multiplicação vai ser {}".format(n))
    elif c == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("O maior número será {}".format(maior))
    elif c == 4:
        n1 = int(input('Escolha novamente! um número:'))
        n2 = int(input("Escolha novamente! outro número:"))
    elif c == 5 :
        print("Acabo")
    else:
        print("erro")





