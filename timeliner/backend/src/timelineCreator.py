import pandas as pd
from os.path import dirname, join
def create(data):
    dataframe = pd.DataFrame(data)
    dataframe['lalala'] = 123
    nnn=1234
    filename=join(dirname(__file__),f'../charts/si{nnn}.html')
    dataframe.to_html(filename)
    return filename