from typing import Type, List
from abc import ABC, abstractmethod
import sys
# tell interpreter where to look
sys.path.insert(0,"/home/matias/Documents/misRepos/my_little_programs/poetry_api")
from poem.PoemParser import PoemParser
from rules.Rule import  *


class Ruleset(ABC):
    def __init__(self, input, params) -> None:
        self.name = self.__class__.__name__
        self.input = input
        self.params = params
    
    @abstractmethod
    def check_rules(self):
        for param in self.params:
            assert param



class SonnetRules(Ruleset):
    def __init__(self, input: Type[PoemParser]) -> None:
        self.params = [
            Hendecasyllable(input)
        ]
        super().__init__(input,self.params)
        print("Da ok?: ",self.check_rules())

    def check_rules(self):
        checks = []
        for param in self.params:
            checks.append(param.check())
        return all(checks)