casa = int(input("Qual é o valor da casa?"))
salario = int(input("Qual é o seu salario?"))
periodo = int(input("Quantos anos você vai pagar a casa?"))
mínimo = salario * 30 /100
prestação = casa / (periodo*12)
if prestação <= mínimo:
    print("O seu emprestimo foi aprovado!")
else:
    print("O seu emprestimo NÃO foi aprovado!")
print("O valor do coeficiente de finaciamento é {}".format(prestação))
print("O valor do salário é {}".format(salario))

'''casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento?"))
prestação = casa / (anos*12)
minimo = salario * 30 /100
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa,anos), end='')
print("a prestação será de R${:.2f}".format(prestação))
if prestação <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
print("Comparando tem que pagar {} eo mínimo é {}".format(prestação,minimo))'''








