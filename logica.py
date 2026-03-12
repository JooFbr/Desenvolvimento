# Criando variáveis para armazenar dados.

nome = "João"
sobrenome = "Silva"
idade = 20
altura = "1.71"
adulto = True

# Escrevendo no console.

print(nome)
print(sobrenome)
print(idade)
print(altura)
print(adulto)

# conectando informações
print('Meu nome é', nome)
print('Meu sobrenome é ' + sobrenome)
print('Meu nome completo', nome, sobrenome)
print('Minha idade é {} e minha altura é {}'.format(idade, altura))

# maneira moderna (baiana) de concatenar
print(f'Meu nome é {nome} e tenho {idade} anos')


# Verificando tipos de Variavel
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(altura))
print(type(adulto))
