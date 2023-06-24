import traceback
from view.PopupView import PopupManager

class Modification:
    def __init__(self, commit, date, type, beforeCode, afterCode, hash, filename) :
        self.commit = commit
        self.date = date
        self.type = type
        self.beforeCode = beforeCode
        self.afterCode = afterCode
        self.hash = hash
        self.filename = filename
    
    def get_commit_hash(self):
        return self.commit
    
    def get_date(self):
        return self.date