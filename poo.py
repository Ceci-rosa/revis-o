with open("presenca.txt", "w") as arquivo:
    while (nome := input("Nome do aluno (ou 'fim' para encerrar): ")) != "fim":
        arquivo.write(nome + "\n")
print("Lista de presença:")
with open("presenca.txt") as arquivo:
    print(arquivo.read())

with open("produtos.txt", "w") as arquivo:
    for _ in range(int(input("Quantos produtos deseja cadastrar? "))):
        nome = input("Produto: ")
        preco = float(input("Preço: "))
        arquivo.write(f"{nome},{preco}\n")
print("Conteúdo do arquivo produtos.txt:")
with open("produtos.txt") as arquivo:
    print(arquivo.read())

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    def exibir(self):
        print(f"{self.nome}, {self.cargo}, R${self.salario:.2f}")
funcionarios = [Funcionario(input("Nome: "), input("Cargo: "), float(input("Salário: "))) for _ in range(3)]
print("Funcionários cadastrados:")
for f in funcionarios:
    f.exibir()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

pessoas = []
for _ in range(2):
    pessoas.append(Aluno(input("Nome do aluno: "), int(input("Idade: ")), input("Matrícula: ")))
for _ in range(2):
    pessoas.append(Professor(input("Nome do professor: "), int(input("Idade: ")), float(input("Salário: "))))

print("Dados cadastrados:")
for p in pessoas:
    if isinstance(p, Aluno):
        print(f"Aluno: {p.nome}, Idade: {p.idade}, Matrícula: {p.matricula}")
    else:
        print(f"Professor: {p.nome}, Idade: {p.idade}, Salário: R${p.salario:.2f}")
