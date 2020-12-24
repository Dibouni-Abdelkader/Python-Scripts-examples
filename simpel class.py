class Person:
    
    
    "for take full_information from users and sorted it"
    def __init__(self,name,pre_name):
        self.name=name
        self.pre_name=pre_name
        
    @property
    def fullname(self):
        return '{} {}'.format(self.name,self.pre_name)

    @fullname.setter
    def fullname(self,fullname):
        name,pre_name=fullname.split(' ')
        self.name=name
        self.pre_name=pre_name

    @classmethod
    def get_age(cls,age):
        cls.age=int(age)

    @classmethod
    def get_hoby(cls,hoby):
        cls.hoby=hoby
        
    @property
    def talk(self):
        print( 'so your fullname is {}'.format(self.fullname))
        print('and you age is {} old'.format(self.age))
        print('your favorit hoby is the {}'.format(self.hoby))






    
