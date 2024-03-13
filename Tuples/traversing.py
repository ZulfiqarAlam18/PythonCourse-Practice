
fav_fruits = ("apple", "orange", "Kiwi")

#print(fav_fruits)
#for f in fav_fruits:
    #print(f)


#for any single element of fav_fruits
#print(fav_fruits[1])

#Modify fav_fruits: as tuples are immutable therefore first we have to type cast are tuple into a list
my_list = list(fav_fruits)
my_list[1] = "Vanilla"
myNewTup = tuple(my_list)
#print(myNewTup)

#Concatenating two tuples 
t1 = ("Zulfiar",23)
t2 = (23,45)
res = t1 + t2
#print(res)

#tuple length
#print(len(fav_fruits))

#Unpacking the tuple
a,b,c = (3,5,10)
#print(a,b,c)
#print(a+b+c)

#Counting occurrences of any element in the tuple
data = ('a', 'b', 'c', 'd', 'e','a', 'f', 'g', 'h', 'i','a','b')
#print(data.count('a'))        

#type casting any tuple into a string/int/float etc
t = ("Zulfiqar alam")
s = "".join(t)
#print(s)

t2 = ("Zulfiqar","Alam","Jamali")
str = "_".join(t2)
#print(str)

