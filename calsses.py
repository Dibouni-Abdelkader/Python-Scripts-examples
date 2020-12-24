class Emp:
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first+' ' + last + '@email.com'
        
    def fullname(self):
        #return '{} {}'.format(self.first,self.last)
        return f'{self.first} {self.last}'
    
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
    
class dev(Emp):
    raise_amt=1.10
    def __init__(self,first,last,pay,prog_lg):
        super().__init__(first,last,pay)
        self.prog_lg=prog_lg
        
class mang(Emp):
    def __init__(self,first,last,pay,employes=None):
        super().__init__(first,last,pay)
        if employes is None:
            self.employes=[]
        else:
            self.employes=employes
    def add_emp(self,emp):
        if emp not in self.employes:
            self.employes.append(emp)
     
    def remove_emp(self,emp):
         if emp in self.employes:
            self.employes.remove(emp)

        
            
    def print_emp(self):
        for emp in self.employes:
            print('--->',emp.fullname())
            
class bose(Emp):
    def __init__(self,first,last,pay,workers=[]):
        super().__init__(first,last,pay)
        self.workers=workers
        
    
    def add_workers(self,work):
        if work  not in self.workers:
            self.workers.append(work)

        else:
            print('the worker is alredy in workers')
            
    def remove_workers(self,work):
        if work in self.workers:
            self.workers.remove(work)
        else:
            print('Oops the worker is not here')
    
    def print_workers(self):
        for work in self.workers:
            print('--->',work.fullname())
        else:
            print('there is not workers with this name ')





