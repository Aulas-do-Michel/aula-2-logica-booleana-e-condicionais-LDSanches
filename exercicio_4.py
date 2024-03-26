# """
# #### Exercício 2 - Conversor de moeda
# 
# Você é uma casa de câmbio, recebe dinheiro em reais e transforma na moeda da viagem do usuário.
# 
# Você tem em caixa dólares, pesos argentinos e ienes.
# 
# Pergunte para o usuário para onde ele vai viajar:
# 
# Se ele falar "Estados Unidos", "Argentina" ou "Japão", faça o seguinte processo:
#     Pergunte quantos reais ele vai converter. Receba o valor em float.
#     Converta o valor para a moeda do país.
#     Responda com o valor da moeda e em seguida o tipo da moeda (USD, ARS, ou JPY).
# 
# Se ele falar qualquer outra coisa, responda "Não temos essa moeda em caixa.".
# 
# Utilize as seguintes conversões:
# 5 reais = 1 USD
# 1 real = 180 ARS
# 1 real = 30 JPY
# 
# Obs:
# Nos testes, vou tentar ignorar caso haja apenas uma diferença no número de casas decimais nas respostas.
# Porém, se você quiser garantir que você imprima com exatamente 2 casas decimais você pode usar a seguinte sintaxe: f"{sua_variavel:.2f}".
# 
# Exemplo:
# valor_em_dolares = 23.333333
# print(f"{valor_em_dolares:.2f} USD")
# >>> 23.33 USD
# 
# Mais informações sobre formatação de strings: https://realpython.com/python-f-strings/#interpolating-values-and-objects-in-f-strings
# 
# -------------------------------------------
# Exemplos:
# 
# Qual país você vai viajar? Estados Unidos
# Quantos reais você quer converter? 100
# 
# Resposta:
# 20.00 USD
# 
# -------------------------------------------
# Qual país você vai viajar? Argentina
# Quantos reais você quer converter? 100
# 
# Resposta:
# 18000.00 ARS
# 
# -------------------------------------------
# Qual país você vai viajar? China
# 
# Resposta:
# Não temos essa moeda em caixa.
# """

# ############
# Exercicio 4

pais_destino = str(input('Qual país você vai viajar? '))

cotacao_dolar = float(5)
cotacao_pesos = float(180)
cotacao_ienes = float(30)

if pais_destino == 'Estados Unidos':
    total_reais = float(input('Quantos reais você quer converter? '))
    valor_total = (total_reais / cotacao_dolar)
    print(f'Resposta:\n{valor_total:.2f} USD')
elif pais_destino == 'Argentina':
    total_reais = float(input('Quantos reais você quer converter? '))
    valor_total = (total_reais * cotacao_pesos)
    print(f'Resposta:\n{valor_total:.2f} ARS')
elif pais_destino == 'Japão':
    total_reais = float(input('Quantos reais você quer converter? '))
    valor_total = (total_reais * cotacao_ienes)
    print(f'Resposta:\n{valor_total:.2f} JPY')
else:
    print('Resposta:\nNão temos essa moeda em caixa.')
