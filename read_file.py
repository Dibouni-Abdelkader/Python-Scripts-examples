import os
os.chdir(r'') #path here
class file_data :  #defin a class named file_data
    def __init__(self,filename):  # constactor
        self.filename=filename    
    def open_file(self):    
        try:                              # try statement to catche the excptions 
            my_file=open(self.filename,'r')   #open a file in read mode
            read_file=my_file.read()
        except IOError:                    #if the file is not found 
            print('file not found or invalid data')
        else:                  

            print('____________you file here__________________')
            print(read_file)                 # print contin of file
            print('_____________end of reading file_________________')
         
            
        finally:
            my_file.close()      #cloosing the file after reading 

    

filename=input('enter a file to read: ')  # insert a file from user
file_one=file_data(filename)  
file_one.open_file()        

