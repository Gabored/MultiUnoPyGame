
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
        return f"{self.value_card()} - {self.color}"
    
    def value_card(self):
        ''' Function that prevents from returning None when value is missing in action cards or color cards'''
        if self.number == None:
            return self.action
        else:
            return self.number
    
    