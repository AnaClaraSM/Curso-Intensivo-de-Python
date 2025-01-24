# Anotações do Livro

## CAP 1 - PRIMEIROS PASSOS

*16-07-2024*

- Comandos e instruções python não utilizam ponto e vírgula (;).

- Em caso de erro, sempre verifique o Traceback.

- Faça um caderno de erros e um caderno de ideias (descrevendo sucintamente o que deseja criar). 

- Tente implementar suas ideias de projeto desde o início, mesmo que só consiga fazer pedacinhos delas no começo. Ex.: Quero criar um app de pizzaria e prendi a imprimir textos -> Imprima a mensagem de boas-vindas ao cliente do aplicativo da pizzaria.



## CAP 2 - VARIÁVEIS E TIPOS DE DADOS SIMPLES

*31-07-2024*

Variáveis: 

Nomes de variáveis:
-> Não podem ter espaços, traços ou outros caracteres especiais EXCETO underscore/underline/sublinhado (_)

OBSERVAÇÃO -> "variáveis" nomeadas em CAIXA ALTA são, por convenção, vistas como constantes (ou seja, convencionou-se nomear constantes Python com letras maiúsculas). No entanto, não é uma "constante verdadeira" (como em outras linguagens), pois o Python não impede que seu valor seja mudado.
-> mensagem = variável
-> Mensagem = variável
-> MENSAGEM = constante

--> O python faz diferença entre letras maiúsculas e minúsculas (linguagem case sensitive), logo:
--> ---> mensagem != Mensagem

\## Teste de erros em variáveis

message = 1 #variavel literal
Message = 2 #variavel literal
MESSAGE = 3 #constante literal
_message = 4 #variavel literal   # "_message" is not accessed Pylance
_message5 = 5 #variavel literal   # "_message" is not accessed Pylance

\# message-6 = 6   \### SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
\# message 7 = 7   ### SyntaxError: invalid syntax
\# 8message = 8   ### SyntaxError: invalid decimal literal
\# 9_message = 9   ### SyntaxError: invalid decimal literal
\# mess@ge = 10   ### SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

\# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
\# ErroDeSintaxe: não é possível atribuir à expressão aqui. Talvez você quisesse dizer '==' em vez de '='?
\# Não é possível atribuir valor à expressão declarada antes do =, pois ela não é reconhecida como uma variável. Ou seja, a variável foi declarada incorretamente, recebeu um nome inválido, e não está sendo reconhecida pelo interpretador. O interpretador informa que não é possível atribuir valor aquela expressão (pois não é uma variável) e sugere que talvez o usuário quisesse utilizar o operador de comparação ao invés do operador de atribuição, para comparar valores ao invés de atribuir.

\# SyntaxError: invalid syntax
\# ErroDeSintaxe: sintaxe inválida
\# A sintaxe usada para nomear a variável é inválida

\# SyntaxError: invalid decimal literal
\# ErroDeSintaxe: número decimal inválido
\# Ao ver o número no início do nome da "variável" o interpretador automaticamente reconhece a sequência de caracteres a partir dele como um número (e não como variável), então, ao encontrar letras ou underscores na sequência, ele não reconhece o número, e informa que o número decimal declarado é inválido (pois nenhum número decimal válido contém letras ou underscores).

#OBS.: As variáveis iniciadas com underscore ficaram mais claras (menos opacas) no editor e com uma nota do Pylance dizendo ""_message" is not accessed" (a variável _message não é acessada) - apenas uma atenção do recurso Pylance a esse tipo de variável, visto que variáveis privadas costumam iniciar com _ ????

\# Pylance -> é uma extensão do VSCode para Python -> "Pylance is an extension that works alongside Python in Visual Studio Code to provide performant language support." -> fornece análise estática de código Python




----------------------------------------------
## CAP 3 - INTRODUÇÃO ÀS LISTAS

Listas são conjuntos de elementos ordenados. 

Em python, as listas são designadas por colchetes, "[]", dentro dos quais ficam os elementos, separados por vírgulas.

Para criar listas em Python, basta:

```python
nomeDaLista = [] #Cria uma lista vazia

outraLista = [elemento1, elemento2, elemento3] #Cria uma lista e inicializa com 3 elementos
```

Ao criar listas, como geralmente terão mais de um elemento, é conveniente nomeá-las no plural. Ex.: names, elements, cars, etc.

Lista são indexáveis, ou seja, seus elementos possuem índices, que indicam sua posição na lista e permitem referenciá-los individualmente. 

Os índices começam em 0. Portanto, o índice de qualquer elemento será equivalente ao número de sua posição/ordem na lista, menos 1. \
Exemplos: 
 - 1º elemento -> índice 0;
 - 2º Elemento -> índice 1; 
 - 3º Elemento -> índice 2; 
 - 4º Elemento -> índice 3;

Logo: \
&nbsp;&nbsp;&nbsp;&nbsp;$ índice = posi\c{c}ão - 1 $


Em python, o índice -1 designa o último elemento da lista. O índice -2 designa o segundo elemento do final, o -3 o terceiro do final, e assim em diante ```(como um ciclo, ou carrossel (?))```.

Para acessar um elemento de uma lista com base em seu índice, basta:

```python
nomeDaLista[i] #Em que i é o número do índice

#Exemplo:

corredoresF1 = ["Hamilton", "Leclerc", "Verstappen"]

print(corredoresF1[0]) #Retorna o primeiro item da lista (Hamilton)
print(corredoresF1[1]) #Retorna Leclerc
print(corredoresF1[-1]) #Retorna o último item da lista (Verstappen)
```

Os métodos de string também podem ser usados nos elementos de listas. Exemplo:

```python
# Nomes dos corredores em minúsculas
corredoresF1 = ["hamilton", "leclerc", "verstappen"]

#Usa o método title() para imprimir o primeiro elemento da lista com a inicial maiúscula
print(corredoresF1[0].title()) #Imprime Hamilton
```








## Loops

### For in

for elemento in lista:
    comandos

O for in pode ser usado para percorrer listas (ou strings ou números) e realizar ações com seus elementos individuais

Basta inserir, após o for, um nome que irá referenciar os elementos da lista, seguido de in e do nome da lista

#Para cada elemento na lista, imprime o elemento
#Percorre a lista quiz e a cada elemento (referenciado como question), armazena-o em uma variável (nesse caso question) e, nesse caso, ainda o imprime
for question in quiz:
    print(f"{question}\n")

A estrutura do for é a seguinte:
for item in colecao:
    # Código que será executado para cada item

item: Representa cada elemento da coleção, que vai mudando a cada iteração do loop.
colecao: É o objeto que contém os itens que você quer percorrer (pode ser uma lista, string, etc.).


Exemplo 1: Percorrendo uma lista
Vamos ver um exemplo simples com uma lista de frutas:

    frutas = ["maçã", "banana", "laranja"]

    for fruta in frutas:
        print(fruta)

Como funciona?
O for começa a execução e pega o primeiro item da lista frutas, que é "maçã", e coloca na variável fruta.
O código dentro do for (neste caso, print(fruta)) é executado, imprimindo "maçã".
O for passa para o próximo item da lista, que é "banana", e faz o mesmo processo.
Isso acontece até que todos os itens da lista tenham sido percorridos.
Saída:
    maçã
    banana
    laranja



#print("Bem-vindo ao Quiz de Fórmula 1! Responda as perguntas a seguir e descubra o quanto você sabe sobre o esporte.")
#print() #Line Break (Isso é uma boa prática???)
#print(f"Pergunta {i+1}: {quiz[i]["pergunta"]}")
#print(quiz[i]["alternativas"][0])
#print(quiz[i]["alternativas"][1])
#print(quiz[i]["alternativas"][2])
#print(quiz[i]["alternativas"][3])
#print("Digite sua resposta:")
#print() #Linha em branco entre as perguntas

#Para cada elemento na lista, imprime o elemento
#Percorre a lista quiz e a cada elemento (referenciado como question), armazena-o em uma variável (nesse caso question) e impr
for question in quiz:
    print(f"{question}\n")

#Percorre os elementos de um dicionário (quiz[0] é o primeiro elemento da lista quiz, é um objeto/dicionário), ou seja, as chaves. Retorna apenas as chaves sem os valores 
for element in quiz[0]:
    print(f"{element}\n")

#Para acessar os valores das chaves de um dicionário, pode-se usar o método .values() do python
#Percorre cada valor do dicionário (quiz[0]), e imprime
for element in quiz[0].values():
    print(f"{element}\n")

#Para acessar tanto as chaves como os valores de um dicionário, pode-se usar o método .items() do python, que retorna pares chave-valor (key-value)
for chave, valor in quiz[0].items():
    print(f"{chave} = {valor}")

### Enumerate - Percorrer e enumerar elementos de listas 

O enumerate é uma função do python que permite enumerar os itens de uma lista enquanto ela é percorrida.
A cada iteração do loop, a função enumerate retorna dois valores:
- O índice do elemento, começando em 0, por padrão (pode ser alterado com o start)
- O elemento da lista.
Como o enumerate retorna dois valores, é preciso inserir duas variáveis após o for (ao invés de só uma) para que possam armazenar cada uma um valor. Ou seja, é preciso inserir uma variável para receber o índice, e outra para o elemento em si.

Ex.: 
```python
corredoresF1 = ["Hamilton", "Leclerc", "Verstappen"]

# Loop com enumeração de elementos
for indice, corredor in enumerate(corredoresF1):
    print(f"Corredor {indice}: {corredor}")
```
Retornou:
```
Corredor 0: Hamilton  
Corredor 1: Leclerc   
Corredor 2: Verstappen
```
Observe que o primeiro corredor foi nomeado como "Corredor 0", ao invés de 1, pois a enumeração de índices começa em 0. 

Uma forma de resolver isso seria somando 1 à variável indice no print. Assim:
```python
# Loop com enumeração de elementos
for indice, corredor in enumerate(corredoresF1):
    # Soma 1 ao índice, para contar de 1 em diante
    print(f"Corredor {indice + 1}: {corredor}")
```
Retorna:
```
Corredor 1: Hamilton  
Corredor 2: Leclerc   
Corredor 3: Verstappen
```


Em python, porém, há uma forma mais prática, que elimina cálculos extras, o start.

O start é uma parâmetro opcional da função enumerate. Ele permite definir o ponto de início da contagem de índice retornada pelo enumerate (ou seja, não muda a indexação real da lista, só a contagem retornada pelo enumerate no loop). 

Como usar:
```python
# Loop com enumeração de elementos
enumerate(iteravel, start=valor_inicial)

# Exemplo
enumerate(corredoresF1, start=1)
```
// Iterável:

Diferenças +1 e start=1

+1 no print
- É apenas uma manipulação visual para exibição. A indexação da lista a partir zero, dentro ou fora do loop, permanece inalterada.
- Útil quando se quer manter o índice original (zero-based) e alterar apenas a visualização final.
- Útil para situações em que a lógica do índice importa (ex.: acessar itens na lista pelo índice real).

start=1
- Mais prático, direto e intuitivo.
- Elimina cálculos a mais e deixa o código mais limpo.
- Altera o número inicial do índice retornado pelo enumerate.
- Afeta como o número do índice aparece durante o loop, sem mudar a lista original.
- Útil quando se quer que o índice sempre comece de um valor específico, sem precisar manipular a exibição no loop. Ex: Numeração de perguntas, páginas ou qualquer coisa que o usuário veja.


## Entrada de Usuário 

### Input

A função input() permite solicitar uma entrada de dado ao usuário através do terminal.

O valor retornado pelo input() será sempre uma string. Para trabalhar com outros tipos, é preciso converter o valor manualmente.

Ao usar input() é preciso criar uma variável para armazenar o valor que o usuário digitará, e pode-se também inserir uma mensagem.

```python
resposta = input("Mensagem")

# Exemplos
nome = input("Qual o seu nome?")

# Conversão para inteiro
idade = int(input("Qual a sua idade"))
```

Obs.: Se o usuário inserir algo inválido (como texto em vez de um número), o programa pode gerar um erro. Para evitar isso, você pode usar um bloco try-except.