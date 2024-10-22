s = "([{}])"
li=[]
for i in s:
    if i=="(" or i=="[" or i=="{":
        li.append(i)
    elif i == "}":
        if len(li)<0 or li.pop()!="{":
            print(False)
        
        

        