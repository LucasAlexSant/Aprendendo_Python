nome = "Lucas"
idade = 19
profissao = "Padeiro"
linguagem = "Python"
saldo =  45.553

dados = {"nome": "Lucas", "idade": 19}

print("Nome: %s Idade: %d" % (nome,idade)) #forma não muito ideal
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}". format(**dados))

print(f"Nome: {nome} idade: {idade}")
print(f"Nome: {nome} idade: {idade} Saldo: {saldo:0.2f}")
print(f"Nome: {nome} idade: {idade} Saldo: {saldo:10.2f}")
