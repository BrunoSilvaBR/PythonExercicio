'''import random
n = random.sample(['João','Felipe','Paulo','Renato'],k= 4)
print('Os nomeados são {}'.format(n))'''

from random import sample , shuffle
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1,n2,n3,n4]
shuffle(lista)
print("A ordem dos alunos é: {}".format(lista))

'''lista = sample([n1,n2,n3,n4], k= 4)
print("A ordem dos alunos é: {}".format(lista))'''

