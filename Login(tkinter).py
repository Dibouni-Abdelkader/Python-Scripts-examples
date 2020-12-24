from tkinter import *   #import all method from tkinter module
from tkinter import ttk  # import ttk's module from tkinter 
from tkinter import messagebox  # import the messgebox modul
import os, sqlite3 # import both os and sqlite3 

'''sqlite3 is module in python used for make database files'''

class Application(Frame):

	"""This Gui made by tkinter it's sempel LogIn Application 
		store data in filename """

	db = None  # class attribute all instance can see hem , None : give value later in the code 

	def __init__(self,master=None): # just frame 
		Frame.__init__(self,master)
		self.master = master
		self.pack(expand=YES,fill=BOTH) # show the frame in the root gui
		self.master.title('LOGIN')

		self.label = Label(self,text='Name') #label user type his name
		self.label.grid(row=0,column=0,sticky='snew') #the place were put label name

		self.label_2 = Label(self,text='Password') #label passsword 
		self.label_2.grid(row=1,column=0,sticky='snew')# place were put the label password

		self.entry = ttk.Entry(self) #make entry name
		self.entry.grid(row=0,column=1,sticky='snew',padx=0,pady=2) #put in row 0, column 1

		self.entry_2 = ttk.Entry(self,show='*') # same thing
		self.entry_2.grid(row=1,column=1, sticky='snew' ,padx=0,pady=2) #also the same 
		
		self.button = ttk.Button(self,text='login',command=self.login) # the buttton that submit the data to filename
		self.button.grid(row=2,column=1,sticky='e') # were put the button in the frame

		self.button_1 = ttk.Button(self,text='Show',command=self.show)
		self.button_1.grid(row=3,column=1,sticky='e')

	def login(self):

		try:
			os.chdir(r'C:\Users\2018\Desktop') # change the dir to Desktop

			self.db = sqlite3.connect('test.db') # create database file named test.db 
			self.db.row_factory = sqlite3.Row 
			self.db.execute('drop table if exists text')  #delete table if he exists 
			self.db.execute('create table text(t1 text,i1 int)') #create table with tow column t1,i1

			name= self.entry.get() # get the value from entry
			passwod = self.entry_2.get() # get the value from entry

		except Exception as e:
			messagebox.showerror('Error', e) #if somethig goes wrong show error
		else:  # if no exception happend go and do this part

			if (not name) or (not passwod):# check if the one of the field is empty show warning to user
				messagebox.showinfo('Warning','The Feild Must Not Be Empty!') # popup show warning
			else:
				self.entry.delete(0,END) # clear the fields after get values
				self.entry_2.delete(0,END)
				self.db.execute('insert into text(t1,i1) values(?, ?)',(name,passwod))  #insert name password into the table
				self.db.commit()  #commit
				self.db.close() # close the file after save data 	
				messagebox.showinfo('Cong..','{} registred sucsec'.format(name)) # if all ok show the registred sucsec

	def show(self): # method show all the user who they regestred in the database file

		root_1 = Tk() # make new window call it root_1
		listbox = Listbox(root_1)  # make listbox to sort the user
		
		os.chdir(r'C:\Users\2018\Desktop') #chang the directry to Desktop 
		self.db = sqlite3.connect('test.db') # create database file named test.db 
		dbread = self.db.execute('select * from text order by i1') # read the data from the file
		index = 0
		for i in dbread:     
			listbox.insert(index,i)
			index = index + 1
		listbox.pack()
		root_1.mainloop()

if __name__ == '__main__': #for test the gui
	root = Tk()   # make the main root 
	app = Application(root) # get object from our class Application 
	root.mainloop() # run the Gui
