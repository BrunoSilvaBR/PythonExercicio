'''s = 0
for c in range(1+2,501,3):
    print("O números são {}".format(c))
    s = s + c
print("A soma do números são {}".format(s))'''

cont = 0
soma = 0
for c in range(1,501, 2):
    if c % 3==0:
        soma = soma + c # soma += c Mesma coisa !
        cont = cont + 1 # soma += 1 Mesma coisa !
print("A soma de todos os {} valoras solicitados é {}".format(cont, soma))
