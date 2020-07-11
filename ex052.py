'''n = int(input("Escreva um número: "))
if n //n == 1 and n // n == 1:
    print("Esse número é primo!")
else:
    print("Esse número não é primo")'''

núm = int(input("Digite um número: "))
tot = 0 # Não entendi muito bem !
for c in range(1,núm + 1):
    if núm % c == 0:
      print("\033[1;34m", end=" ")
      tot += 1
    else:
        print("\33[1;31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[33mO número {} foi divisível {} vezes".format(núm,tot)) # (\n) É uma quebra de texto !
if tot == 2:
    print("E por isso ele É PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")

