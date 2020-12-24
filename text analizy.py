def count_char(text,char):
	count=0
	for c in text:
		if c==char:
			count+=1
	return count

file_name=input("enter the file name: ")
try:
        with open(file_name)as f:
                text=f.read()

        for char in "abcdefghijklmnopqrstuvwxyz":
                perc=100*count_char(text,char)/len(text)
                print("{0}-{1}%".format(char,round(perc,2)))
except FileNotFoundError as e:
        print('Error:',str(e))
        




	
