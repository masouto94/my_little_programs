import os
import sys
fpath = os.path.join(os.path.dirname(os.getcwd()), 'poemParser')
sys.path.append(fpath)
from flask import Flask, render_template,request
from poemParser.poem.Poem import *
from poemParser.parsers.PoemParser import PoemParser
from poemParser.encoders.Encoders import PoemEncoder
from poemParser.database.DatabaseConnector import DatabaseConnector
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = DatabaseConnector('../poemParser/database/poems.db')
poems = db.select('select author,title,object from poems')

def rebuild_poems(poems:List[tuple]) -> Dict[int, Poem]:
    """Returns a dict of `Poem` objects indexed by enumeration from a query of object`

    Args:
        poems (List[tuple]): Query result

    Returns:
        Dict[int, Poem]: Dict of poems
    """
    _allPoems = {}
    for idx,_poem in enumerate(poems):
        try:
            author,title,poem_object = _poem
            deserialized = PoemEncoder.deserialize_object( poem_object)
            _allPoems[idx] = deserialized
        except:
            print(f"Failed to load poem {title} from {author}")
    return _allPoems
allPoems = rebuild_poems(poems)
print(allPoems[0])


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
    to_get = {i:poem for i,poem in allPoems.items() if poem.author == selected}
    
    if not to_get:
        return render_template('not_found.html.jinja')
    return render_template('poem_container.html.jinja', poems=to_get.items(), author=selected)

@app.route('/poemsByType/',  methods=['POST'])
def get_poems_by_type():
    selected = request.form.get('select_type')
    to_get = {i:poem for i,poem in allPoems.items() if poem.type == selected}
    
    if not to_get:
        return render_template('not_found.html.jinja')
    return render_template('poem_container.html.jinja', poems=to_get.items(), type=selected)