class Queue(object):
    def __init__(self):
        self.__q = []
        
    def push(self, value: object) -> None:
        """ push to queue
        
        :param value: the item will be pushed to queue
        :return: None
        
        """
        self.__q.append(value)
        
    def pop(self) -> object:
        if self.__q == []:
            return None
        value = self.__q[0]
        self.__q = self.__q[1:]
        return value
        
