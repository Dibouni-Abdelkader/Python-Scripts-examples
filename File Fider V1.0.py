from tkinter import *
from tkinter import ttk, messagebox
import os

class App(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.master.title('FileFinder V1.0')
		self.master.minsize(250,400)
		self.master.maxsize(250,400)
		self.var = StringVar()
		self.radio_var = StringVar()
		self.pack()

	def find(self):
		try:
			path = self.var.get()
			type_search = '.'+ self.radio_var.get()
			os.chdir(path)
			count = 1
			for root,dirs,files in os.walk('.'):
				for file in files :
					if file.endswith(type_search):
						self.listbox.insert(0,str(count)+'- '+file)
						count += 1
			self.label.config(text= str(count)+'files')
		except Exception as e:
			messagebox.showerror('Eroor','something goes wrong please try again.')
			os._exit(0)

		finally:
			self.entry.delete(0,END)

	def clear(self):
		self.listbox.delete(0,END)
		self.label.config(text='fileFinder')

	def widgets(self):
		self.label = Label(self,text='fileFinder')
		self.label.pack(expand = YES,fill=BOTH,pady=5)
		self.entry = ttk.Entry(self,width=44,textvariable=self.var)
		self.entry.pack(expand = YES,fill=BOTH,ipady=5,pady=5)
		self.entry.focus()
		frame_button = Frame(self).pack(expand=YES,fill=BOTH)
		self.radio_butt1 = Radiobutton(frame_button,text='video',variable= self.radio_var,value="mp4").pack()
		self.radio_butt2 = Radiobutton(frame_button,text='document',variable= self.radio_var,value="pdf").pack()
		self.radio_butt3 = Radiobutton(frame_button,text='song',variable= self.radio_var,value="mp3").pack()
		self.listbox =Listbox(frame_button)
		self.listbox.pack(expand = YES,fill=BOTH)
		self.button_find =ttk.Button(frame_button,text='Find',command=self.find)
		self.button_find.pack(expand = YES,fill=BOTH)
		self.button_clear = ttk.Button(frame_button,text= 'Clear',command=self.clear)
		self.button_clear.pack(expand = YES,fill=BOTH)


	


if __name__ == '__main__':
	root = Tk()
	app = App(root)
	app.widgets()
	root.mainloop()