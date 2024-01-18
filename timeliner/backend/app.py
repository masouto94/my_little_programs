from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    data = pd.DataFrame(data={"lo":[1,2,3],"le":[9,3,1]})
    return data.to_json()