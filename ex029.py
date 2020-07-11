'''v = float(input("O carro está em qual velocidade?"))
n = (v - 80)
c = (7 * n)
d = 120
if v > 80:
    print("O seu carro está acima da velocidade permitida")
    print("Você terá que pagar:{} R$ ! ".format(c))
else :
    print("Você está na velocidade permitida!")'''

velocidade = float(input("Qual é a velocidade do carro:"))
if velocidade > 80:
   print("MULTADO! Você excedeu o limite permitido que é de 80KM/h")
   multa = (velocidade-80) * 7
   print("Você deve pagar uma multa de R${:.2f}".format(multa))
print("Tenha um bom dia! Dirija com segurança")


