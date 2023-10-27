import requests as r
import pandas as pd



html = r.get("https://lots-project.com/",verify=False)
dfs = pd.read_html(html.text)

lots_table = dfs[0]
urls = lots_table.iloc[:,0]
urls = urls.str.lstrip('*')
urls.to_csv("lots.csv", index=False, header=False)
