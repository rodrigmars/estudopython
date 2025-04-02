# -------------------------
# 1 - Variáveis

a = 10  # int
b = 15  # int
c = 2.5  # float
d = "0.15"  # str
e = True  # bool

total = a + b + c + float(d) + e

print("total:", total)

# -------------------------
# A função input() do Python permite que o programador receba dados do utilizador.
# É uma função incorporada na linguagem Python, ou seja, não é
# necessário instalar ou importar para usá-la.

a = input("Informe valor 1:")
b = input("Informe valor 2:")
c = input("Informe valor 3:")

total = a + b + c

print("total:", total)

# -------------------------

nome = "Matheus Vicente Lima"
cpf = "302.940.171-51"
rg = "37.118.623-7"
data_nascimento = "18/02/1981"
sexo = "Masculino"
celular = "(27) 98672-4102"
email = "matheus_lima@lins.net.br"
senha = "zctUwLF70x"

print("nome:", nome)
print("cpf:", cpf)
print("rg:", rg)
print("data_nascimento:", data_nascimento)
print("sexo:", sexo)
print("celular:", celular)
print("email:", email)
print("senha:", senha)
print()

# -------------------------
# Função é um bloco de código que realiza uma tarefa específica.
# As funções são essenciais para organizar e reutilizar código,
# tornando os programas mais legíveis e fáceis de manter.


def buscar_email_senha(email, senha):

    return email, senha


email, senha = buscar_email_senha("rdo@gmail", "teste001")

print("email:", email)
print("senha:", senha)
print()


def soma_valores(a, b):

    total = a + b
    return total


total = soma_valores(2, 2)

print("total:", total)

# -------------------------
# Vetor é uma estrutura de dados que armazena uma sequência
# de elementos do mesmo tipo. Os vetores são uma forma eficiente de
# armazenar e manipular dados

vetor_de_numeros_int = [5, 10, 15, 20, 25, 30, 35, 40, 45]

print("vetor_numeros:", vetor_de_numeros_int[0])
print("vetor_numeros:", vetor_de_numeros_int[1])
print("vetor_numeros:", vetor_de_numeros_int[2])
print("vetor_numeros:", vetor_de_numeros_int[3])
print("vetor_numeros:", vetor_de_numeros_int[4])
print("vetor_numeros:", vetor_de_numeros_int[5])
print("vetor_numeros:", vetor_de_numeros_int[6])
print("vetor_numeros:", vetor_de_numeros_int[7])
print("vetor_numeros:", vetor_de_numeros_int[8])

# -------------------------
vetor_de_numeros_int = [5, 10, 15, 20, 25, 30, 35, 40, 45]

total = vetor_de_numeros_int[0]

for elemento in vetor_de_numeros_int:

    if total != elemento:
        total = total + elemento

print("total:", total)

# -------------------------
