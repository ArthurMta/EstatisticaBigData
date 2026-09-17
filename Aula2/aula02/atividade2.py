import pandas as pd
import numpy as np
import os, time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()



### READ dos DOCS



# abrir
df_planilha_custo = pd.read_csv('planilha_de_custos.csv')



### PRINTS



# 

df_planilha_custo['Custo Total'] = (
    df_planilha_custo['Preco de Compra (R$)']
    + (df_planilha_custo['Preco de Compra (R$)'] * (df_planilha_custo['Imposto (%)'] / 100))
    + df_planilha_custo['Frete (R$)']
    + (df_planilha_custo['Preco de Compra (R$)'] * (df_planilha_custo['Taxa Operacional (R$)'] / 100))
)
print(df_planilha_custo)



#
array_custo_total = np.array(df_planilha_custo['Custo Total'])


media_custo_total = np.mean(array_custo_total)
mediana_custo_total = np.median(array_custo_total)

print('\nMEDIDAS DE TENDENCIA CENTRAL\n')
print(f'\n\nMédia: R$ {media_custo_total}\n\n')
print(f'\n\nMediana: R$ {mediana_custo_total}\n\n')

