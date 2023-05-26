import os
import sys
fpath = os.path.join(os.path.dirname(os.getcwd()), 'poemParser')
sys.path.append(fpath)
print(sys.path)
from flask import Flask, render_template,request
from Encoders import PoemEncoder
from Poem import todo
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True



allPoems = {idx: PoemEncoder(poem).deserialize()  for idx,poem in enumerate(todo)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/poem/',  methods=['POST'])
def get_poem():
    to_get = allPoems.get(int(request.form['index']))
    if not to_get:
        return render_template('not_found.html')
    return render_template('poem.html.jinja', poem=to_get, single=True)

@app.route('/poemsByAuthor/',  methods=['POST'])
def get_poems_by_author():
    to_get = [poem for poem in allPoems.values() if poem.author == request.form['author']]
    if not to_get:
        return render_template('not_found.html')
    return render_template('poem_container.html.jinja', poems=to_get, author=request.form['author'])