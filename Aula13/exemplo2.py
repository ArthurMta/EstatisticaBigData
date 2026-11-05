import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import polars as pl
import os
from datetime import datetime

# limpar terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_terminal()

inicio = datetime.now()





### ENTRADA DE DADOS





ENDEREC0_DADOS = './../.dados/'

try:
    
    
    # df_janeiro = pd.read_csv(ENDEREC0_DADOS + '202601_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')
    # tempo para ler = 17.67seg
    
    # df_fevereiro = pd.read_csv(ENDEREC0_DADOS + '202602_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1 ')
    # tempo para ler = 18.09seg
    
    # df_marco = pd.read_csv(ENDEREC0_DADOS + '202603_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1 ')
    # tempo para ler = 16.39seg
    
    
    lista_meses_arquivos = ['202601_NovoBolsaFamilia.csv', '202602_NovoBolsaFamilia.csv', '202603_NovoBolsaFamilia.csv']
    
    
    # df principal
    df_bolsa_familia = None
    
    # add meses ao df principal
    for arquivo in lista_meses_arquivos:
        
        df_mes_bolsa_familia = pl.read_csv(ENDEREC0_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        
        # se dfbolsafamilia nao estiver vazio, LOGO concatena o dfbolsafamilia com o df proximo mes
        if df_bolsa_familia is not None:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df_mes_bolsa_familia]) 
        # se dfbolsafamilia estiver vazio, LOGO atribui o df do mes ao dfbolsafamilia
        else:
            df_bolsa_familia = df_mes_bolsa_familia
            
        del df_mes_bolsa_familia  # libera memoria do df do mes
    
    
    # teste
    print(df_bolsa_familia.head(10))

except Exception as e:  # noqa: BLE001
    print(f'Erro ao obter dados -  {e}')





### TRATAMENTO DE DADOS





#











#calculo de tempo de execução
fim = datetime.now()
print(f'Tempo de execução: {fim - inicio}')