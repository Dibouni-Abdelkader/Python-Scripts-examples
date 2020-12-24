print ('*************************this is a simpel calcu********************************')
print ("""how it's work:\n 1'enter a number' \n 2 'enter other number '\n
for operation: write\t
(+)for sum
(-)for minus
(//)for floor sub
(*)for multi
(/)for normal sub
""")
def clcu(x,y,new):
        while True:
                if new =='+':
                        print (result, x+y)
                        break
                elif new== "*":
                        print (result,x*y)
                        break
                elif new=="-":
                        print (result,x-y)
                        break
                elif new=="//":
                        print (result,x//y)
                        break
                elif new=="/":
                        print (result,x/y)
                        break
                else:
                        print ("invalid number or unknown opiration")
                        break
        clcu(x,y,new)
x=int(input('enter number1: '))
new=input("enter operation: ")
y=int(input('enter number2:  '))            
result='the result is:'


clcu(x,y,new)

print('__________________________________________________________________________')
