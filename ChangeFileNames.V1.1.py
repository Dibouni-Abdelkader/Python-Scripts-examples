import os
path = r"C:\Users\2018\Desktop/Videos" #add Path here
os.chdir(path)

def changeFilesName():
	try:
		for i in os.listdir('.'):
			os.rename(i, str(i[0:10]) + ".pdf")
	except FileNotFoundError:
		print('File Not Found Please Try Again.')
	else:
		print('Mission Complete...')



def changeSubMultiFilesName(path, filexExE):
	try:
		for root, dirs, files in os.walk('.'):
			for file in files:
				os.rename(files, str(file[0:10] + '.pdf'))
	except FileNotFoundError :
		print('File Not Found Please Try Again.')
	else:
		print('Mission Complete...')




def CountFileInDir():
	data= []
	for root, dirs, files in os.walk('.'):
		for file in files :
			data.append(file)

	print('there is: ' + str(len(data)) + ' files in this Dir')


if __name__ == '__main__':
	CountFileInDir()

