'''n = int(input("Você viajo quantos Km?"))
d = 10
if n >=200:
    print("Você viajou {}km".format(n))
    print("Você vai pagar{}R$!".format(d))
else:
    print("Você viajou {}km".format(n))
    print("Você vai pagar{}R$!".format(d))'''

'''distância = float(input("Qual é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}Km".format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância* 0.45
print("É o preço da sua pasagem é de R${:.2f}".format(preço))'''

distância = float(input("Qua é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}Km".format(distância))
preço = distância * 0.50 if distância <=200 else distância * 0.45
print("E o preço da sua passagem será de R${:.2f}".format(preço))

    

