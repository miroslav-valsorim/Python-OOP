from Zoo.lizard import Lizard
from Zoo.mammal import Mammal


class Gorilla(Mammal):
    def __init__(self, name: str):
        super().__init__(name)


mammal = Mammal("Stella")

print(mammal.__class__.__bases__[0].__name__)

print(mammal.name)

lizard = Lizard("John")

print(lizard.__class__.__bases__[0].__name__)

print(lizard.name)