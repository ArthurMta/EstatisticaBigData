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
        df_ocorrencia[['aisp', 'cvli', 'munic']]
        .groupby('aisp', as_index=False)
        .agg({'cvli': 'sum', 'munic': 'first'})
    )
    
    
    
    df_cvli_por_aisp['aisp'] = df_cvli_por_aisp['aisp'].astype(str) 
    
    
    
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

    df_cvli_por_aisp_outliers_inf = df_cvli_por_aisp[df_cvli_por_aisp['cvli'] < limite_inferior]
    df_cvli_por_aisp_outliers_sup = df_cvli_por_aisp[df_cvli_por_aisp['cvli'] > limite_superior]






#### SAIDA DE DADOS


    # print(f'Outliers menores:\n{df_cvli_por_aisp_outliers_inf}')
    # print(f'Outliers maiores:\n{df_cvli_por_aisp_outliers_sup}')
    

    try:
        plt.figure(figsize=(18, 9))
        

        # grafico no qual seja possivel obserar como os dados estão distribuidos
        plt.subplot(1, 3, 1)
        
        
        plt.boxplot(df_cvli_por_aisp['cvli'], orientation='vertical', showmeans=True)
        
        plt.title('DISTRIBUIÇÃO DE CVLIs POR BATALHÃO')
        
        plt.xlabel('Crimes Violentos Letais Intencionais')
        
        plt.ylabel('Batalhão')
        plt.yticks([])
        
        
        
        
        # detalhamento das medidas estatisticas que sustentarão as observações acerca dos dados de cvli nos bpms
        # plt.subplot(1, 3, 2)
        plt.subplot(2, 3, 2)
        plt.axis('off')
        
        
        plt.title('RESUMO ESTATÍSTICO')
        
        plt.text(0, 0.9, f'Limite inferior: {limite_inferior:.2f}')
        plt.text(0, 0.8, f'Mínimo: {min_cvli}', fontweight='bold')
        plt.text(0, 0.7, f'Q1: {q1_cvli:.2f}')
        plt.text(0, 0.6, f'Q2 (Mediana): {q2_cvli:.2f}')
        plt.text(0, 0.5, f'Q3: {q3_cvli:.2f}')
        plt.text(0, 0.4, f'Limite superior: {limite_superior:.2f}')
        plt.text(0, 0.3, f'Máximo: {max_cvli}', fontweight='bold')
        
        plt.text(0.5, 0.9, f'Média: {media_cvli:.2f}', fontweight='bold')
        plt.text(0.5, 0.8, f'Mediana: {mediana_cvli:.2f}', fontweight='bold')
        plt.text(0.5, 0.7, f'Distância: {distancia_cvli:.2f}%')
        plt.text(0.5, 0.6, f'IQR: {iqr_cvli:.2f}')
        plt.text(0.5, 0.5, f'Amplitude Total: {amplitude_total}')
        plt.text(0.5, 0.4, f'Variância: {variancia_cvli:.2f}')
        plt.text(0.5, 0.3, f'Assimetria: {assimetria_cvli:.2f}')
        plt.text(0.5, 0.2, f'Curtose: {curtose_cvli:.2f}')
        
        
        
        
        
        # conclusão
        plt.subplot(2, 3, 5)
        plt.axis("off")
        
        plt.title('PERCENTUAL DE CVLI POR AISP')
        
        df_cvli_por_aisp_percent = df_cvli_por_aisp[['aisp', 'cvli']].head(10)
        
        df_cvli_por_aisp_percent['Percentual %'] = (
            df_cvli_por_aisp_percent['cvli'] / df_cvli_por_aisp_percent['cvli'].sum()
            * 100
        ).round(2)
        
        df_cvli_por_aisp_percent = df_cvli_por_aisp_percent.sort_values(
            by='cvli', ascending=False
        )
        

        plt.table(
            cellText=df_cvli_por_aisp_percent.values,
            colLabels=['AISP', 'CVLI', 'Percentual %'],
            loc='center'
        )
        
        
        
        
        # grafico de barras dos bpm que registraram muito mais ocorrencias que os demais
        plt.subplot(2, 3, 3)
        
        plt.title('GRÁFICO DE BARRAS SOBRE OCORRÊNCIAS')
        
        df_cvli_por_aisp_bar = df_cvli_por_aisp_outliers_sup.sort_values(
            by='cvli', ascending=True
        ).copy()
        
        df_cvli_por_aisp_bar['aisp'] = (
            df_cvli_por_aisp_bar['aisp'] + ' - ' + df_cvli_por_aisp_bar['munic']
        )
        
        plt.bar(
                df_cvli_por_aisp_bar['aisp'],
                df_cvli_por_aisp_bar['cvli'],
                edgecolor='black'
            ) 
        
        plt.xticks()
        
        
        
        
        
        #historgrama
        plt.subplot(2, 3, 6)
        
        plt.title('HISTOGRAMA DE CVLIs POR BATALHÃO')
        
        plt.hist((df_cvli_por_aisp['cvli']), bins=15, edgecolor='black')
        plt.xlabel('Crimes Violentos Letais Intencionais')
        plt.ylabel('Frequência')
        
        


        # plt.subplots_adjust(left=0.1, right=0.1)
        plt.tight_layout()
        # plt.show()
        
        
        plt.figure(figsize=(12, 6))
        
            
        plt.title('GRÁFICO DE BARRAS SOBRE OCORRÊNCIAS')
        
        df_cvli_por_aisp_bar = df_cvli_por_aisp.sort_values(
            by='cvli', ascending=True
        ).copy()

        df_cvli_por_aisp_bar['aisp'] = (
            df_cvli_por_aisp_bar['munic'] + ' - ' + df_cvli_por_aisp_bar['aisp']
        )
        
        plt.bar(
                df_cvli_por_aisp_bar['aisp'],
                df_cvli_por_aisp_bar['cvli'],
                edgecolor='black'
            )
        plt.xticks(rotation=45, ha='right')
        
        plt.subplots_adjust(bottom=0.3)
        
        plt.show()
    
    except Exception as e:  # noqa: BLE001
        print(f'Erro ao gerar os graficos - {e}')
