#%%
import pandas as pd

df_clientes = pd.read_csv(r"C:\Users\User\Documents\SCRIPTS PYTHON\machine_learning\data\clientes.csv", sep=';')

df_clientes.head(n=10) # Número de colunas para serem visualizadas
# %%
df_clientes.tail() # Mostra as últimas linhas do DF
# %%
df_clientes.sample(10) # Selecionar n linhas, aleatorias
# %%
df_clientes.shape # Número de linhas e colunas

# %%
df_clientes.columns # Listar colunas

#%%
df_clientes.index 

#%%
df_clientes.info() # Informações sobre o DF
df_clientes.info(memory_usage='deep') # Informações sobre o DF, mas mostra o uso efetivo da memoria ram

#%%
df_clientes.dtypes['flEmail']

#%%
