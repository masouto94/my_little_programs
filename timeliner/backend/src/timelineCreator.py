import pandas as pd
from datetime import datetime,timedelta
from os.path import dirname, join
def create(data):
    dataframe = pd.DataFrame(data).sort_values(by='from_date').reset_index().drop('index', axis=1)
    dataframe['from_date'] = dataframe.from_date.apply(lambda x: datetime.fromisoformat(x))
    dataframe['to_date'] = dataframe.to_date.apply(lambda x: datetime.fromisoformat(x))
    nnn=1234
    filename=join(dirname(__file__),f'../charts/si{nnn}.html')
    dataframe.to_html(filename,classes=["table","table-sm"], index=False)
    return filename