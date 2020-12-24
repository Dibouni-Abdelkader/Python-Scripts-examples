class ana:   
    def __init__(self,fellname,char):#defin a constractor 
        self.fellname=fellname  #somme attributes
        self.char=char
    def __str__(self):  
        count=0
        try:
            with open (self.fellname)as f: #opening a file from your pc as named 'f'
                text=f.read() #reading the file and asgnied to variable 'text'
            
            for i in text:          
                if i ==self.char:   
                    count+=1
            return count
        except :
            print('Error file not found')
            fellname=input("enter a fellname: ")  #get filename from user
            char=input('enter char for count: ')  #get char from user to check count  

fellname=input("enter a fellname: ")  #get filename from user
char=input('enter char for count: ')  #get char from user to check count    
    
kadi=ana(fellname,char)  #make a instance named kadi from class 'ana'
print(kadi.__str__())  #printed the methed thats counting the char


                
