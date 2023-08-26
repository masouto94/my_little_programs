from typing import Type
from abc import ABC, abstractmethod
from parsers.PoemParser import PoemParser 
from rules.Rule import *
from rulesets.Ruleset import *
from encoders.Encoders import *
from database.DatabaseConnector import *
db = DatabaseConnector('poemParser/database/poems.db')


class Poetry(ABC):
    def __init__(self, text: str, rules: Type[Ruleset] = None) -> None:
        self.name = ""
        self.text = PoemParser(text)
        self.raw_text = self.text.initial
        self.rules = rules

    def arrange_verses(self):
        print(self.raw_text)


class Sonnet(Poetry):
    def __init__(self, text: Type[PoemParser]) -> None:
        super().__init__(text)
        self.name="Sonnet"
        self.rules = SonnetRules(self.text)

class Free(Poetry):
    def __init__(self, text: Type[PoemParser]) -> None:
        super().__init__(text)
        self.name="Free poem"
        self.rules = FreePoemRules(self.text)

class Poem():
    def __init__(self, author, title, body: Type[Poetry]) -> None:
        self.author = author 
        self.title = title
        self.body = body
    
    @property 
    def verses(self):
        return self.body.text.verses
    
    @property 
    def strophes(self):
        return self.body.text.strophes

    @property 
    def parsed(self):
        return self.body.text.parsed

    @property 
    def type(self):
        return self.body.name
    def read(self):
        self.body.arrange_verses()
    
    def describe(self):
        return f"""The poem '{self.title}' was written by {self.author}. It is a {self.type} and it has {len(self.body.text.verses)} verses"""



from to_import import poems_list
for poem in poems_list:
    try:
        if not db.poem_exists(poem['title'], poem['author']):
            cls = globals()[poem['type']](poem['text'])
            item = Poem(poem['author'], poem['title'], cls)
            encoded=PoemEncoder(item)
            db.save_poem(encoded)
        else:
            print(f"Poem {poem['title']} from {poem['author']} already exists")

    except KeyError:
        print(f"Error processing '{poem['title']}'.Type {poem['type']} is not supported yet")
        continue

allPoems = {}
for idx,poem in enumerate(db.select('select object from poems')):
    allPoems[idx] = PoemEncoder.deserialize_object( poem[0])

for a in allPoems.values():
    print(a.author)

unique_authors = list(set([p.author for p in allPoems.values()]))
print(unique_authors)