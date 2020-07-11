'''n =int(input("Qual é o preço do produto?"))
tipo = str(input("Qual é o tipo de pagamento?(dinheiro,cartão,2x e 3x):")).strip()
n1 = n * 0.1
n2 = n * 0.05
n3 = n * 0.2
vista = n - n1
cartao = n - n2
mais = n + n3
if tipo == "dinheiro":
    print("O valor em dinheiro é {}".format(vista))
if tipo == "cartão":
    print("O valor no cartão será {}".format(cartao))
if tipo == "2x":
    print("O preço será {}".format(n))
if tipo == "3x":
    print("O preço será {}".format(mais))'''


'''n = int(input("Preço da compra: R$"))
print(''''''Forma de pagamento 
[1] Á vista dinheiro/cheque
[2] Á vista no cartão
[3] 2x no cartão
[4] 3x no cartão'''''')
n2 = int(input("Qual é a opção ?"))
vista = n * (10/100)
cartao = n * (5/100)
cartao2 = n / (20/100)
if n2 == 1:
    print("O preço a vista será {}".format(vista))
elif n2 == 2:
    print("O preço no cartão será {}".format(cartao))
elif n2 == 3:
    print("O preço em duas vezes será {}".format(n))
elif n2 == 4:
    print("o preço em 3x vezes será {}".format(cartao2))
else:
    print("Opção inválida")'''

print("{:=^40}".format(" LOJAS PREDITEC "))
preço = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int (input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10 /100)
elif opção == 2:
    total = preço - (preço * 5 /100)
elif opção ==3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif opção == 4:
    total = preço + (preço * 20 /100)
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(totalparc, parcela))
else:
    total = preço
    print("\033[1;31mOpção invalida de pagamento. Tente novamente!")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, total))

