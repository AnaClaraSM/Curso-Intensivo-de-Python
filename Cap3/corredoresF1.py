# Exercício: crie uma lista com o tema que desejar, armazenando diversos exemplos, e use a lista para exibir declarações sobre seus itens.

# Cria a lista com os nomes dos corredores em minúsculas
racers = ["lewis hamilton", "charles leclerc", "max verstappen", "yuki tsunoda", "andrea kimi antonelli", "george russel"]

# Imprime os nomes dos pilotos um por um
# Uso do title() para deixar as iniciais maiúsculas (observe que o title() age em todas as palavras que componhem a string e não só na primeira)
print("Segue abaixo alguns dos corredores da Fórmula 1, Temporada de 2025:")
print(f"\t{racers[0].title()}")
print(f"\t{racers[1].title()}")
print(f"\t{racers[2].title()}")
print(f"\t{racers[3].title()}")
print(f"\t{racers[4].title()}")
print(f"\t{racers[5].title()}")

print() # Linha em branco

# Imprime declarações sobre os corredores
print("Saiba mais sobre os pilotos dessa temporada:")
# Lewis Hamilton
print(f"\t{racers[0].title()}, sete vezes campeão mundial, inicia uma nova fase na Ferrari após longa carreira na Mercedes.")
# Charles Leclerc
print(f"\t{racers[1].title()}, piloto monegasco talentoso, permanece na Ferrari visando conquistar seu primeiro campeonato mundial.")
# Max Verstappen
print(f"\t{racers[2].title()}, tetracampeão mundial, continua liderando a equipe Red Bull Racing em busca de mais títulos.")
# Yuki Tsunoda
print(f"\t{racers[3].title()}, do Japão, continua na Racing Bulls (antiga AlphaTauri) buscando maior consistência e resultados expressivos.")
# Andrea Kimi Antonelli
print(f"\t{racers[4].title()}, jovem italiano, estreia na Fórmula 1 trazendo talento e expectativa para a Mercedes.")
# George Russel
print(f"\t{racers[5].title()}, britânico promissor, busca consolidar-se como líder da equipe Mercedes após a saída de Hamilton.")