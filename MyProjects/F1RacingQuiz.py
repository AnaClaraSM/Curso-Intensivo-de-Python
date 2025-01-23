# Jogo de perguntas e respostas sobre a Fórmula 1

# Fazer uma lista de objetos (dicionários) para armazenar as perguntas, respostas e alternativas
quiz = [
    # Pergunta 1 (índice 0)
    {
        "pergunta": "Qual piloto atual detém o recorde de mais títulos mundiais na Fórmula 1?",
        "alternativas": ["A) Lewis Hamilton", "B) Sebastian Vettel", "C) Max Verstappen", "D) Fernando Alonso"],
        "resposta_correta": "A"
    },
    # Pergunta 2 (índice 1)
    {
        "pergunta": "Qual equipe venceu o campeonato de construtores de 2024 na Fórmula 1?",
        "alternativas": ["A) Mercedes", "B) Red Bull Racing", "C) Ferrari", "D) McLaren"],
        "resposta_correta": "B" 
    },
    # Pergunta 3 (índice 2)
    {
        "pergunta": "Qual é o nome completo do piloto conhecido como \"Checo\" Pérez?",
        "alternativas": ["A) Sergio Pérez Mendoza", "B) Esteban Pérez Gutiérrez", "C) Carlos Pérez Alva", "D) Alejandro Pérez Landa"],
        "resposta_correta": "A" 
    },
    # Pergunta 4 (índice 3)
    {
        "pergunta": "Quantas vitórias Lewis Hamilton tem na carreira até o final da temporada de 2024?",
        "alternativas": ["A) 103", "B) 99", "C) 97", "D) 95"],
        "resposta_correta": "B" 
    },
    # Pergunta 5 (índice 4)
    {
        "pergunta": "Qual é a nacionalidade de Charles Leclerc?",
        "alternativas": ["A) Francês", "B) Monegasco", "C) Italiano", "D) Suíço"],
        "resposta_correta": "B" 
    },
    # Pergunta 6 (índice 5)
    {
        "pergunta": "Qual é o nome do circuito em que ocorre o GP de Mônaco?",
        "alternativas": ["A) Circuito da Riviera", "B) Circuit de Monaco", "C) Circuito de Monte Carlo", "D) Circuito do Principado"],
        "resposta_correta": "C" 
    },
    # Pergunta 7 (índice 6)
    {
        "pergunta": "Qual piloto conquistou o campeonato de pilotos da Fórmula 1 em 2024?",
        "alternativas": ["A) Max Verstappen", "B) Lewis Hamilton", "C) Lando Norris", "D) Charles Leclerc"],
        "resposta_correta": "A" 
    },
    # Pergunta 8 (índice 7)
    {
        "pergunta": "Qual é o país de origem da equipe Mercedes-AMG Petronas?",
        "alternativas": ["A) Lewis Hamilton", "B) Sebastian Vettel", "C) Max Verstappen", "D) Fernando Alonso"],
        "resposta_correta": "B" 
    },
    # Pergunta 9 (índice 8)
    {
        "pergunta": "Quantos títulos mundiais Fernando Alonso possui?",
        "alternativas": ["A) Lewis Hamilton", "B) Sebastian Vettel", "C) Max Verstappen", "D) Fernando Alonso"],
        "resposta_correta": "B" 
    },
    # Pergunta 10 (índice 9)
    {
        "pergunta": "Em que ano foi introduzido o sistema de pontuação para a volta mais rápida em corridas?",
        "alternativas": ["A) 2018", "B) 2019", "C) 2020", "D) 2021"],
        "resposta_correta": "B" 
    }  
]

# # Acesso à lista
# print(quiz) #Retorna a lista quiz, com todos os seus objetos, com todos os seus atributos
# # Acesso a elementos da lista pelo índice
# print(quiz[0]) #Retorna o primeiro item da lista, ou seja, o primeiro objeto com todos os seus atributos (pergunta, alternativas, resposta)
# # Acesso a valores do objeto pela chave (nome do atributo)
# print(quiz[0]["pergunta"]) #Retorna o valor do atributo pergunta do primeiro objeto (pergunta) da lista quiz
# Índices sempre ao lado...
# print(quiz[0]["alternativas"][0]) #Retorna o valor do primeiro item (alternativa) da lista contida no atributo alternativas do primeiro objeto (pergunta) da lista quiz

numero_acertos = 0
resposta_usuario = ""

#Ao comparar a resposta do usuário utilizar upper, para garantir que a letra fique em maiúsculo, para evitar erros na comparação por digitação e case sensitive

# Índice para testes
i = 0

# Impressão das perguntas

# print("Bem-vindo ao Quiz de Fórmula 1! Responda as perguntas a seguir e descubra o quanto você sabe sobre o esporte.")
# print() #Line Break (Isso é uma boa prática???)
# print(f"Pergunta {i+1}: {quiz[i]["pergunta"]}")
# print(quiz[i]["alternativas"][0])
# print(quiz[i]["alternativas"][1])
# print(quiz[i]["alternativas"][2])
# print(quiz[i]["alternativas"][3])
# print("Digite sua resposta:")
# print() #Linha em branco entre as perguntas

# Para cada elemento na lista, imprime o elemento
# Percorre a lista quiz e a cada elemento (referenciado como question), armazena-o em uma variável (nesse caso question) e impr
for question in quiz:
    print(f"{question}\n")

# Percorre os elementos de um dicionário (quiz[0] é o primeiro elemento da lista quiz, é um objeto/dicionário), ou seja, as chaves. Retorna apenas as chaves sem os valores 
for element in quiz[0]:
    print(f"{element}\n")
