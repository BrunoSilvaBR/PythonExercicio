'''frase = str(input("Escreva seu nome completo:"))
cadeia = frase.split()
print(frase.upper())
print(frase.lower())
print(len(frase.strip()))
print(cadeia[0])'''

nome = str(input("Digite o seu nome completo:")).strip()
print("Analisando seu nome ...")
print("Seu nome em maiúsculo é {}".format(nome.upper()))
print("Seu nome em minusculo é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
#print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
n = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(n[0], len(n[0])))



















