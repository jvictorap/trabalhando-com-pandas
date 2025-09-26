# %%

import pandas as pd

df = pd.read_clipboard() # É criado um DF com o que estiver no 'ctrl + c'

#%%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

# simula um navegador
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# agora lê o HTML com o pandas
dfs = pd.read_html(response.text)

print(dfs[0].head())  # exibe as primeiras linhas da primeira tabela

# %%
print(len(dfs))   # quantas tabelas encontrou

#%%

dfs[1].to_excel("Informações sobre as unidades federativas.xlsx", index=False)
# %%
