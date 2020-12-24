
class Person :
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job
        
    def talk(self):
        return 'hi there my name is {} i have {} year \nand i worke in {}'.format(self.name,self.age,self.job)
    
kadi=Person('sami',26,'front end devloper ')

print(kadi.talk())
