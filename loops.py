# NB p7 loops
import random

count= 1
#1 is starting point 

while count<= 10: #stop point boodean statement
    print(count)
    count += 1

ducks = 1
goose=random.randint(1,11)

while True:
    if ducks == goose:
        break
    print("duck....")
    ducks+= 1 #ducks=ducks+ 1
print("GOOSE!")

#complex data type= holds other data in it 
sibling= ["Val", "paula", "natty"]
#surronded by brackets
#every item in list must be sepperated by commas
# must be valid data type
print(sibling[0])
#to print an item of the list you say the name of the varible and the number of what you want from the list starting at 0
#Adding to a list
sibling.append("nickolle")
print("sibling")

#remove from the list
sibling.pop(3)


print(sibling)


   


          



