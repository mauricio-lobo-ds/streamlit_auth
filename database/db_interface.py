from abc import ABC, abstractmethod

''' 
abstractmethod é um decorador que marca um método como abstrato. 
Um método abstrato é um método que é declarado, mas não contém implementação.
Qualquer classe que herde de uma classe abstrata contendo métodos abstratos deve fornecer 
uma implementação para esses métodos, caso contrário, ela também será considerada abstrata 
e não poderá ser instanciada.
'''

class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query, params=None):
        pass

    @abstractmethod
    def fetchall(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def close(self):
        pass