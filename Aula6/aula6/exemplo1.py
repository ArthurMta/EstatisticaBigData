import os

from sqlalchemy import create_engine
import pandas as pd

from dotenv import load_dotenv



# Carrega variaveis de ambiente
load_dotenv()

def conecta_banco():
    
    # Cria a engine de conexão com o banco de dados
    engine = create_engine(
        
        f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'
        
        )
    
    return engine

engine = conecta_banco()

try:
    df_usuarios = pd.read_sql('tb_usuarios', engine)
    df_livros = pd.read_sql('tb_livros', engine)
    df_alugados = pd.read_sql('tb_alugados', engine)
    df_itens = pd.read_sql('tb_itens_alugados', engine)
    print(df_usuarios)
    
except Exception as e:
    print(f"Erro : {e}") 
    
    
try:
    df_merge1 = pd.merge(
        df_livros, df_itens, on='id_livro'
    )
    
    print(df_merge1)
except Exception as e:
    print(f"Erro : {e}") 