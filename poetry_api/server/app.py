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
    unique_authors = list(set([p.author for p in allPoems.values()]))
    unique_types = list(set([p.type for p in allPoems.values()]))
    unique_authors.sort()
    unique_types.sort()
    return render_template('index.html.jinja',
                            current=len(allPoems.values()), 
                            authors=unique_authors,
                            types=unique_types)

@app.route('/poem/',  methods=['POST'])
def get_poem():
    to_get = allPoems.get(int(request.form['index'])-1)
    if not to_get:
        return render_template('not_found.html.jinja')
    return render_template('poem.html.jinja', poem=to_get, single=True)

@app.route('/poemsByAuthor/',  methods=['POST'])
def get_poems_by_author():
    selected = request.form.get('select_author')
    to_get = [poem for poem in allPoems.values() if poem.author == selected]
    
    if not to_get:
        return render_template('not_found.html.jinja')
    return render_template('poem_container.html.jinja', poems=to_get, author=selected)

@app.route('/poemsByType/',  methods=['POST'])
def get_poems_by_type():
    selected = request.form.get('select_type')
    to_get = [poem for poem in allPoems.values() if poem.type == selected]
    
    if not to_get:
        return render_template('not_found.html.jinja')
    return render_template('poem_container.html.jinja', poems=to_get, type=selected)