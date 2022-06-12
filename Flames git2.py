#The FLAMES game by Gnanesh : ) done on 12/06/2022 at 09:33
from collections import *
from itertools import *
from re import *
while True:
    xyz=input("do you want to play (y or n):").strip().lower()          #asking user to play or not
    if xyz == "y":
        l = ["friends", "lovers", "attraction", "marriage", "enemies", "siblings"]
        # the n1 and n2 ask user for input and remove all scratch like spaces
        n1 = input("enter 1st name:").strip().lower().replace(" ", "") #gnanesh
        n2 = input("enter 2nd name:").strip().lower().replace(" ", "") #geetha
        # the down lines remain scratch like all special characters
        n1 = sorted("".join(list(compile(r"[a-z]").findall(n1))))
        n2 = sorted("".join(list(compile(r"[a-z]").findall(n2))))
        if n1 == n2:                   # if size and names are equal print last one i.e.,  siblings
            print(l[-1])               # if the 2 strings are the same we can stop the process in the before itself
            continue
        #to count the no. of same letters 
        cc=list(Counter(n1).items())
        cc2=list(Counter(n2).items())
        #since the counter sequence return as tuple let us convert as list
        cc=list(list(cc[i]) for i in range(len(cc)))
        cc2=list(list(cc2[i]) for i in range(len(cc2)))
        #canceling all matching letters both in name1 and name2
        for i in cc:
            for j in cc2:
                if i[0] == j[0]:
                    if i[1] == j[1]:i[1] = j[1] = 0
                    elif i[1] < j[1]:j[1] -= i[1];i[1] = 0
                    else:i[1] -= j[1];j[1] = 0
                    break                       #if we wont break the process will repeat and remove all similar letters at a time
        #joining all the remaing elements 
        st="".join(list((i[0])*i[1] for i in cc+cc2 if i[1]>0))
        c=len(st)
        #len of st must be greater than 0
        if c>0:
            while len(l) > 1:          #the loop will run until the len of l is upto 1
                l2=cycle(l)            #this will iterate the same list again and again 
                count=1
                for i in l2:
                    temp = l.index(i)   #finding that index of that i element
                    if count==c:
                        l.remove(i)     #removing the i elements of l where we got
                        break
                    count+=1
                d=deque(l)
                d.rotate(len(l[temp:])) #here we rotate the right splited list to front
                l=list(d)               #the rotated list will become new list
        #since count=0 then with 0 gap we got remain as siblings : )
        else:print(l[-1])
        print("relation:",*l)
    elif xyz=="n":break
    else:print("you need to enter (y or n) only")
#this is my 2nd project in python by using modules 
#the above all code done by my own,I write this more than 5 hrs
