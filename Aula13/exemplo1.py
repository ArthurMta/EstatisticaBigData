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
    
    
    
    
    #Polars
    
    df_janeiro_polars = pl.read_csv(ENDEREC0_DADOS + '202601_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')
    
    
    print(df_janeiro_polars.head(10))

except Exception as e:  # noqa: BLE001
    print(f'Erro ao obter dados -  {e}')





### TRATAMENTO DE DADOS





#











#calculo de tempo de execução
fim = datetime.now()
print(f'Tempo de execução: {fim - inicio}')