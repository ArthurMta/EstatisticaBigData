import polars as pl
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
    
    
    df_bolsa_familia = None
    
    arquivos = []
    
    lista_arquivos = os.listdir(ENDEREC0_DADOS)
    
    for arquivo in lista_arquivos:
        if arquivo.endswith('.csv'):
            arquivos.append(arquivo)
    
    for arquivo in arquivos:
        #concat dos arquivos
        df_temp = pl.read_csv( ENDEREC0_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        
        if df_bolsa_familia is None:
            df_bolsa_familia = df_temp
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df_temp])
        
        print(f"Arquivo {arquivo} lido com sucesso!")
    
    
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col("VALOR PARCELA")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    
    #salvando em arquivo parquet
    print("Salvando em arquivo parquet...")
    df_bolsa_familia.write_parquet(ENDEREC0_DADOS + 'bolsa_familia.parquet')
    
    
    
    
    
    fim = datetime.now()
    print(f"Tempo de execução: {fim - inicio}")
    
except Exception as e:
    print(f"Erro ao ler os dados: {e}")