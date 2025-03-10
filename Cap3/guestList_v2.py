# EXERCÍCIO 3.4: Crie uma lista de convidados para um jantar e exiba uma mensagem de convite a cada pessoa.

print(f"É com prazer que queremos anunciar a organização de um jantar de comemoração aos 10 anos do setor 9 de TI em nossa empresa. Conseguimos uma mesa com lugar para 6 dos nossos queridos funcionários. Os convidados serão notificados em breve.")
print()

# Lista de convidados
convidados = ["Will", "Louise", "Carl", "Amelia", "Madson", "Oliver"]

# Mensagem de convite padrão
mensagem_convite = "Estamos organizando um jantar e gostaríamos de contar com a sua presença."

# Exibição da mensagem para cada convidado da lista de convidados
for convidado in convidados:
    print(f"\tOlá, {convidado}! {mensagem_convite}")
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

print(f"\tOlá {convidados[2]}! {mensagem_convite}")
print()


# EXERCÍCIO 3.6: Adicione novos convidados no começo, meio e fim de sua lista, e envie uma mensagem para cada

# Informa encontro de mesa maior
print("Gostariamos de informar, alegremente, que encontramos uma mesa maior para o nosso jantar, com lugares para mais 3 convidados!")

# Adiciona convidado no início da lista
convidados.insert(0, "Sunny")
# Envia mensagem ao convidado
print(f"\tOlá, {convidados[0]}! {mensagem_convite}")

# Adiciona convidado no meio da lista
convidados.insert(3, "Garret")
print(f"\tOlá, {convidados[3]}! {mensagem_convite}")

# Adiciona convidado no final da lista (com repetições "indevidas")
convidados.append("Harold")
convidados.append("Harold")
convidados.append("Harold")

# Remove repetições
convidados.remove("Harold") #Por nome
del convidados[-1] #Por índice

print(f"\tOlá, {convidados[-1]}! {mensagem_convite}")

print()


# EXERCÍCIO 3.7: Remova os convidados da lista até sobrarem dois, envie mensagens, depois esvazie a lista

# Exibe aviso de redução de lugares
print(f"Lamentamos muito em informar que nossa mesa não chegará a tempo, e agora poderemos chamar somente dois dos convidados previstos. Pedimos sinceras desculpas a todos, em especial aos que não poderão comparecer.")


# Remoção dos convidados e aviso de desconvite

mensagem_desconvite = "É com tristeza que informamos que não poderemos mais ter-lhe em nosso jantar. Pedimos desculpas e esperamos poder compensar em uma próxima oportunidade."

# Não percorra uma lista com for enquanto remove elementos dela dentro do for -> erros

# Enquanto houver mais de dois convidados
while len(convidados) > 2:
    # Remove convidado do final e armazena
    convidado_removido = convidados.pop()
    # Informa desconvite
    print(f"\tOlá {convidado_removido}. {mensagem_desconvite}")
print()

# Aviso aos convidados restantes

mensagem_permanencia = "Gostaríamos de informar que você permanece em nossa lista de convidados! Esperamos que possa aproveitar o jantar ao máximo."

# Para cada convidado da lista
for convidado in convidados:
    # Informa a permanência
    print(f"\tOlá {convidado}! {mensagem_permanencia}")
    # Erro de retorno de mensagens apenas para Sunny -> Loop for com convidado[0] ao invés de convidado
print()

# Esvazia a lista
convidados.clear() #clear() -> None

print(f"Lista de Convidados: {convidados}")