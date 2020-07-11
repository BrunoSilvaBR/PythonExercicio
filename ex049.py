'''n = int(input("Escolha um número! "))
for c in range (1,11):
    calculadora = n * c
    print(calculadora)'''

num = int(input("Digite um número para ver sua tabuada: "))
for c in range(1,11):
    print("{} x {} = {}".format(num, c, num*c))
