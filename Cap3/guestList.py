# EXERCÍCIO 3.4: Crie uma lista de convidados para um jantar e exiba uma mensagem de convite a cada pessoa.

# Lista de convidados
convidados = ["Will", "Louise", "Carl", "Amelia", "Madson", "Oliver"]

# Exibe lista
print(f"Convidados: {convidados}")
print()

# Mensagem de convite padrão
mensagem_convite = "Estamos organizando um jantar e gostaríamos de contar com a sua presença."

# Exibição da mensagem para cada convidado
print(f"Olá {convidados[0]}! {mensagem_convite}")
print(f"Olá {convidados[1]}! {mensagem_convite}")
print(f"Olá {convidados[2]}! {mensagem_convite}")
print(f"Olá {convidados[3]}! {mensagem_convite}")
print(f"Olá {convidados[4]}! {mensagem_convite}")
print(f"Olá {convidados[5]}! {mensagem_convite}")
print()
print()


# EXERCÍCIO 3.5: Modifique sua lista, removendo um convidado, adicionando outro e mandando uma mensagem

# Altera o nome de um convidado
convidados[0] = "William"

# Remove o terceiro convidado e armazena
convidado_removido = convidados.pop(2)

# Adiciona um convidado no lugar do ausente
convidados.insert(2, "Sophie")

# Aviso de ausência
print(f"Lamentamos informar que o convidado {convidado_removido} não poderá comparecer ao jantar.") #como alternar o sufixo dependendo do gênero?

# Exibe lista de convidados
print(f"Convidados: {convidados}")
print()

print(f"Olá {convidados[2]}! {mensagem_convite}")
print()


# EXERCÍCIO 3.6: Adicione novos convidados no começo, meio e fim de sua lista, e envie uma mensagem para cada

# Informa encontro de mesa maior
print("Gostariamos de informar, alegremente, que encontramos uma mesa maior para o nosso jantar, com lugares para mais 3 convidados!")

# Adiciona convidado no início da lista
convidados.insert(0, "Sunny")
# Envia mensagem ao convidado
print(f"Olá, {convidados[0]}! {mensagem_convite}")

# Adiciona convidado no meio da lista
convidados.insert(3, "Garret")
print(f"Olá, {convidados[3]}! {mensagem_convite}")

# Adiciona convidado no final da lista (com repetições "indevidas")
convidados.append("Harold")
convidados.append("Harold")
convidados.append("Harold")

# Remove repetições
convidados.remove("Harold") #Por nome
del convidados[-1] #Por índice

print(f"Olá, {convidados[-1]}! {mensagem_convite}")

print()
# Exibe lista de convidados
print(f"Convidados: {convidados}")