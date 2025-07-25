numero = int(input("Informe um número inteiro: "))
if numero % 2 == 0:
    print("O número informado é par!")

elif numero > 0:
    print("O número é maior que zero!")

else:
    print("Onúmero informado é ímpar!")

numero = 0

while numero < 10:
    print("Mostre o número: ", numero)
    numero += 1

print("Saiu da repetição")

numero = 1

while numero <= 100:
    if numero % 2 == 0:
        print(numero)
    numero += 1

for num in range(1, 101, 2):
    print("Mostre o número: ", num)

lista = []

for numero in range(5):
    numero = int(input("Informe um numero inteiros: "))
    lista.append(numero)

    print(lista)
    for item in lista:
        print(item)

        
filmes = {}
nome = input("Informe o nome do filme: ")
ano = int(input("Informe o ano do filme: "))
filmes[nome] = ano

print(filmes)

for nome_filme, ano in filmes.items():
    print("Nome do filme: ", nome_filme)
    print("Ano de Lançamento: ", ano)

nome_filme = input ("Informe o nome do filme que deseja buscar: ")
 
if nome_filme in filmes:
    print("Filme encontrado!")

else:
    print("Filme não encontrado!")

with open("teste_atividade.txt", "w") as arquivo:
    arquivo.write("texto qualquer!!")


with open ("teste_atividade.txt", "r") as arquivos:
    conteudo = arquivo.read()
    print(conteudo)