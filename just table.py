def table(base):   #defin func named tabel with one argemment name'base'
        result=[]     #result=empty list 
        n=1
        while n<11:             #
            b=n*base
            result=result+[b]   #resultat=[1*base,2*base,........] 
            n=n+1              # n+1=2,2+1=3........ 
        return result


tab9=table(8)             
print (tab9)
