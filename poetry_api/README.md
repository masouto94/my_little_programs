# Poems for everyone

## Overview
This repo is divided in two modules: 
    
- `poemParser`: Has the models and local database for all poems. New poems can be saved by executing the corresponding lines in `main.py`

- `server`: Contains a web app visualization that retrieves all saved poems and render them using `flask`

## How it works

This framework is targeted to students or teachers of poetry in spanish and general public that just want to organize or study their collection in a different way. 

### A journey from art to data
The first question is...how can we compute something as complex as a poem? In order to do that, we must take the original poem and represent it as an object. We will have a `title`, `author`, `type`, and `text`. After that, we can:

1) Access the title, author, type, and full text
2) Count the strophes by searching double line breaks (`\n\n`)
3) Count the verses as every single line break (`\n`)
4) Calculate the syllables of each verse (*Credits to Nebur for his amazing work creating [pyverse package](https://github.com/neburnodrog/Pyverse)*)

To do all this, we use the `PoemParser` class: We just need to create an instance of `PoemParser` with the poem string. This object will let us access all these items easily

### About poetry beyond structure
After parsing the original poem string, we should analyze what kind of poem it is. Different schools and traditions have, sometimes, very rigid rules of rhyme, metric, or structure. For this we can use the `Poetry` class and its derivates.

To build a `Poetry` object we need the previously parsed text, and a set of rules that represent a given structure. For this we have the `Ruleset` class. We create different rulesets by arranging specific `Rule` objects. 
Rules can be the max length of verses, the total amount of verses, the metric of certain strophe, etc.

So, to summarize, we can create different `Poetry` objects, such as `Sonnet` or `Haiku` with their corresponding parsed text and their ruleset or even `Free` that allows anything 

### The `Poem` object
`Poem` objects are built with the `title`, `author`, and `body` (instance of `Poetry`). They are the class to properly access all the previously described attributes and methods.

They are also the object that will be saved in the database through the `PoemEncoder`


## To install locally

Create a virtual env with `venv` with version `3.11.3`

Example
```bash
// Windows
py -3.11.3 -m venv venv
source venv/Scripts/activate

// Linux
python3 -3.11.3 -m venv venv
source venv/bin/activate

```

Install `requirements.txt`

```
pip install -r requirements.txt
```

### Import or manage poems

To run the framework locally, use `main.py`. There you can access `DatabaseConnector` and have full control of the database. You can pass new poems as a list with the following structure:

```python
from database.DatabaseConnector import DatabaseConnector

poems_list = [
    {
        "title": "poemTitle",
        "author":"Author",
        "type": "PoemType", # Use 'Free' if it does not have a determined type
        "text": """Text body"""
    }
]
db = DatabaseConnector('poemParser/database/poems.db')
db.import_poems(poems_list)
```


### Run flask server

```
cd poetry_api/server
flask run
```

