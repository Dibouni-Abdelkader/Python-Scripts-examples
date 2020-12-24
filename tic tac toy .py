from tkinter import *
from tkinter import ttk
from tkinter import messagebox


ActivePlayer = 1
P1=[]
P2=[]


#-------------------------------------------------------------------

root=Tk()
root.title('Tic Tac Toy : Player 1')
root.maxsize(300,300)
style=ttk.Style()
style.theme_use('classic')


#-------------------------------------------------------------

bou1=ttk.Button(root,text='')
bou1.grid(row=0,column=0,ipadx=30,ipady=30,sticky='snew')
bou1.config(command=lambda:buclick(1))


bou2=ttk.Button(root,text='')
bou2.grid(row=0,column=1,ipadx=30,ipady=30,sticky='snew')
bou2.config(command=lambda:buclick(2))


bou3=ttk.Button(root,text='')
bou3.grid(row=0,column=2,ipadx=30,ipady=30,sticky='snew')
bou3.config(command=lambda:buclick(3))


bou4=ttk.Button(root,text='')
bou4.grid(row=1,column=0,ipadx=30,ipady=30,sticky='snew')
bou4.config(command=lambda:buclick(4))


bou5=ttk.Button(root,text='')
bou5.grid(row=1,column=1,ipadx=30,ipady=30,sticky='snew')
bou5.config(command=lambda:buclick(5))


bou6=ttk.Button(root,text='')
bou6.grid(row=1,column=2,ipadx=30,ipady=30,sticky='snew')
bou6.config(command=lambda:buclick(6))


bou7=ttk.Button(root,text='')
bou7.grid(row=2,column=0,ipadx=30,ipady=30,sticky='snew')
bou7.config(command=lambda:buclick(7))


bou8=ttk.Button(root,text='')
bou8.grid(row=2,column=1,ipadx=30,ipady=30,sticky='snew')
bou8.config(command=lambda:buclick(8))


bou9=ttk.Button(root,text='')
bou9.grid(row=2,column=2,ipadx=30,ipady=30,sticky='snew')
bou9.config(command=lambda:buclick(9))


#--------------------------------------------------------------

def buclick(id):
	global ActivePlayer
	global P1
	global P2

	if(ActivePlayer ==1):
		setlayout(id,'X')
		P1.append(id)
		root.title('Tic Tac Toy : Player 2')
		ActivePlayer =2


	elif(ActivePlayer ==2):
		setlayout(id,'O')
		P2.append(id)
		root.title('Tic Tac Toy : Player 1')
		ActivePlayer =1

	if len(P1) or len(P2)>2:
		CheckWiner()
#--------------------------------------------------------

def setlayout(id,text):
    if(id==1):
    	bou1.config(text=text)
    	bou1.state(['disabled'])

    elif(id==2):
    	bou2.config(text=text)
    	bou2.state(['disabled'])

    elif(id==3):
    	bou3.config(text=text)
    	bou3.state(['disabled'])

    elif(id==4):
    	bou4.config(text=text)
    	bou4.state(['disabled'])

    elif(id==5):
    	bou5.config(text=text)
    	bou5.state(['disabled'])

    elif(id==6):
    	bou6.config(text=text)
    	bou6.state(['disabled'])

    elif(id==7):
    	bou7.config(text=text)
    	bou7.state(['disabled'])

    elif(id==8):
    	bou8.config(text=text)
    	bou8.state(['disabled'])
 
    elif(id==9):
    	bou9.config(text=text)
    	bou9.state(['disabled'])



#---------------------------------------------------------------------

def CheckWiner():
	winer= -1

	if((1 in P1) and(2 in P1) and(3 in P1)):
		winer =1
	if((1 in P2) and(2 in P2) and(3 in P2)):
		winer =2



	if((4 in P1) and(5 in P1) and(6 in P1)):
		winer =1
	if((4 in P2) and(5 in P2) and(6 in P2)):
		winer =2


	if((7 in P1) and(8 in P1) and(9 in P1)):
		winer =1
	if((7 in P2) and(8 in P2) and(9 in P2)):
		winer =2



	if((1 in P1) and(4 in P1) and(7 in P1)):
		winer =1
	if((1 in P2) and(4 in P2) and(7 in P2)):
		winer =2


	if((2 in P1) and(5 in P1) and(8 in P1)):
		winer =1
	if((2 in P2) and(5 in P2) and(8 in P2)):
		winer =2


	if((3 in P1) and(6 in P1) and(9 in P1)):
		winer =1
	if((3 in P2) and(6 in P2) and(9 in P2)):
		winer =2



	if((1 in P1) and(5 in P1) and(9 in P1)):
		winer =1
	if((1 in P2) and(5 in P2) and(9 in P2)):
		winer =2


	if((3 in P1) and(5 in P1) and(7 in P1)):
		winer =1
	if((3 in P2) and(5 in P2) and(7 in P2)):
		winer =2

	
	if winer ==1:
		messagebox.showinfo(title='Cong',message='Player 1 is winer')

	if winer ==2:
		messagebox.showinfo(title='Cong',message='Player 2 is winer')
	
  
	
            

		

root.mainloop()
