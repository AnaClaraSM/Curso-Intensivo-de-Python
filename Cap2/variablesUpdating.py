# EXERCÍCIO COM VARIÁVEIS
# Tendo as variáveis A, B e C, com seus respectivos valores, ponha o valor de C em B, de B em A e de A em C, sem perder nenhum dos valores.

A = 1
B = 2
C = 3

# Ao usar /n e /t, eles foram impressos literalmente pelo terminal, sem gerar a quebra de linha ou tabulação.
# Motivo: o python não reconhece /n e /t como comandos de quebra ou tabulação, por causa da barra usada. O correto é \n e \t.

print(f"Valores Iniciais:\n\tA: {A}\n\tB: {B}\n\tC: {C}") 

# Salva o valor de A em uma variável intermediaria
valorA = A

# A recebe o valor de B
A = B

# B recebe o valor C
B = C

# C recebe o valor de A (armazenado em valorA)
C = valorA

print(f"Valores Finais:\n\tA: {A}\n\tB: {B}\n\tC: {C}")