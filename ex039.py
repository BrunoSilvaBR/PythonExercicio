'''n = int(input("Qual é a sua idade?"))
conta = (18-n)
if n > 18:
    print("Você já passo da idade para se alistar!")
elif n == 18:
    print("Está na hora de se alistar!")
else:
    print("Você ainda não tem idade mínima para se alistar!")
    print("Ainda falta {} anos".format(conta))'''

from datetime import date# foi visto na aula 8
atual = date.today().year
genero = int(input('''Qual é o seu sexo:
[1] \033[1;34mMasculino\033[m.
[2] \033[1;31mFeminino\033[m.
\033[1;33mDigite:\033[m'''))
if genero ==1:
    print("\033[1;34mAlistamento Obrigatorio!\033[m")
    nasc = int(input("\033[1;33mAno de nascimento: \033[m"))
    idade = atual - nasc
    if idade == 18:
        print("\033[1;34mVocê tem que se alistar:IMEDIATAMENTE!\033[m")
    elif idade < 18:
        saldo = 18 - idade
        print("\033[1;31mVocê ainda não tem 18 anos. Ainda falta {} anos para o alistamento!\033[m".format(saldo))
        ano = atual + saldo
        print("\033[1;33mSeu alistamento será em {}\033[m".format(ano))
    else:
        saldo = idade - 18
        print("\033[1;31mVocê já deveria ter se alistado há {} anos.\033[m".format(saldo))
        ano = atual - saldo
        print("\033[1;31mO seu alistamento foi em:{}\033[m".format(ano))
print("="*20)
#print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
if genero == 2:
    print("\033[1;31mVocê não precisa se alistar!")
elif genero != 1 and genero !=2:
    print("\033[1;31mOpção Inválida\033[m")












