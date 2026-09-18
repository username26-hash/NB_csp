#NB strings notes 

#string=> any saved inside of quotation marks "" ''


name= input("what is your name: ").strip().lower()

age= input('how old are you:')
print(type(age))


#Concatenation=> puts two strings directly next to each other 
print(age+age)



#string.action()
sentence="The quick brown fox jumped over the lazy dog"

print(sentence)

print(sentence.replace("dog","monkey"))
print(len(name)) #<= gets the length of a string 
print(f"your name is {name} that is {len(name)} letters long. Your first initial is {name[0]}")

Print(f"your name is {name} that is {len(name)} letters long. Your first initial is {name[0]} I think it I will call you {name[0:3]}")

