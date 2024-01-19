from flask import Flask, send_file
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    data = pd.DataFrame(data={"lo":[1,2,3],"le":[9,3,1]})
    data.to_csv('./data.csv')
    
    return send_file('./data.csv')