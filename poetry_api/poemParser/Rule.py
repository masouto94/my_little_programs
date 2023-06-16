from typing import Type, List
from abc import ABC, abstractmethod

from PoemParser import PoemParser 

class Rule(ABC):
    def __init__(self, input: Type[PoemParser], params = None) -> None:
        self.input = input
        self.params= params
        self.name=self.__class__.__name__

    @abstractmethod
    def check(self):
        return all(self.params)


class Free(Rule):
    def __init__(self, input: Type[PoemParser]) -> None:
        super().__init__(input)
        params = [
            self.allow_anything()
        ]
        self.params = params

    def allow_anything(self):
        return True
    def check(self):
        super().check()

class Octosyllable(Rule):
    def __init__(self, input: Type[PoemParser]) -> None:
        super().__init__(input)
        params = [
            self.eight_syllables()
        ]
        self.params = params

    def eight_syllables(self):
        result=[]
        for counts in self.input.get_syllable_count_by_strophe().values():
            result.append(all([i == 8 for i in counts ]))
        return all(result)

    def check(self):
        super().check()

class Hendecasyllable(Rule):
    def __init__(self, input: Type[PoemParser]) -> None:
        super().__init__(input)
        params = [
            self.eleven_syllables()
        ]
        self.params = params

    def eleven_syllables(self):        
        result=[]
        for counts in self.input.get_syllable_count_by_strophe().values():
            result.append(all([i == 11 for i in counts ]))
        return all(result)
    
    def check(self):
        return super().check()

class SonnetStructure(Rule):
    def __init__(self, input: Type[PoemParser]) -> None:
        super().__init__(input)
        params = [
            self.two_quartets_first(),
            self.two_tercets_second(),
            self.four_strophes_total()
        ]
        self.params = params

    def two_quartets_first(self):        
        result=[]
        pairing = self.input.get_syllable_count_by_strophe()
        result.append(len(pairing.get(0))==4)
        result.append(len(pairing.get(1))==4)
        return all(result)
   
    def two_tercets_second(self):        
        result=[]
        pairing = self.input.get_syllable_count_by_strophe()
        result.append(len(pairing.get(2))==3)
        result.append(len(pairing.get(3))==3)
        return all(result)
    
    def four_strophes_total(self):        
        return len(self.input.strophes) == 4
    
    def check(self):
        return super().check()

class TotalVerses(Rule):
    def __init__(self, input: Type[PoemParser], amount) -> None:
        super().__init__(input)
        self.amount = amount
        params = [
            self.count_verses(),
        ]
        self.params = params
    
    def count_verses(self):        
        return len(self.input.verses) == self.amount

    def check(self):
        return super().check()