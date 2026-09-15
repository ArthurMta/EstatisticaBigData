import pandas as pd


# importar como df o arquivo vendas_eletronicos.xlsx
df_vendas_eletronicos = pd.read_excel('./Aula1/atividade2/vendas_eletronicos.xlsx')


# max e minimo de prodts em seus faturamentos da tabela
max = df_vendas_eletronicos["Faturamento Total (R$)"].max()
min = df_vendas_eletronicos["Faturamento Total (R$)"].min()



# prins em abela com prodt e faturamento


print(f'''\nPRODUTO COM MAIOR FATURAMENTO:\n\n{
    df_vendas_eletronicos[df_vendas_eletronicos["Faturamento Total (R$)"] == max]
    [['Produto', 'Faturamento Total (R$)']]
      }\n\n''')

print(f'''\nPRODUTO COM MENOR FATURAMENTO:\n\n{
    df_vendas_eletronicos[df_vendas_eletronicos["Faturamento Total (R$)"] == min]
    [['Produto', 'Faturamento Total (R$)']]
      }\n\n''')