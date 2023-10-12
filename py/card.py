
class Card:
    '''Card Python Class that represents the Uno Card '''
    def __init__(self, color:str=None, number:int=None, action:str= None) -> None:
        self.color = color
        self.number = number
        self.action = action

    def __str__(self) -> str:
        ''' Returns str print of attributes of a Card instance'''
        return f"{self.number} {self.action}"

    def __repr__(self) -> str:
        ''' Returns str print of attributes including color of a Card Instance'''
        return f"{self.number} {self.color} {self.action}"
    