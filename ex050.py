'''s = 0
for c in range (1+1, 7, 2):
    print("Os pares são: {}".format(c))
    s = s + c # S += C -> é A MESMA COISA
print("A soma total é {}".format(s))'''

soma = 0 # Contador
cont = 0# Acumulador
for c in range (1,7):
    num = int(input("Digite o {} valor: ".format(c)))
    if num % 2 ==0:
        soma += num
        cont += 1
print("Você informou {} números PARES e a soma foi {}".format(cont, soma))
