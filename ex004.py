n = input('\033[31mDigite algo :\033[m')
print('\033[32mO tipo primetivo é :\033[m', type(n))
print('\033[33mSó tem espaço :\033[m', n.isspace())
print('\033[34mEle é Deciamal ? \033[m', n.isdecimal())
print('\033[35mEle é um Número ?\033[m', n.isnumeric())
print('\033[36mEle é alfabético ? \033[m', n.isalpha())
print('\033[37mEle é letra Maiscúla ?\033[m', n.isupper())
print('\033[4;43mEle está em Minucúla ?\033[m', n.islower())
print('\033[7;42mEle está capitalizada ? \033[m', n.istitle())







