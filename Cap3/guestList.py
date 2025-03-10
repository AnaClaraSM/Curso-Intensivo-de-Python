# EXERCÍCIO 3.4: Crie uma lista de convidados para um jantar e exiba uma mensagem de convite a cada pessoa.

print(f"É com prazer que queremos anunciar a organização de um jantar de comemoração aos 10 anos do setor 9 de TI em nossa empresa. Conseguimos uma mesa com lugar para 6 dos nossos queridos funcionários. Os convidados serão notificados em breve.")
print()

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
print()


# EXERCÍCIO 3.7: Remova os convidados da lista até sobrarem dois, envie mensagens, depois esvazie a lista

# Exibe aviso de redução de lugares
print(f"Lamentamos muito em informar que nossa mesa não chegará a tempo, e agora poderemos chamar somente dois dos convidados previstos. Pedimos sinceras desculpas a todos, em especial aos que não poderão comparecer.")

# Exibe lista inicial
print(f"Lista Incial: {convidados}") # 9 convidados

# Remoção dos convidados e aviso

convidado_removido = convidados.pop() #Restam 8
print(f"Olá {convidado_removido}. É com tristeza que informamos que não poderemos mais ter-lhe em nosso jantar. Pedimos desculpas e esperamos poder compensar em uma próxima oportunidade.")
print()

convidado_removido = convidados.pop() #Restam 7
print(f"Olá {convidado_removido}. É com tristeza que informamos que não poderemos mais ter-lhe em nosso jantar. Pedimos desculpas e esperamos poder compensar em uma próxima oportunidade.")
print()

convidado_removido = convidados.pop() #Restam 6
print(f"Olá {convidado_removido}. É com tristeza que informamos que não poderemos mais ter-lhe em nosso jantar. Pedimos desculpas e esperamos poder compensar em uma próxima oportunidade.")
print()

convidado_removido = convidados.pop() #Restam 5
print(f"Olá {convidado_removido}. É com tristeza que informamos que não poderemos mais ter-lhe em nosso jantar. Pedimos desculpas e esperamos poder compensar em uma próxima oportunidade.")
print()

convidado_removido = convidados.pop() #Restam 4
print(f"Olá {convidado_removido}. É com tristeza que informamos que não poderemos mais ter-lhe em nosso jantar. Pedimos desculpas e esperamos poder compensar em uma próxima oportunidade.")
print()

convidado_removido = convidados.pop() #Restam 3
print(f"Olá {convidado_removido}. É com tristeza que informamos que não poderemos mais ter-lhe em nosso jantar. Pedimos desculpas e esperamos poder compensar em uma próxima oportunidade.")
print()

convidado_removido = convidados.pop() #Restam 2
print(f"Olá {convidado_removido}. É com tristeza que informamos que não poderemos mais ter-lhe em nosso jantar. Pedimos desculpas e esperamos poder compensar em uma próxima oportunidade.")
print()

# Aviso aos convidados restantes

print(f"Olá {convidados[0]}! Gostaríamos de informar que você permanece em nossa lista de convidados! Esperamos que possa aproveitar o jantar ao máximo.")

print(f"Olá {convidados[1]}! Gostaríamos de informar que você permanece em nossa lista de convidados! Esperamos que possa aproveitar o jantar ao máximo.")


# Exibe lista final
print(f"Lista Final: {convidados}") # 2 convidados


# Esvazia a lista -> convidados.clear() ou = [] são possibilidades
# del convidados[0] 
# del convidados[1] #Erro -> ao remover o 0 primeiro, o elemento de posição 1 é deslocado para a posição 0, eliminando o índice 1
del convidados[1]
del convidados[0] 

# Exibe lista esvaziada
print(f"Lista de Convidados: {convidados}")