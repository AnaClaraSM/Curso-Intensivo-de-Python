# O Python e demais linguagens de programação desconsideram erros ortográficos no que tange ao idioma inglês, português, ou enfim. Porém, as linguagens são criteriosas quanto à correspondência entre os nomes de variáveis (e outros), ao referenciá-las, se não forem referenciados corretamente em tudo, o Python não reconhecerá a variável, função ou comando.


# Variáveis com nomes gramaticalmente incorretos, mas correspondentes (mesage)

mesage = "The term 'mesage' is gramatically wrong"
print(f"{mesage}, but it has been corretly referenciated.")


# Variáveis com nomes gramaticalmente corretos, mas não correspondentes (message)
message = "The term 'message' is gramatically correct"
print(f"{Message}, but has been incorrectly referenciated.")
# Retorno -> NameError: name 'Message' is not defined. Did you mean: 'message'?
print(f"{messsage}, but has been incorrectly referenciated.")
# Retorno -> NameError: name 'messsage' is not defined. Did you mean: 'message'?
