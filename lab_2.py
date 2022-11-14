test = input("enter a string:")
frq = {}
for i in test:
        if i in frq:
            frq[i] += 1
        else:
            frq[i] = 1
print ("Count of all characters in string is :\n "
                                        +  str(frq))  
              
            