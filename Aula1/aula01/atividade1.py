import pandas as pd

vendas = pd.Series([32, 45, 28, 50, 38, 42])

cancelamentos = pd.Series([3, 5, 2, 8, 4, 6])

print(vendas[2])
print(vendas[[1,3,5]])
print(vendas[vendas > 40])
print((vendas - cancelamentos))