import os # Importa OS (Operationa System)

# Jogo de perguntas e respostas sobre a Fórmula 1 - Quiz (teste)

# Lista de objetos (dicionários) para armazenar as perguntas, respostas e alternativas
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

acertos = 0 # Armazena o número de acertos do usuário
total_perguntas = len(quiz) #Obtém o total de perguntas do quiz

# Limpa o terminal (cls se for windows, clear se outro)
os.system("cls" if os.name == 'nt' else 'clear')

# Mensagem incial
print()
print("===========================================")
print("  🏁 BEM-VINDO AO QUIZ DE FÓRMULA 1! 🏁   ")
print("===========================================")
print("   Responda as questões a seguir e veja    ")
print("   se é um expert em Fórmula 1! 🏎️💨      ")
print("===========================================")
print()
# print("Está pronto para começar?")
# print()

# Percorre cada pergunta (item/dicionário) do quiz (lista), enumerando-as (a partir do 1)
# Para cada número e pergunta do quiz
for numero, pergunta in enumerate(quiz, start=1):

    # Imprime o número da pergunta e o enunciado - Não usar as mesmas aspas de fora dentro da string
    print(f"{numero}. {pergunta['enunciado']}")
    # Percorre a lista de alternativas da pergunta. 
    # Para cada alternativa
    for alternativa in pergunta["alternativas"]:
        # Imprime a alternativa
        print(alternativa)
    
    # Recebe a resposta do usuário e converte para maiúscula (para  para garantir compatibilidade com a resposta certa armazenada)
    resposta_usuario = input("Digite sua resposta (A, B, C ou D):").upper()
    
    # Verifica se a resposta do usuário para a pergunta está correta.
    if (resposta_usuario == pergunta["resposta_correta"]):
        # Se sim, conta o acerto
        acertos += 1
        #Exibe mensagem de acerto [OPCIONAL]
        print("✅ Resposta Correta!")
    else:
        #Exibe mensagem de erro [OPCIONAL]
        print(f"❌ Resposta Errada! A resposta correta é {pergunta['resposta_correta']}.") 
    
    #Quizzes não costumam exibir as respostas, a fim de poderem ser refeitos

    # Linha em branco para separar as perguntas
    print()

# [OPCIONAL] Calcula a porcentagem de acertos
porcentagem_acertos = (acertos / total_perguntas) * 100

# Exibe a quantidade (e percentual) de acertos do usuário em relação ao total
print(f"Você acertou {acertos} de {total_perguntas} questões ({int(porcentagem_acertos)}%).")

# Opção - Utilizar porcentagem para automatizar o cálculo
# Verifica a quantidade de acertos de usuário e exibe uma mensagem personalizada
# 9-10 acertos
if acertos > 8:
    print("Você é um mestre em Fórmula 1! Seu conhecimento é de um comentarista esportivo. Continue acompanhando todas as corridas, pois você claramente é apaixonado por esse esporte!")
# 7-8 acertos
elif acertos > 6:
    print("Excelente desempenho! Você sabe muito sobre Fórmula 1 e claramente acompanha o esporte com atenção. Com mais algumas corridas, você se tornará um especialista!")
# 4-6 acertos
elif acertos > 3:
    print("Bom trabalho! Seu conhecimento é sólido, mas ainda há espaço para crescer. Que tal revisar alguns detalhes e assistir às corridas antigas para se aprofundar mais?")
# 1-3 acertos
elif acertos > 0:
    print("Você está no começo da sua jornada na Fórmula 1. Não desanime! Quanto mais você acompanhar as corridas e explorar a história do esporte, mais vai aprender. Vamos acelerar no aprendizado!")
# 0 acertos
else:
    print("Ah, parece que você ainda não pegou o ritmo do jogo! Mas tudo bem, todo mundo começa de algum lugar. Assista às corridas, leia sobre os pilotos e tente o quiz novamente depois!")

print()