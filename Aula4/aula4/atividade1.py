import pandas as pd
from sqlalchemy import create_engine

# conexao

host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula4'

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

# querys

query1 = 'SELECT * FROM materiais_construcao;'
df_materiais = pd.read_sql(query1, engine)

query2 = 'SELECT Produto, Preco FROM materiais_construcao;'
df_produtos = pd.read_sql(query2, engine)

query3 = 'SELECT * FROM materiais_construcao WHERE Categoria = "Cimento";'
df_cimento = pd.read_sql(query3, engine)

query4 = 'SELECT * FROM materiais_construcao WHERE Preco > 200;'
df_preco = pd.read_sql(query4, engine)

print('ATIVIDADE 1')
print(df_materiais)
print('\n\n\n')

print('ATIVIDADE 2')
print(df_produtos)
print('\n\n\n')

print('ATIVIDADE 3')
print(df_cimento)
print('\n\n\n')

print('ATIVIDADE 4')
print(df_preco)