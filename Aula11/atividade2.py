import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_terminal()




try:
    ENDEREÇO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    df_ocorrencia = pd.read_csv(ENDEREÇO_DADOS, sep=';', encoding='iso-8859-1')
    
    df_cvli_por_aisp = (
        df_ocorrencia[['aisp', 'cvli']]
        .groupby('aisp', as_index=False)['cvli']
        .sum()
    )
except Exception as e:
    print(f'Erro ao ler o arquivo CSV - {e}')
else:




### ANALISE DE DADOS





    array_cvli = np.array(df_cvli_por_aisp['cvli'])

    total_cvli = np.sum(array_cvli)
    min_cvli = np.min(array_cvli)
    max_cvli = np.max(array_cvli)
    media_cvli = np.mean(array_cvli)
    mediana_cvli = np.median(array_cvli)
    distancia_cvli = (
        ((media_cvli - mediana_cvli) / mediana_cvli) * 100
    )

    q1_cvli, q2_cvli, q3_cvli = np.quantile(array_cvli, [0.25, 0.50, 0.75])
    iqr_cvli = q3_cvli - q1_cvli
    limite_inferior = q1_cvli - (1.5 * iqr_cvli)
    limite_superior = q3_cvli + (1.5 * iqr_cvli)
    amplitude_total = max_cvli - min_cvli
    variancia_cvli = np.var(array_cvli)
    assimetria_cvli = df_cvli_por_aisp['cvli'].skew()
    curtose_cvli = df_cvli_por_aisp['cvli'].kurtosis()

    outliers_menores = df_cvli_por_aisp[df_cvli_por_aisp['cvli'] < limite_inferior]
    outliers_maiores = df_cvli_por_aisp[df_cvli_por_aisp['cvli'] > limite_superior]






#### SAIDA DE DADOS


    print(f'Outliers menores:\n{outliers_menores}')
    print(f'Outliers maiores:\n{outliers_maiores}')



    


    plt.figure(figsize=(12, 8))
    

    plt.subplots(1, 3)

    # plt.boxplot(array_cvli, patch_artist=True)
    plt.axis('off')
    
    
    plt.title('Resumo estatístico')
    
    plt.text(0.5,0.95, f'Limite inferior: {limite_inferior:.2f}')
    plt.text(0.5,0.9, f'Mínimo: {min_cvli}')
    plt.text(0.5,0.85, f'Q1: {q1_cvli:.2f}')
    plt.text(0.5,0.8, f'Mediana (Q2): {q2_cvli:.2f}')
    plt.text(0.5,0.75, f'Q3: {q3_cvli:.2f}')
    plt.text(0.5,0.7, f'Limite superior: {limite_superior:.2f}')
    plt.text(0.5,0.65, f'Máximo: {max_cvli}')
    
    plt.text(0.6,0.95, f'Média: {media_cvli:.2f}')
    plt.text(0.6,0.9, f'Mediana: {mediana_cvli:.2f}')
    plt.text(0.6,0.85, f'Distância: {distancia_cvli:.2f}%')
    plt.text(0.6,0.8, f'IQR: {iqr_cvli:.2f}')
    plt.text(0.6,0.75, f'Amplitude Total: {amplitude_total}')
    plt.text(0.6,0.7, f'Variância: {variancia_cvli:.2f}')
    plt.text(0.6,0.65, f'Assimetria: {assimetria_cvli:.2f}')
    plt.text(0.6,0.6, f'Curtose: {curtose_cvli:.2f}')

    plt.show()

#