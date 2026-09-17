import pandas as pd
import os, time
import tkinter


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()



### READ dos DOCS



# abrir
df_roupas = pd.read_excel('vendas_roupas.xlsx')



### PRINTS



total_vendido = df_roupas['Unidades Vendidas'].sum()
media_prodts = df_roupas['Preco por Unidade (R$)'].mean()

max_fat = df_roupas['Faturamento Total (R$)'].max()
min_fat = df_roupas['Faturamento Total (R$)'].min()

pc_maior_fat = df_roupas[df_roupas["Faturamento Total (R$)"] == max_fat]['Produto']
pc_menor_fat = df_roupas[df_roupas["Faturamento Total (R$)"] == min_fat]['Produto']

time.sleep(5)
print('\n' + ('=' * 50) +'\n'+ '            RESUMO DAS VENDAS DE ROUPAS' +'\n'+ ('=' * 50))
print(f'Unidades vendidas       : {total_vendido}')
print(f'Preço médio por unidade : R$ {media_prodts:,.2f}')
print(f'Maior faturamento       : R$ {max_fat:,.2f}')
print(f'Menor faturamento       : R$ {min_fat:,.2f}')
print('=' * 50)


print('\n\n')
time.sleep(5)

print('\n' + ('=' * 50) +'\n'+ '            PEÇAS COM MENOR/MAIOR FATURAMENTO' +'\n'+ ('=' * 50))
print(f'Peça com Maior Faturamento  : {pc_maior_fat.to_string(index=False)}')
print(f'Peça com Maior Faturamento  : {pc_menor_fat.to_string(index=False)}')


print('\n\n')
time.sleep(5)


print('\n' + ('=' * 50) +'\n'+ '            MELHOR/PIOR SATISFAÇÃO EM PEÇAS' +'\n'+ ('=' * 50))
print(f'Peça com Maior Satsfação  :\n{df_roupas[df_roupas["Satisfacao"] == 'MUITO ALTO']['Produto'].to_string(index=False)}\n')
print(f'Peça com Menor Satsfação  :\n{df_roupas[df_roupas["Satisfacao"] == 'BAIXO']['Produto'].to_string(index=False)}')
