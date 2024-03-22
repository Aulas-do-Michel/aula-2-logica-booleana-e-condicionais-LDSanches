# """
# #### Exercício 1

# Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

# Exemplo:

# Digite um número:
# 10

# Par
# --------
# Digite um número:
# 1

# Ímpar

# Dica: Lembre do comando de resto da divisão inteira!
# """

# ############
# Exercicio 1

digite_numero = int(input('Digite um número: '))

numero_resultado = (digite_numero % 2)

if numero_resultado == 0:
    print('Par')
else:
    print('Ímpar')

