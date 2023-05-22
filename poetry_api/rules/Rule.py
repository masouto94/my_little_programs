from typing import Type, List
from abc import ABC, abstractmethod
import sys
# tell interpreter where to look
sys.path.insert(0,"/home/matias/Documents/misRepos/my_little_programs/poetry_api")

from poem.PoemParser import PoemParser 

class Rule():
    def __init__(self, input: Type[PoemParser]) -> None:
        self.input = input


    def eleven_syllables(self, input: Type[PoemParser]):        
        result=[]
        for counts in input.get_syllable_count_by_strophe().values():
            result.append(all([i == 11 for i in counts ]))
        return all(result)

    def eight_syllables(self, input: Type[PoemParser]):
        result=[]
        for counts in input.get_syllable_count_by_strophe().values():
            result.append(all([i == 8 for i in counts ]))
        return all(result)
    
class Octosyllable(Rule):
    def __init__(self, input) -> None:
        super().__init__(input)
        params = [
            super().eight_syllables(input)
        ]
        self.params = params

class Hendecasyllable(Rule):
    def __init__(self, input) -> None:
        super().__init__(input)
        params = [
            super().eleven_syllables(input)
        ]
        self.params = params
    def check(self):
        return all(self.params)