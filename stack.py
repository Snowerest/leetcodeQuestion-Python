class Stack(object):
    def __init__(self):
        self.__v = []
        
    def is_empty(self) -> bool:
        return self.__v == []
        
    def push(self, value: object) -> None:
        self.__v.append(value)
        
    def pop(self) -> object:
        if self.is_empty():
            return None
        value = self.__v[-1]
        self.__v = self.__v[:-1]
        return value
    
