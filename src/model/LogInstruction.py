import traceback
from view.PopupView import PopupManager

class LogInstruction:
    def __init__(self, instruction, modifications, date):
        self.instruction = instruction
        self.date = date
        if modifications is None:
            self.modifications = []
        else:
            self.modifications = modifications
    
    def add_modification(self, modification):
        if(self.modifications is not None):
            self.modifications.append(modification)