import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('sqlite:///db.sqlite3')

df = pd.read_csv('athlete_events.csv')

#dfh = df.head(10)

df.to_sql('olymp_olymp', if_exists='replace', con=engine, index_label='index')
