from typing import Type
from abc import ABC, abstractmethod
from PoemParser import PoemParser 
from Rule import *
from Ruleset import *
from Encoders import *


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
todo=[]
for poem in poems_list:
    try:
        cls = globals()[poem['type']](poem['text'])
        item = Poem(poem['author'], poem['title'], cls)
        encoded=PoemEncoder(item)
        todo.append(encoded.serialize())
    except KeyError:
        print(f"Error processing '{poem['title']}'.Type {poem['type']} is not supported yet")
        continue



# print(todo[0].get('poem').get('ruleset').get('rules'))
# print(type(PoemEncoder(todo[0]).deserialize()))