'''from time import sleep
print("Contagem regressiva")
for c in range (10,0,-1):
    sleep(1)
    print(c)
print("\033[1;31mFeliz Ano Novo! \033[m")'''

from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print("Acabou")
print("Bum! Bum! POOOW!")

