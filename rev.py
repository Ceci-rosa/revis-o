# Programa para ler 5 números inteiros e exibir o maior e o menor
numeros = []
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
print("Lista completa:", numeros)
print("Maior valor:", max(numeros))
print("Menor valor:", min(numeros))

tarefas = []
while True:
    tarefa = input("Digite uma tarefa (ou 'listar' para ver as tarefas): ")
    if tarefa.lower() == "listar":
        print("Tarefas cadastradas:", tarefas)
        break
    else:
        tarefas.append(tarefa)

alunos = {}
for _ in range(int(input("Quantos alunos deseja cadastrar? "))):
    nome = input("Nome: ")
    nota = float(input("Nota (0 a 10): "))
    alunos[nome] = nota
media = sum(alunos.values()) / len(alunos)
print("Média:", media)
print("Acima da média:", [nome for nome, nota in alunos.items() if nota > media])

produtos = {"maçã": 3.00, "banana": 2.50, "laranja": 4.00, "uva": 5.00, "pera": 6.00}
while True:
    produto = input("Produto (ou 'sair' para encerrar): ")
    if produto == "sair":
        break
    print(f"Preço: R${produtos.get(produto, 'Produto não encontrado.'):.2f}")
