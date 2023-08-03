import jsonpickle
from abc import ABC, abstractmethod


class Encoder(ABC):
    def __init__(self, original) -> None:
        self.original = original
        self.encoded = None
    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        return jsonpickle.decode(self.original.get("object"))


class RuleEncoder(Encoder):
    def __init__(self, original) -> None:
        super().__init__(original)

    def serialize(self):
        if not self.encoded:
            serialized={
                "name": self.original.name,
                "object": jsonpickle.encode(self.original)
                }
            self.encoded = serialized
        return self.encoded

    def deserialize(self):
        return super().deserialize()


class RulesetEncoder(Encoder):
    def __init__(self, original) -> None:
        super().__init__(original)

    def serialize(self):
        if not self.encoded:
            serialized={
                "name": self.original.rules.name,
                "rules": [rule for rule in self.original.rules.params],
                "object": jsonpickle.encode(self.original)
                }
            self.encoded = serialized
        return self.encoded

    def deserialize(self):
        return super().deserialize()

class PoetryEncoder(Encoder):
    #Pensar si esto tiene sentido que siga
    def __init__(self, original) -> None:
        super().__init__(original)

    def serialize(self):
        if not self.encoded:
            serialized={
                "name": self.original.name,
                "ruleset": RulesetEncoder(self.original).serialize(),
                "object": jsonpickle.encode(self.original)
                }
            self.encoded = serialized
        return self.encoded

    def deserialize(self):
        return super().deserialize()
    
class PoemEncoder(Encoder):
    def __init__(self, original) -> None:
        super().__init__(original)

    def serialize(self):
        if not self.encoded:
            #poem no deberia estar. Tendria que ser directamente el object para no armar una cadena
            #interminable
            # serialized = {
            #     "author": self.original.author,
            #     "title": self.original.title,
            #     "poem": PoetryEncoder(self.original.body).serialize(),
            #     "object": jsonpickle.encode(self.original)
            # }
            serialized = {
                "author": self.original.author,
                "title": self.original.title,
                "object": jsonpickle.encode(self.original)
            }
            self.encoded = serialized
        return self.encoded

    def deserialize(self):
        return super().deserialize()
    
