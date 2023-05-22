from typing import Type, List
from abc import ABC, abstractmethod
from PoemParser import PoemParser 
import sys
# tell interpreter where to look
sys.path.insert(0,"/home/matias/Documents/misRepos/my_little_programs/poetry_api")
from rules.Rule import *
from rulesets.Ruleset import *



class Poetry():
    def __init__(self, text: str, rules: List[Rule] = None) -> None:
        self.text = PoemParser(text)
        self.rules = rules

    def arrange_verses(self):
        print(self.text.parsed)


class Sonnet(Poetry):
    def __init__(self, text) -> None:
        self.name="Sonnet"
        super().__init__(text)
#        self.rules = SonnetRules(11)
        self.rules = SonnetRules(self.text)

class Free(Poetry):
    def __init__(self, text, rules=None) -> None:
        super().__init__(text)
        self.name="Free poem"
        self.rules = []

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

    def read(self):
        self.body.arrange_verses()
    
    def describe(self):
        print(f"""The poem '{self.title}' was written by {self.author}. It is a {self.body.name} and it has {len(self.body.text.verses)} verses""")



from database.to_import import poems_list
todo=[]
for poem in poems_list:
    try:
        cls = globals()[poem['type']](poem['text'])
        item = Poem(poem['author'], poem['title'], cls)
        todo.append(item)
    except KeyError:
        print(f"Error processing '{poem['title']}'.Type {poem['type']} is not supported yet")
        continue


# todo[1].describe()


# print(Hendecasyllable(todo[0].parsed).input)
print(todo[0].body.rules.params)
