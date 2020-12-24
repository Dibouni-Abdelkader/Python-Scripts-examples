

def changeFilesEx():

	import os
	path = r"" #path here
	os.chdir(path)
	for i in os.listdir('.'):
		os.rename(i, str(i[0:10]) + ".pdf")
	print(os.listdir())

changeFilesEX()
