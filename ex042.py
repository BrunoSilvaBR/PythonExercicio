'''r1 = int(input("Qual é o comprimento do reta 1?"))
r2 = int(input("Qual é o comprimento da reta 2?"))
r3 = int(input("Qual é o comprimento da reta 3?"))
print("=="*20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1: # Comprimento forma um triângulo ?
    print("Essas retas podem formar um triângulo!")
    print("==" * 20)
    # Tipo de triângulo
    if r1 == r2 and r1 == r3:
        print("Esse triângulo é Equilátero!")
    elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r3 == r1 and r3 != r2:
        print("Esse triângulo é Isósceles!")
    else:
        r1 != r2 and r1 != r3 or r2 != r3 and r2 != r1 or r3 != r1 and r3 != r2
        print("Esse Triângulo é Escaleno!")
else:
    print("Essas retas não podem formar um triângulo!")'''

r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo " , end='')
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")



