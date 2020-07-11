'''programa = int(input("Escreva um número!"))
base = str(input("Qual é a base que você quer?")).strip()
bin = (programa / 7) * 5
octa = (programa / 8) * 3
hexa =  (programa / 9) * 7
if base == "BINARIO" or "Binario" or "binario" or "BINÁRIO" or "Binário" or "binário":
    print("O valor será {}".format(bin))
elif base == "OCTAL" or "octal" or "Octal":
    print("O valor será {}".format(octa))
elif base == "HEXADECIMAL" or "Hexadecimal" or "hexadecimal":
    print("O valor será {}".format(hexa))
else:
    print("Escreva uma das opções!")'''

num = int(input("Digite um número inteiro:"))
print('''Escolha uma das bases para conversão:
[1] converter para Bínario
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int (input("Sua opção:"))
if opção == 1:
    print("{} convertido para Binário é igual a {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido para Octal é igual a {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} convertido para Hexadecimal é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente.")



















