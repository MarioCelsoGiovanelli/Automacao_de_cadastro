import pandas as pd
import script

# Lendo o arquivo Excel:

df = pd.read_excel('cadastro_clientes.xlsx')
script.cadastro_web(df)