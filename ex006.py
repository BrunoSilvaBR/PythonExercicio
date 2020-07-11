n = int(input('Coloque um número !'))
d = n * 2
t = n * 3
q = n ** (1/2)
print("\033[31mO número é\033[m \033[34m{}\033[m \033[31m, O seu dobro é\033[m \033[34m{}\033[m \033[31m, o seu triplo é\033[m \033[34m{}\033[m\033[31m, A sua raiz quadrada é\033[m\033[34m{:.2f}\033[m".format(n,d,t,q))
# Posso usar no format a operação direta, " . format(n,(n*2),(n*3),(n**(1/2)))
# A potência pode ser usada com " pow(n,(1/2))
