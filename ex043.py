'''peso = float(input("Qual é o seu peso?KG"))
altura = float(input("Qual é a sua altura?M"))
calculo = peso / (altura * altura)
print("O seu IMC É {}".format(calculo))
print("="*20)
if calculo <= 18.5:
    print("Você está Abaixo do Peso!")
elif calculo <=25:
    print("Você está no peso Ideal!")
elif calculo <=30:
    print("Você está com Sobrepeso")
elif calculo <= 40:
    print("Você está com Obesidade")
else:
    print("Você está com Obesidade Mórbida")'''

peso = float(input("Qual é o seu peso? (Kg)"))
altura = float(input("Qual é sua altura? (m)"))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO DO PESO Normal")
elif 18.5 <= imc < 25:
    print("PARABÉNS, você está na faixa de PESO NORMAL")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO")
elif 30 <= imc < 40:
    print("VocÊ está em OBESIDADE, Cuidado!")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA,Cuidado")









