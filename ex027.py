'''n = str(input("Qual é o seu nome:")).strip()
n1 = n.split()
print("O seu primeiro nome é {}".format(n1[0], len(n1[0])))
print("O seu último nome é {}".format(n1[99], len(n1[99])))'''

n = str(input("Qual é o seu nome:")).strip()
nome =n.split()
print("Muito prazer em te conhecer!")
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[-1])) #Posso, colocar sem o len
#print('O seu último nome é {}'.format(nome[len(nome)-1]))






