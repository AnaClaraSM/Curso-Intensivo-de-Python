# Exercício 1: Armazenar nomes de pessoas em uma lista chamada names e exibir os nomes um por um

# Lista de nomes (inspirados em nomes de linguagens)
names = ["Patrick", "Jasmine", "Hector", "Cirus", "Cedar", "Arden", "Pietro", "Seacole", "Jamal"]

# Imprime os nomes individualmente
print("Below comes a list with names, inspired in programming languages names.")
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])
print(names[7])
print(names[8])

# Exercício 2: Exiba uma mensagem para cada pessoa, que deve ser a mesma para todas, mas personalizada com seu nome

# Extra, criar mais uma lista, com os nomes das linguagens, e criar uma mensagem associando os nomes.
languages = ["Python", "JavaScript", "HTML", "CSS", "C", "Arduino", "PHP", "SQL", "Java"]

# Mensagem padrão
commonMessage = "tem seu nome inspirado na linguagem"

# Imprime uma mensagem padrão para cada pessoa, personalizada com seu nome e linguagem respectiva
print()
print(f"{names[0]} {commonMessage} {languages[0]}")
print(f"{names[1]} {commonMessage} {languages[1]}")
print(f"{names[2]} {commonMessage} {languages[2]}")
print(f"{names[3]} {commonMessage} {languages[3]}")
print(f"{names[4]} {commonMessage} {languages[4]}")
print(f"{names[5]} {commonMessage} {languages[5]}")
print(f"{names[6]} {commonMessage} {languages[6]}")
print(f"{names[7]} {commonMessage} {languages[7]}")
print(f"{names[8]} {commonMessage} {languages[8]}")