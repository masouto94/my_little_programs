import json
from typing import Type, Dict
from abc import ABC, abstractmethod
from parsers.PoemParser import PoemParser 
from rules.Rule import *
from rulesets.Ruleset import *
from encoders.Encoders import *
from database.DatabaseConnector import *


class Poetry(ABC):
    def __init__(self, text: Type[PoemParser], rules: Type[Ruleset] = None) -> None:
        self.name = ""
        self.text = text
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
        self.name="Free"
        self.rules = FreePoemRules(self.text)

class Haiku(Poetry):
    def __init__(self, text: Type[PoemParser]) -> None:
        super().__init__(text)
        self.name="Haiku"
        self.rules = HaikuRules(self.text)

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
    
    @staticmethod
    def from_json(json: dict):
        expected = ["title","author","type","text"]
        assert all([key in json.keys() for key in expected]),f"The following keys: {str(expected)} are expected in json"
        try:
            cls = globals()[json['type']](json['text'])
            return Poem(json['author'], json['title'], cls)
            
        except KeyError:
            raise KeyError(f"Error processing '{json['title']}'.Type '{json['type']}' is not supported yet")



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