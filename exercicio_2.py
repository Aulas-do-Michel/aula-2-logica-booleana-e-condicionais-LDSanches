# """
# #### Exercício 2 - Identificar se a variante está no gene BRCA1 - Versão 1.
# 
# Receba 2 inputs do usuário:
# 1) O cromossomo de uma variante. Ele virá escrito como texto e da seguinte forma "chr1", "chr2", etc.
# 2) A posição dessa variante. Será um número inteiro.
# 
# Responde:
# "Sim" se ela estiver no BRCA1.
# "Não" se ela não estiver.
# 
# Considere que a variante está no gene BRCA1 se estiver no cromossomo 17 (chr17), e se a posição estiver no # intevalo de 41196312 a 41277500.
# 
# Obs: Tirei a localização daqui: https://grch37.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012048;# r=17:41196312-41277500.
# 
# Exemplos:
# 
# ----------------------------------
# 
# Digite o cromossomo: chrM
# Digite a posição: 41196390
# Resposta:
# Não
# 
# ----------------------------------
# 
# Digite o cromossomo: chr17
# Digite a posição: 99
# Resposta:
# Não
# 
# ----------------------------------
# 
# Digite o cromossomo: chr17
# Digite a posição: 41196313
# Resposta:
# Sim
# 
# """

# Exercicio 2
cromossomo_variante = input('Digite o cromossomo: chr')
posicao_variante =  int(input('Digite a posição: '))

gene_brca1 = (str(f'chr{cromossomo_variante}') == str('chr17'))
range_posicao = (posicao_variante >= 41196312 and posicao_variante <= 41277500)

if gene_brca1 == True and range_posicao == True:
    print('Resposta:')
    print('Sim')
else:
    print('Resposta:')
    print('Não')
