from math import sqrt
CO = float(input('Qual é o cateto oposto ?'))
CA = float(input('Qual é o cateto adjacente ?'))
HI = sqrt(CO**2+CA**2)
# HI = (CO**2+CA**2)**(1/2) --- > SEM IMPORTAÇÃO
# HI = math.hypot(CO,CA) ---- > OUTRA DE SE FAZER
print(' O comprimento do cateto oposto é {}\n O comprimento do cateto adjacente é {}\n O comprimento da hipotenusa é {:.4f}'.format(CO,CA,HI))


