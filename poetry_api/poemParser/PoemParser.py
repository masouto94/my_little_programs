from pyverse import Pyverse

class PoemParser():
    def __init__(self, poem_string) -> None:
        self.initial = poem_string
        self.parsed = self.parse_all(self.initial)

    def get_strophes(self, whole_poem):
        return [strophe for strophe in whole_poem.split("\n\n")]

    def get_verses(self, strophe):
        return [verse for verse in strophe.split("\n")]

    def parse_all(self,poem):
        strophes = self.get_strophes(poem)
        verses=[]
        parsed={}
        for i, strophe in enumerate(strophes):
            parsed[i] = {"verses":self.get_verses(strophe)}
            verses.append(parsed[i].get("verses"))
            parsed[i]["syllables"] = [Pyverse(verse).count for verse in parsed[i]["verses"]]
        self.strophes = verses
        self.verses = [verse for verses in self.strophes for verse in verses]
        return parsed
    
    def get_syllable_count_by_strophe(self):
        return {key:val["syllables"] for key,val in self.parsed.items() }
    
    def get_verse(self,index):
        try:
            if len(index) != 2:
                raise IndexError("Index must be int or an array of size 2")
            return self.strophes[index[0]][index[1]]
        except TypeError:
            return self.verses[index]
    def check_metric(self):
        result=[]
        for counts in self.get_syllable_count_by_strophe().values():
            result.append(all([i == 8 for i in counts ]))
        return all(result)

    def check_structure(self):
        result=[]
        for strophe, counts in self.get_syllable_count_by_strophe().items():
            if strophe in (0,1):
                result.append(len(counts) == 4)
            elif strophe in (2,3):
                result.append(len(counts) == 3)
            else:
                result.append(False)
        return all(result)


#TODO: ver como hacer que 'Empieza a' y la "y" sea sinalefa
# hernandez="""Empieza a vivir, y empieza
# a morir de punta a punta
# levantando la corteza
# de su madre con la yunta."""
# hernandez_poem=PoemParser(hernandez)

