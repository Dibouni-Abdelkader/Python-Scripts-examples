try:
	fh = open('textfile','w')
	fh.write('hello world')
except IOError:
	print('Error: can\'t find file or read data')
else:
	fh.close()