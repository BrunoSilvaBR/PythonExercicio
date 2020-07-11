n = int(input('Coloque um número !'))
s = n + 1
a = n - 1
#print("O número é {}, Seu antecessor é {} , seu sucessor é {} ".format(n, a, s))
print ('\033[31mO numero é \033[34m{}\033[m\033[31m, Seu antecessor é\033[m \033[34m{}\033[m\033[31m, seu sucessor é\033[m \033[34m{}\033[m'.format(n,(n-1),(n+1)))

