import pandas as pd
from datetime import datetime,timedelta
from os.path import dirname, join
import plotly.express as px
from matplotlib import transforms

def setup_dataframe(data):
    dataframe = pd.DataFrame(data).sort_values(by='from_date').reset_index().drop('index', axis=1)
    dataframe['from_date'] = dataframe.from_date.apply(lambda date: datetime.fromisoformat(date))
    dataframe['to_date'] = dataframe.to_date.apply(lambda date: datetime.fromisoformat(date))
    return dataframe
def create(data):
    dataframe = setup_dataframe(data)
    #filename=join(dirname(__file__),f'../charts/table{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.html')
    filename=join(dirname(__file__),f'../charts/table{123}.html')
    dataframe.to_html(filename,classes=["table","table-sm"],justify='center', index=False)
    return filename

def render_timeline(data):
    dataframe = setup_dataframe(data)
    layout = dict(
        xaxis=dict(
            tickmode="array",
            tickvals=dataframe.from_date,
            ticktext=dataframe.from_date.tolist(),
            tickformat='%Y-%m-%d',
            tickangle=45,
        )
    )
    fig = px.timeline(dataframe,
                      x_start="from_date",
                      x_end="to_date",
                      y="episode",
                      text="episode",
                      color_discrete_sequence=["tan"]
                      )
    fig.update_layout(layout)
    filename = join(dirname(__file__),f'../charts/chart{123}.html')
    fig.write_html(filename )
    return filename