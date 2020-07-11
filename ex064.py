'''s = "S"
c = int(input("Escreva um número:"))
while c !=999:
    c = c + 1
    s = str(input("Você quer continuar?"))
    if s == "S".strip().upper():
        c = c + 1
        print("A soma dos termos é {}".format(c))
    else:
        print("Fim") '''

núm = cont = soma = 0
núm = int(input("Digite um número [999 para parar]:"))
while núm != 999:
    soma += núm
    cont +=1
    núm = int(input("Digite um número [999 para parar]:"))
print("Você digitou {} números e a soma entre eles foi {}".format(cont, soma))
