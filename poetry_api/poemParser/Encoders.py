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
                "name": self.original.name,
                "rules": [rule.name for rule in self.original.params],
                "object": jsonpickle.encode(self.original)
                }
            self.encoded = serialized
        return self.encoded

    def deserialize(self):
        return super().deserialize()

class PoetryEncoder(Encoder):
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
    
class PoemEncoder(Encoder):
    def __init__(self, original) -> None:
        super().__init__(original)
    
    def serialize(self):
        if not self.encoded:
            serialized = {
                "author": self.original.author,
                "title": self.original.title,
                "type": self.original.body.name,
                "object": jsonpickle.encode(self.original)
            }
            self.encoded = serialized
        return self.encoded

    def deserialize(self):
        return super().deserialize()
    
