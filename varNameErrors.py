message = 1 #variavel literal
Message = 2 #variavel literal
MESSAGE = 3 #constante literal
_message = 4 #variavel literal   # "_message" is not accessed Pylance
_message5 = 5 #variavel literal   # "_message" is not accessed Pylance

# message-6 = 6   ### SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
# message 7 = 7   ### SyntaxError: invalid syntax
# 8message = 8   ### SyntaxError: invalid decimal literal
# 9_message = 9   ### SyntaxError: invalid decimal literal
# mess@ge = 10   ### SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
# ErroDeSintaxe: não é possível atribuir à expressão aqui. Talvez você quisesse dizer '==' em vez de '='?
# Não é possível atribuir valor à expressão declarada antes do =, pois ela não é reconhecida como uma variável. Ou seja, a variável foi declarada incorretamente, recebeu um nome inválido, e não está sendo reconhecida pelo interpretador. O interpretador informa que não é possível atribuir valor aquela expressão (pois não é uma variável) e sugere que talvez o usuário quisesse utilizar o operador de comparação ao invés do operador de atribuição, para comparar valores ao invés de atribuir.

# SyntaxError: invalid syntax
# ErroDeSintaxe: sintaxe inválida
# A sintaxe usada para nomear a variável é inválida

# SyntaxError: invalid decimal literal
# ErroDeSintaxe: número decimal inválido
# Ao ver o número no início do nome da "variável" o interpretador automaticamente reconhece a sequência de caracteres a partir dele como um número (e não como variável), então, ao encontrar letras ou underscores na sequência, ele não reconhece o número, e informa que o número decimal declarado é inválido (pois nenhum número decimal válido contém letras ou underscores).

#OBS.: As variáveis iniciadas com underscore ficaram mais claras (menos opacas) no editor e com uma nota do Pylance dizendo ""_message" is not accessed" (a variável _message não é acessada) - apenas uma atenção do recurso Pylance a esse tipo de variável, visto que variáveis privadas costumam iniciar com _ ????

# Pylance -> é uma extensão do VSCode para Python -> "Pylance is an extension that works alongside Python in Visual Studio Code to provide performant language support." -> fornece análise estática de código Python