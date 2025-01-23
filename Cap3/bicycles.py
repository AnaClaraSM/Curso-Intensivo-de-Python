# Cria uma lista para armazenar nomes de bicicletas e inicializa com 4 elementos
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Imprime a lista
print(bicycles) #A lista é impressa com os colchetes, aspas e todos os elementos
# bicycles sozinho não retorna nada, precisa do print

# Imprime o primeiro elemento da lista
print(bicycles[0]) #Imprime apenas o elemento acessado, sem aspas

# Imprime o primeiro elemento, com letra inicial maiúscula
print(bicycles[0].title())

# Retorna a segunda bicicleta da lista
print(bicycles[1])

# Retorna a quarta bicicleta da lista
print(bicycles[3])

# Retorna o último elemento da lista
print(bicycles[-1])

# Cria uma mensagem com um elemento da lista (usando f-strings)
message = f"My first bicycle was a {bicycles[0].title()}"
# Imprime a mensagem
print(message)