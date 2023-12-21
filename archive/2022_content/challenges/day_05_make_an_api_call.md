<h1 style="font-weight:normal">
  Python Charmers :snake:
</h1>

Learning python through 15 minute daily projects.

### Day 05: Make an API Call

Today we’ll be grabbing some data from an API, parse the JSON code and writing the data to a csv.

**Task: Pip install json & urllib3**

Let's get started

- Open VS Code
- Top Menu Bar > Select ‘Terminal’ > Select ‘New Terminal’
- In the terminal window type:
```
pip install json
pip install urllib3
```

### Tableau Public Search

On Tableau Public you can search through all the published vizzes, for example I can search for "maps" [Tableau Public Search for maps](https://public.tableau.com/app/search/vizzes/maps).

In the background the Tableau Public website is calling an API and so can we. You learn more about finding APIs on webpages here: [Flerlage Twins Blog](https://www.flerlagetwins.com/2021/04/tableau-public-api.html)

Here is the API call, which you can copy and paste to a browser:

[https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=vizzes](https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=vizzes)

Note some variables in this api call:
- count - the number of results returned
- language - default is english
- query - your search term, i.e. 'maps'
- start - how many results you wish to skip
- type - either vizzes or authors

### Make an API call in Python

In python we see this data too:

```
import json
import pandas as pd
import urllib3

api_call = "https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=vizzes"
http = urllib3.PoolManager()
search_call = json.loads(http.request('GET',api_call).data)
print(search_call)
```
The data returned will be in a json format. You can use an online tool to convert this json to a csv, or you can use python.

With the pandas library we can use `json_normalize` to flatten the json into a table format.

```
# convert json to dataframe structure just for search reults
df = pd.json_normalize(search_call['results'], max_level=0)

# Note there are additional nodes in the data frame so we need to
# normalise more nodes to get details of workbooks and authors
workbook_meta = pd.json_normalize(df['workbookMeta'], max_level=0)
workbooks = pd.json_normalize(df['workbook'], max_level=0)

# concat normalized nodes together, axis 1 to concatenate side by side (i.e. join on row number)
search_results = pd.concat([workbook_meta,workbooks], axis=1)

# view the steps here so you can understand what's happening
print(df)
print(workbook_meta)
print(workbooks)
print(search_results)
```

We can then save our results to a csv.
```
# Save locally
search_results.to_csv('output//tableau_public_search_results.csv', index=False)
```

### Tasks

- Run the script [05_tabpub_api_calls.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/05_tabpub_api_calls.py)
- Change up the variables `search_term`, `n_results`, `index`

Note: Tableau does have some limits on the count - you can always double check an api call in the browser

**Bonus Task**

On Github [wjsutton/tableau_public_api](https://github.com/wjsutton/tableau_public_api) I've documented various API calls from Tableau Public, try extracting the data from one of the calls, e.g.

- [VOTD Winners](https://github.com/wjsutton/tableau_public_api#user-content-chart_with_upwards_trend-votd-dashboards)
- [Profile workbook stats](https://github.com/wjsutton/tableau_public_api#user-content-books-workbooks)
- [Fullscreen image of a viz](https://github.com/wjsutton/tableau_public_api#user-content-books-workbook-image)
