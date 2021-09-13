import pandas as pd
df_json = pd.read_json('/home/tf-dev-01/workspace_sol/wn/rina/rina/wine.json')
df_json.to_excel('./wine.xlsx')