'''primeira = int(input("Qual é o termo? "))
razão = int(input("Qual é a razão? "))
conta = primeira * (10 - 1) * razão
while primeira  != conta:
    print("O termo é {} a razão é {} e a progressão é {}".format(primeira, razão, conta))
    n = str(input("você quer continuar ?")).strip().upper()
    if n == "S":
        primeira = int(input("Qual é o termo?"))
    else:
        print("Fim")
print("Fim")'''

print("Gerador de PA")
print("-="*10)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} ->".format(termo), end="")
    termo = termo + razão
    cont +=1
print("Fim")


