'''n = float(input("Quanto você tiro na P1?"))
n1 = float(input("Quanto você tiro na P2?"))
n2 = float(input("Quanto você tiro na P3?"))
n3 = float(input("Quanto você tiro na P4?"))
media = (n + n1 + n2 + n3) / 4
if media >=7:
    print("Você foi \033[1;34mAPROVADO!")
elif media >=5:
    print("Você está de \033[1;33mRECUPERAÇÃO!")
else:
    print("Você Foi \033[1;31mREPROVADO!")'''

nota1 = float(input("Primeira nota!"))
nota2 = float(input("Segunda nota!"))
media = (nota1 + nota2) / 2
print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1,nota2,media))
if 7 > media >= 5:
    print("O aluno está de RECUPERAÇÃO.")
elif media < 5:
    print("O aluno está REPROVADO.")
elif media:
    print("O aluno está APROVADO.")
