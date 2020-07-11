n = int(input('\033[31mDigite um Valor :\033[m'))
n1 = int(input('\033[31mDigite outro Valor :\033[m'))
x = n1 + n
#print ('A soma entre {} e {} é igual a {}'.format(n,n1,x))
print (f'\033[32mA soma entre \033[31m{n}\033[m \033[32me\033[m \033[31m{n1}\033[m \033[32mé igual a : \033[31m{n+n1}\033[m')

