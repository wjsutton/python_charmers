import json
import pandas as pd
import urllib3

# do API call to search for top 20 "maps" from Tableau Public search
search_term = 'maps'
n_results = '20'
index = '0'

api_call = "https://public.tableau.com/api/search/query?count=" + n_results + "&language=en-us&query=" + search_term + "&start=" + index + "&type=vizzes"
http = urllib3.PoolManager()
search_call = json.loads(http.request('GET',api_call).data)

# convert json to dataframe structure just for search reults
df = pd.json_normalize(search_call['results'], max_level=0)

# Note there are additional nodes in the data frame so we need to
# normalise more nodes to get details of workbooks and authors
workbook_meta = pd.json_normalize(df['workbookMeta'], max_level=0)
workbooks = pd.json_normalize(df['workbook'], max_level=0)

# concat normalized nodes together, axis 1 to concatenate side by side (i.e. join on row number)
search_results = pd.concat([workbook_meta,workbooks], axis=1)
print(search_results)

# Save locally
search_results.to_csv('output//tableau_public_search_results.csv', index=False)
