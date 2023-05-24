from flask import Flask, render_template,request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/', methods=['GET', 'POST'])
def hello(name=None):
    if request.method == 'POST':
        return render_template('hello.html', name=request.form["greet"])
    return render_template('hello.html', name=name)