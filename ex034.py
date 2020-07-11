'''n = int(input("Quanto você ganha?"))
if n >=1250:
    s = n * 0.1
    f = s + n
    print("O seu salário é:{}".format(f))
else:
    b = n * 0.15
    d = b + n
    print("O seu salario é:{}".format(d))
print("--Fim--")'''

salário = float(input("Qual é o salário do funcionário? R$"))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora".format(salário,novo))






