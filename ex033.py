'''n = int(input("Escreva um número: "))
n1 = int(input("Escreva um segundo número: "))
n2 = int(input("Escreva um terceiro número: "))
if n > n1
    print("O número {} é maior!".format(n))
else:
    print("O numero {} é maior!".format(n1))'''

a = int(input("Escreva um número:"))
b = int(input("Escreva um segundo número:"))
c = int(input("Escreva um terceiro número:"))
#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o maior
if b > a and b > c:
    maior = b
if c > a and c > b:
        maior = c
print("O menor valor digitado foi {}".format(menor))
print("O maior valor Digitado foi {}".format(maior))









