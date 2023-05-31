from abc import ABC, abstractmethod

class Telephone(ABC):
    def __init__(self , telecom_service , name):
        self.telecom_service = telecom_service
        self.name = name
    
    @abstractmethod
    def dial(self):
        pass

class Wireless(Telephone):
    def __init__(self, telecom_service, name):
        super().__init__(telecom_service, name)
    
    def dial(self):
        print("wireless phone")

class Wired(Telephone):
    def __init__(self, telecom_service, name):
        super().__init__(telecom_service, name)
    
    def dial(self):
        print("Wired Phone")

wireless = Wireless("Jio" , "OnePlus")
wired = Wired("Vodaphone" , "Samsung")

list_of_objects =[wireless , wired]

for obj in list_of_objects:
    obj.dial() 




         