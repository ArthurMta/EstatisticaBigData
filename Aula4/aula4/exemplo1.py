import pandas as pd
from sqlalchemy import create_engine

# conexão
host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula4'

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

###

query1 = 'SELECT * FROM cadastro_produtos;'
df_produtos = pd.read_sql(query1, engine)

# print(df_produtos)

query2 = 'SELECT * FROM cadastro_produtos WHERE `Preço Unitario` > 20;'
df_clientes = pd.read_sql(query2, engine)

print(df_clientes)