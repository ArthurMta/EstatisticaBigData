import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Obtendo os dados
try:
    print('Obtendo os dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # print(df_ocorrencias)

    # delimitando os dados
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    # print(df_roubo_veiculo.head(30))
    # print(df_roubo_veiculo.tail(30))


    # ### PREPARANDO OS DADOS
    # Totalizando os roubos por cidade (Var Qualitativa 'munic' e Var Quant 'roubo_veiculo')
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()


    # Ordenando os dados
    df_roubo_veiculo = df_roubo_veiculo.sort_values(
        by='roubo_veiculo',
        ascending=False
    )

    print(df_roubo_veiculo.head(10))
    # print(df_roubo_veiculo.tail(10))

except Exception as e:
    print(f'Erro ao obter os dados - {e}')



try:
    print('\nObtendo informações a cerca dos roubos dos veículos...')
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs(
        (media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo * 100
    )

    print('\nMedidas de Tendência Central')
    print(f'Média: {media_roubo_veiculo}')
    print(f'Mediana: {mediana_roubo_veiculo}')
    print(f'Distância Média - Mediana: {distancia:.2f}%')


except Exception as e:
    print(f'Obtendo Medidas - {e}')



# Calculando os quartis
try:
    print('\nSeparando os quartis...')
    q1 = np.quantile(array_roubo_veiculo, .25)
    q2 = np.quantile(array_roubo_veiculo, .50)
    q3 = np.quantile(array_roubo_veiculo, .75)

    print('\nMedidas de Posição')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

    # Cidades c/ menos ocorrências de roubos
    df_roubo_veiculo_menores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] < q1
    ]

    # Cidades c/ maiores ocorrências de roubos
    df_roubo_veiculo_maiores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] > q3
    ]

    # Menores
    print('\nMunicípios com menores roubos')
    print(30*'-')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))
    # Exportando o dataframe
    # index=False - Não exporta os índices. Salva os dados das colunas munic e roubo_veiculo
    # sep=';' - Altera o separador de colunas para ';'
    # encoding='iso-8859-1' - Informa o encoding para salvar o csv. "Pode ser o mesmo"
    df_roubo_veiculo_menores.to_csv('menores.csv', index=False, sep=';', encoding='iso-8859-1')

    # Maiores
    print('\nMunicípios com maiores roubos')
    print(30*'-')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))
    # Exportando o dataframe
    df_roubo_veiculo_maiores.to_csv('maiores.csv', index=False, sep=';', encoding='iso-8859-1')


except Exception as e:
    print(f'Erro ao analizar a distribuição {e}')


# Medida de posição e dispersão
try:
    print('\nCalculando a Amplitude Total')
    amplitude_total = np.max(array_roubo_veiculo) - np.min(array_roubo_veiculo)
    
except Exception as e:
    print(f'Erro ao calcular medidas: {e}')

# Achando os outliers
try:
    # Intervalo Interquartil
    # É a amplitude dos dados mais centrais
    iqr = q3 - q1

    # calculando os limites
    # Superior
    limite_superior = q3 + (1.5 * iqr)

    # Inferior
    limite_inferior = q1 - (1.5 * iqr)


    print(f'\nLimite Superior: {limite_superior}')
    print(f'\nLimite Inferior: {limite_inferior}')

    # Filtrando os outliers menores
    df_roubo_veiculo_outliers_menores = (
        df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]
    )

    # Printando os outliers menores
    print('\nMunicípios com outliers inferiores')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_menores) == 0:
        print('Não há outliers Inferiores')
    else:
        print(df_roubo_veiculo_outliers_menores)
    

    # Printando os outliers maiores
    df_roubo_veiculo_outliers_maiores = (
        df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]
    )

    print('\nMunicípios com outliers superiores')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_maiores) == 0:
        print('Não há outliers Superiores')
    else:
        print(df_roubo_veiculo_outliers_maiores)

except Exception as e:
    print(f'Erro ao calcular os outliers {e}')
    
    
try:
    
    print('\n\nMostrando as medidas..\n\n')
    
    print(30*'-')
    print(f'Minimo: {np.min(array_roubo_veiculo)}')
    print(f'Limite Inferior: {limite_inferior}')
    print('\n\n')
    print(f'q1: {q1}')
    print(f'q2: {q2}')
    print(f'q3: {q3}')
    print('\n\n')
    print(f'Maximo: {np.max(array_roubo_veiculo)}')
    print(f'Limite Superior: {limite_superior}')
    
    print(30*'-')
    print('\n\n')
    print(f'Média: {media_roubo_veiculo}')
    print(f'Mediana: {mediana_roubo_veiculo}')
    print(f'Distância: {distancia:.2f}%')
    print(f'Iqr: {iqr}')
    print(f'Amplitude Total: {amplitude_total}')

    
except Exception as e:
    print(f'Erro ao mostrar medidas: {e}')
    
    

# plotando grafico

try:
    print('\n\nPlotando boxplot...')
    
    plt.figure(figsize=(17, 9))

    plt.subplot(1, 2, 1)
    
    plt.boxplot(df_roubo_veiculo['roubo_veiculo'], orientation='horizontal', showmeans=True)
    plt.title('Distribuição dos Dados de Roubo de Veículos')
    plt.xlabel('Roubos de Veículos')
    plt.ylabel('Municípios')
    
    # plot sem x e y 
    plt.subplot(1, 2, 2)
    plt.axis('off')
    plt.title('Resumo Estatístico')
    
    plt.text(0.1,0.95, f'Limite Inferior: {limite_inferior}')
    plt.text(0.1,0.9, f'Mínimo: {np.min(array_roubo_veiculo)}')
    plt.text(0.1,0.85, f'Q1: {q1}')
    plt.text(0.1,0.8, f'Q2: {q2}')
    plt.text(0.1,0.75, f'Q3: {q3}')
    plt.text(0.1,0.7, f'Limite Superior: {limite_superior}')
    plt.text(0.1,0.65, f'Máximo: {np.max(array_roubo_veiculo)}')
    
    
    plt.text(0.1,0.55, f'Média: {media_roubo_veiculo}')
    plt.text(0.1,0.5, f'Mediana: {mediana_roubo_veiculo}')
    plt.text(0.1,0.45, f'Distância: {distancia:.2f}%')
    plt.text(0.1,0.4, f'IQR: {iqr}')
    plt.text(0.1,0.35, f'Amplitude Total: {amplitude_total}')
    
    
    
    plt.suptitle('Informações de Roubo de Veículos')
    
    plt.show()
    
    
    
except Exception as e:
    print(f'Erro ao plotar o gráfico: {e}')