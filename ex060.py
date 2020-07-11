'''n = 1
n1 = int(input("Escreva um numero:"))
while n < n1+1:
    print(n)
    n=n+1   # Uma forma de mudar a sequência
print("Fim")'''

'''from math import factorial # Como modulo
n = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}".format(n,f))'''

n = int(input("Digite um número para calcular seu fatorial: "))
c = n
f = 1
print("Calculando {}!".format(n), end="")
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f = f * c # f*=c
    c -= 1
print("{}".format(f))

