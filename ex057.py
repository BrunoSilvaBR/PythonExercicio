n = str(input("Qual é o seu sexo? [M] ou [F]?")).strip().upper()[0]
while n not in "FM":
    n = str(input("Qual é o seu sexo? [M] ou [F]")).strip().upper()[0]
print("Ele é {}".format(n))









