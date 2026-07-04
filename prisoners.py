import abc

class Builder(abc.ABC):
    score = 0
    @abc.abstractmethod
    def move(self, moves):
        pass
    
class Peace(Builder):
    def __init__(self):
        self.name = 'Peacefull'
        
    def move(self, moves):
        return 0
    
class Agression(Builder):
    def __init__(self):
        self.name = 'Agressive'
    def move(self, moves):
        return 1
    
class Eye_for_eye(Builder):
    def __init__(self):
        self.name = "Eye_for_eye"
        self.last_move = 0
        
    def move(self, moves):
        if not moves or moves[-1] == 0 or self.last_move == 1:
            return 0
        elif moves[-1] == 1:
            return 1

    
    