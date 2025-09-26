# %%
import pandas as pd

df = pd.read_csv(r"C:\Users\User\Documents\SCRIPTS PYTHON\machine_learning\data\clientes.csv")

# %%
df
# %%
df.to_csv("Clientes.csv", index=False)
# %%
df.to_parquet("clientes.parquet")
# %%

df.to_excel("clientes.xlsx", index=False)
# %%
