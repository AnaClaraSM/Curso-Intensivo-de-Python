# Jogo de perguntas e respostas sobre a Fórmula 1 - Quiz (teste)

# Fazer uma lista de objetos (dicionários) para armazenar as perguntas, respostas e alternativas
quiz = [
    # Pergunta 1 (índice 0)
    {
        "enunciado": "Qual piloto atual detém o recorde de mais títulos mundiais na Fórmula 1?",
        "alternativas": ["A) Lewis Hamilton", "B) Sebastian Vettel", "C) Max Verstappen", "D) Fernando Alonso"],
        "resposta_correta": "A"
    },
    # Pergunta 2 (índice 1)
    {
        "enunciado": "Qual equipe venceu o campeonato de construtores de 2024 na Fórmula 1?",
        "alternativas": ["A) Mercedes", "B) Red Bull Racing", "C) Ferrari", "D) McLaren"],
        "resposta_correta": "B" 
    },
    # Pergunta 3 (índice 2)
    {
        "enunciado": "Qual é o nome completo do piloto conhecido como \"Checo\" Pérez?",
        "alternativas": ["A) Sergio Pérez Mendoza", "B) Esteban Pérez Gutiérrez", "C) Carlos Pérez Alva", "D) Alejandro Pérez Landa"],
        "resposta_correta": "A" 
    },
    # Pergunta 4 (índice 3)
    {
        "enunciado": "Quantas vitórias Lewis Hamilton tem na carreira até o final da temporada de 2024?",
        "alternativas": ["A) 103", "B) 99", "C) 97", "D) 95"],
        "resposta_correta": "B" 
    },
    # Pergunta 5 (índice 4)
    {
        "enunciado": "Qual é a nacionalidade de Charles Leclerc?",
        "alternativas": ["A) Francês", "B) Monegasco", "C) Italiano", "D) Suíço"],
        "resposta_correta": "B" 
    },
    # Pergunta 6 (índice 5)
    {
        "enunciado": "Qual é o nome do circuito em que ocorre o GP de Mônaco?",
        "alternativas": ["A) Circuito da Riviera", "B) Circuit de Monaco", "C) Circuito de Monte Carlo", "D) Circuito do Principado"],
        "resposta_correta": "C" 
    },
    # Pergunta 7 (índice 6)
    {
        "enunciado": "Qual piloto conquistou o campeonato de pilotos da Fórmula 1 em 2024?",
        "alternativas": ["A) Max Verstappen", "B) Lewis Hamilton", "C) Lando Norris", "D) Charles Leclerc"],
        "resposta_correta": "A" 
    },
    # Pergunta 8 (índice 7)
    {
        "enunciado": "Qual é o país de origem da equipe Mercedes-AMG Petronas?",
        "alternativas": ["A) Lewis Hamilton", "B) Sebastian Vettel", "C) Max Verstappen", "D) Fernando Alonso"],
        "resposta_correta": "B" 
    },
    # Pergunta 9 (índice 8)
    {
        "enunciado": "Quantos títulos mundiais Fernando Alonso possui?",
        "alternativas": ["A) Lewis Hamilton", "B) Sebastian Vettel", "C) Max Verstappen", "D) Fernando Alonso"],
        "resposta_correta": "B" 
    },
    # Pergunta 10 (índice 9)
    {
        "enunciado": "Em que ano foi introduzido o sistema de pontuação para a volta mais rápida em corridas?",
        "alternativas": ["A) 2018", "B) 2019", "C) 2020", "D) 2021"],
        "resposta_correta": "B" 
    }  
]

# Percorre cada item (pergunta) do quiz
# Cada pergunta é um dicionário da lista quiz
# Para cada pergunta do quiz
for pergunta in quiz:
    # Acessa e imprime o enunciado (com quebra de linha antes)
    print(f"\n{pergunta["enunciado"]}")
    # Percorre a lista de alternativas da pergunta. 
    # Para cada alternativa
    for alternativa in pergunta["alternativas"]:
        # Imprime a alternativa
        print(alternativa)