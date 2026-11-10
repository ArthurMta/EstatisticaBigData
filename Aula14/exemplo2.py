import pandas as pd
import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import os
import fastparquet
from datetime import datetime

# limpar terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_terminal()





### ENTRADA DE DADOS





ENDEREC0_DADOS = './../.dados/NovoBolsaFamilia/'

try:
    
    inicio = datetime.now()
    
    
    
    
    
    df_bolsa_familia = pl.scan_parquet(ENDEREC0_DADOS+'bolsa_familia.parquet')
    print("Arquivo parquet lido com sucesso!")
    
    print(df_bolsa_familia.collect())
    
    
    fim = datetime.now()
    print(f"Tempo de execução: {fim - inicio}")
    
except Exception as e:
    print(f"Erro ao ler os dados: {e}")





### PROCESSAMENTO DE DADOS



try: 
    
    
    array_valor_parcela = np.array(df_bolsa_familia.select(pl.col("VALOR PARCELA")).collect())
    
    plt.boxplot(array_valor_parcela, orientation='horizontal')
    plt.xlabel("VALOR PARCELA")
    plt.title("Boxplot - VALOR PARCELA")
    
    plt.show()
    

except Exception as e:
    print(f"Erro ao processar os dados: {e}")