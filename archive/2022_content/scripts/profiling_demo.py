import pandas as pd
from ydata_profiling import ProfileReport

# Load csv
df = pd.read_csv('https://raw.githubusercontent.com/wjsutton/games_night_viz/main/challenges/5_montages/cod_mw_players.csv')

# ProfileReport will build a report of your dataset and write it as a html file
profile = ProfileReport(df, title="Call of Duty Modern Warfare Players", explorative=True)
profile.to_file("cod_report.html")