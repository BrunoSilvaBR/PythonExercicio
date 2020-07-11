'''for c in range(2,21,2):
    print(c)'''

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10 - 1) * razão
for c in range (primeiro,décimo + razão, razão):
    print("{}".format(c), end=" > ")
print("ACABOU")

