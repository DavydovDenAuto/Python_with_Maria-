# mvc_exceptions.py
class ItemAlreadyStored(Exception):
    def __init__(self, message):
        self.message = message
       
    def __str__(self):
        return self.message
    


class ItemNotStored(Exception):
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return self.message
