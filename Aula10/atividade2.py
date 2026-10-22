#limpar o terminal
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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



try:
    # fechar a df com munic (municipio), aisp (o batalhão) , cvli (crimes violentos letais intencionais)

    df_cvli_por_aisp = df_ocorrencia[['munic','aisp','cvli']]

    df_cvli_por_aisp = df_cvli_por_aisp.groupby('aisp', as_index=False)['cvli'].sum()

except Exception as e:
    print(f'Erro ao analisar os dados - {e}')





### ANALISE DE DADOS





try:
    # algumas metricas simples

    #total
    total_cvli = df_cvli_por_aisp['cvli'].sum()

    # pegar maior
    max_cvli = df_cvli_por_aisp['cvli'].max()

    #menor
    min_cvli = df_cvli_por_aisp['cvli'].min()

except Exception as e:
    print(f'Erro ao processar metricas - {e}')


try:
    # media mediana distancia

    media_cvli = df_cvli_por_aisp['cvli'].mean()

    mediana_cvli = df_cvli_por_aisp['cvli'].median()

    distancia_cvli = (
        (media_cvli - mediana_cvli) / mediana_cvli
    )



    # quartis

    q1_cvli = np.quantile(df_cvli_por_aisp['cvli'], 0.25)
    q2_cvli = np.quantile(df_cvli_por_aisp['cvli'], 0.50)
    q3_cvli = np.quantile(df_cvli_por_aisp['cvli'], 0.75)

except Exception as e:
    print(f'Erro ao processar metricas2 - {e}')


try:
    # outliers

    #iqr
    iqr_cvli = q3_cvli - q1_cvli

    limite_inferior = q1_cvli - (1.5 * iqr_cvli)
    limite_superior = q3_cvli + (1.5 * iqr_cvli)


    # lista dos menores outliers
    outliers_menores = df_cvli_por_aisp[
        df_cvli_por_aisp['cvli'] < limite_inferior
    ]

    # lista dos maiores outliers
    outliers_maiores = df_cvli_por_aisp[
        df_cvli_por_aisp['cvli'] > limite_superior
    ]

    #teste
    print(f'Outliers menores: \n{outliers_menores}')
    print(f'Outliers maiores: \n{outliers_maiores}')

except Exception as e:
    print(f'Erro ao processar outliers - {e}')


# try:

# except Exception as e:
#     print(f'Erro ao processar ... - {e}')





#### SAIDA DE DADOS





#