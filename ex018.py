'''import math
n = int(input('Escreva um número qualquer :'))
sin = math.sinh(n)
cos = math.cosh(n)
tag = math.tanh(n)
print('O número é :{}\nO seu seno será:{}\nO seu cosseno será:{}\nA sua tangente será:{}'.format(n,sin,cos,tag))'''

from math import radians,sin,cos,tan
ang = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(ang))
print('O ângulo {} tem o Seno de {:.2f}'.format(ang,seno))
cos = cos(radians(ang))
print('O ângulo {} tem o Cos de {:.2f}'.format(ang,cos))
tang = tan(radians(ang))
print('O ângulo {} tem a Tangente de {:.2f}'.format(ang,tang))





