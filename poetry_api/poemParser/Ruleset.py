from typing import Type, List
from abc import ABC, abstractmethod
from PoemParser import PoemParser
from Rule import  *


class Ruleset(ABC):
    def __init__(self, input, params) -> None:
        self.name = self.__class__.__name__
        self.input = input
        self.params = params
    
    @abstractmethod
    def check_rules(self):
        checks = []
        for param in self.params:
            checks.append(param.check())
        return all(checks)



class SonnetRules(Ruleset):
    def __init__(self, input: Type[PoemParser]) -> None:
        self.params = [
            Hendecasyllable(input),
            TotalVerses(input,14),
            SonnetStructure(input)
        ]
        super().__init__(input,self.params)

    def check_rules(self):
        return super().check_rules()

class FreePoemRules(Ruleset):
    def __init__(self, input: Type[PoemParser]) -> None:
        self.params = [
            Free(input)
        ]
        super().__init__(input,self.params)
        

    def check_rules(self):
        return super().check_rules()
