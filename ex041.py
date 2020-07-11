'''idade = int(input("Qual é a sua idade?"))
if idade <=9:
    print("A sua categoria é Mirin")
elif idade <=14:
    print("A sua categoria é Infatil")
elif idade <=19:
    print("A sua categoria é Junior")
elif idade == 20:
    print("A sua categoria é Sênior")
else:
    print("A sua categoria é Master")'''

from datetime import date
atual = date.today().year
nascimento = int(input("Ano de Nascimento:"))
idade = atual - nascimento
print("O atleta tem {} anos".format(idade))
if idade <=9:
    print("Classificação :MIRIM")
elif idade <=14:
    print("Classificação: INFATIL")
elif idade <=19:
    print("Classificação JUNIOR")
elif idade <=25:
    print("Classificação SÊNIOR")
elif idade > 25:
    print("Classificação MASTER")



