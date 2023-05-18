from typing import Type, List
from abc import ABC, abstractmethod

class Rule(ABC):
    def __init__(self, name, params) -> None:
        self.name = name
        self.params = params

    @abstractmethod
    def check_rules(self):
        for param in self.params:
            assert param()

class Octosyllable(Rule):
    def __init__(self, name, params) -> None:
        super().__init__(name, params)

class Hendecasyllable(Rule):
    def __init__(self, name, params) -> None:
        super().__init__(name, params)

class SonnetRules(Rule):
    def __init__(self) -> None:
        self.name = "Sonnet Rules"
        self.params = []
        super().__init__(self.name, self.params)

    def check_rules(self):
        return super().check_rules()

class Poetry():
    def __init__(self, text, rules: List[Rule]) -> None:
        self.text = text
        self.rules = rules

    def arrange_verses(self):
        print(self.text)

class Sonnet(Poetry):
    def __init__(self, text, rules) -> None:
        super().__init__(text,rules)


class Poem():
    def __init__(self, author, title, body: Type[Poetry]) -> None:
        self.author = author 
        self.title = title
        self.body = body
    
    def read(self):
        self.body.arrange_verses()
    
    def describe(self):
        print(f"""The poem {self.title} was written by {self.author}. It is a {self.body.__class__.__name__} and it has {len(self.body.text)} verses""")

soneton=Sonnet(["primero viene el verso","luego el segundo verso", "luego el tercero"], SonnetRules())
elsoneto = Poem('Gabriela','soneton', soneton)
elsoneto.read()
elsoneto.describe()
