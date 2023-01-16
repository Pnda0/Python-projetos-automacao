import pandas as pd

dados = pd.read_excel(r'C:\Users\Alan\Downloads\AD Promotora\Robôs\Esteira\C6\REAPRESENTAÇÃO C6.xlsx')

df = pd.DataFrame(dados)

print(df.head())

nova_entrada = ["AD Promotora", 1111.45, 341, 522, '2270-1', "corrente", "siape", "Xaro Menezes", 4848976548, 886695874]

df.loc[len(df)] = nova_entrada

print(df.head())

df.to_csv('C6porra.xlsx')