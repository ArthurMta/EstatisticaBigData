import pandas as pd 
import numpy as np

#limpar o terminal
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_terminal()



### ENTRADA DE DADOS

try:

    ENDEREÇO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # pegar o csv e colocar num df
    # sep e encnoding para ler o csv sem erros
    df_ocorrencia = pd.read_csv(ENDEREÇO_DADOS, sep=';', encoding='iso-8859-1')


except Exception as e:
    print(f'Erro ao ler o arquivo CSV - {e}')



### ANALISE DE DADOS




try:
    # fechar a amostragem em meses e quant de estelionatos
    df_estelionato_por_mesano = df_ocorrencia[['mes_ano','estelionato']]




    # agrupar por mes e ano e somar os esleionatos deles
    df_estelionato_por_mesano = df_estelionato_por_mesano.groupby('mes_ano', as_index=False)[
        'estelionato'
        ].sum()

    array_estelionato = np.array(df_estelionato_por_mesano['estelionato'])


    # maiores meses com estelionatos (maior quartil)

    top10_meses_mais_estelionato = df_estelionato_por_mesano.sort_values(
        by='estelionato',
        ascending=False
    ).head(10)

    q3_estelionato = np.quantile(array_estelionato, 0.75)

    # menores meses com estelionatos (menor quartil)

    top10_meses_menos_estelionato = df_estelionato_por_mesano.sort_values(
        by='estelionato',
        ascending=True
    ).head(10)

    q1_estelionato = np.quantile(array_estelionato, 0.25)

    # total de estelionato

    df_total_estelionato = df_estelionato_por_mesano['estelionato'].sum()



    # comparacao do total com o maior e menor periodo (percentualmente?)

    perc_mais_estelionato = (top10_meses_mais_estelionato['estelionato'].sum() / df_total_estelionato) * 100
    perc_menos_estelionato = (top10_meses_menos_estelionato['estelionato'].sum() / df_total_estelionato) * 100

except Exception as e:
    print(f'Erro ao analisar os dados (Maior/Menor) - {e}')




# analisar a media, mediana, distancia e os 4 quartis
try:

    # media e mediana
    media_estelionato = df_estelionato_por_mesano['estelionato'].mean()
    mediana_estelionato = df_estelionato_por_mesano['estelionato'].median()

    # distancia
    distancia_estelionato = abs(
        (media_estelionato - mediana_estelionato) / media_estelionato
    )

    # quarti restante
    q2_estelionato = np.quantile(array_estelionato, 0.5)

except Exception as e:
    print(f'Erro ao analisar os dados (estatisticas) - {e}')



# verificar outliers
try:
    
    # calculando limites
    iqr_estelionato = q3_estelionato - q1_estelionato

    limite_inferior = q1_estelionato - (1.5 * iqr_estelionato)
    limite_superior = q3_estelionato + (1.5 * iqr_estelionato)



    # outliers menores

    outliers_menores = df_estelionato_por_mesano[
        df_estelionato_por_mesano['estelionato'] < limite_inferior
    ]

    # outliers maiores

    outliers_maiores = df_estelionato_por_mesano[
        df_estelionato_por_mesano['estelionato'] > limite_superior
    ]

except Exception as e:
    print(f'Erro ao analisar os dados (outliers) - {e}')




### SAIDA DE DADOS



try:

    # mostrar os meses com mais e menos estelionatos

    print('Meses com mais estelionatos:')
    print(30*'-')
    print(top10_meses_mais_estelionato)

    print('\nMeses com menos estelionatos:')
    print(30*'-')
    print(top10_meses_menos_estelionato)



    print('\n\n',30*'-', '\n\n')
    # mostrar o total de estelionatos e a porc dos meses

    print(f'-== MESES COM MAIS ESTELIONATOS ==-\n\n')
    print(f'Percentual dos 10 meses com mais estelionatos sobre o Total:\n > {perc_mais_estelionato:.2f}%\n\n')
    print(f'Q3 dos Estelionatos:\n > {q3_estelionato:.2f}\n\n')

    print(f'-== MESES COM MENOS ESTELIONATOS ==-\n\n')
    print(f'Percentual dos 10 meses com menos estelionatos sobre o Total:\n > {perc_menos_estelionato:.2f}%\n\n')
    print(f'Q1 dos Estelionatos:\n > {q1_estelionato:.2f}\n\n')



    print('\n\n',30*'-', '\n\n')
    # estatisticas
    print(f'-== ESTATISTICAS ==-\n\n')
    
    print(f'\nTotal de estelionatos:\n > {df_total_estelionato}\n\n')
    print(f'Média de estelionatos por mês:\n > {media_estelionato:.2f}\n\n')
    print(f'Mediana de estelionatos por mês:\n > {mediana_estelionato:.2f}\n\n')
    print(f'Distância entre média e mediana:\n > {distancia_estelionato:.2f}\n\n')

    print(f'\nQuartis: \n > q1 = {q1_estelionato}\n > q2 = {q2_estelionato}\n > q3 = {q3_estelionato}')



    print('\n\n',30*'-', '\n\n')
    # outliers
    print(f'-== OUTLIERS ==-\n\n')

    print(f'Limites:\n  Superior > {limite_superior}\n  Inferior > {limite_inferior}\n\n')

    if len(outliers_menores) == 0:
        print(f'Não há outliers menores.\n\n')
    else:
        print('Outliers menores:\n'+30*'-'+f'\n {outliers_menores} \n\n')
        print(f'Número de Outliers menores: {len(outliers_menores)}')

    if len(outliers_maiores) == 0:
        print(f'Não há outliers maiores.\n\n')
    else:
        print('Outliers maiores:\n'+30*'-'+f'\n {outliers_maiores} \n\n')
        print(f'Número de Outliers maiores: {len(outliers_maiores)}')


except Exception as e:
    print(f'Erro na saída dos dados - {e}')