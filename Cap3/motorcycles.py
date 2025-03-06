# Cria lista de motos
motorcycles = ["ducati", "yamaha", "suzuki"]
print(motorcycles)

# Modifica o elemento da posição 0
motorcycles[0] = "honda"
print(motorcycles)

# Adiciona um elemento no final da lista
motorcycles.append("ducati")
print(motorcycles)

# Limpa a lista
motorcycles = []
print(motorcycles)

# Adiciona elementos a lista com append()
motorcycles.append("honda")
print(motorcycles)
motorcycles.append("yamaha")
print(motorcycles)
motorcycles.append("suzuki")
print(motorcycles)

# Insere um elemento em uma posição específica da lista (deslocando à direita os elementos seguintes, se necessário)
motorcycles.insert(0, "ducati") # lista.insert(indice, elemento)
print(motorcycles)
motorcycles.insert(2, "harley")
print(motorcycles)
motorcycles.insert(-1, "harley") #Não vai para o final -> Colocou o elemento novo no lugar em que estava o último (4) e deslocou este para a direita (5)
print(motorcycles)
motorcycles.insert(8, "royal") #Adiciona no fim (índice não ocupado/ não existente) -> adiciona no fim (primeiro índice inexistente) e não necessariamente no 8
print(motorcycles)

# Deleta um elemento de uma posição específica da lista (sem possibilidade de acesso posterior)
del motorcycles[0] #Deletar elemento da posição 0 da lista motorcycles
print(motorcycles)
# deletedOne = (del motorcycles[0]) #nem é possível atribuir

# Remove o último elemento da lista, com possibilidade de acesso ao item posteriormente
popped_motorcycles = motorcycles.pop() #remove o valor da lista e o armazena em uma variável
print(motorcycles)
print(popped_motorcycles)
print(f"Você removeu '{popped_motorcycles.title()}'") # Permite trabalhar o valor removido e exibir detalhes em mensagens, por exemplo

# Remove um elemento de uma posição específica da lista, com possibilidade de acesso ao item posteriormente
first_owned = motorcycles.pop(0) #lista.pop(indice)
print(motorcycles)
print(first_owned)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# Remove um elemento pelo seu valor, ao invés da posição
motorcycles.remove("harley")
print(motorcycles) #Remove apenas a primeira ocorrência do valor (para remover todas requer loop)
# Permite salvar e trabalhar com o valor posteriormente
given_motorcycle = "suzuki"
motorcycles.remove(given_motorcycle)
print(motorcycles)
print(f"My {given_motorcycle.title()} was given away.")


# removed_motorcycle = motorcycles.remove("suzuki")
# print(removed_motorcycle) # -> None

# Após a remoção, os elementos são automaticamente deslocados, se necessário