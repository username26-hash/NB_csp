#NB password strength p7

charecters= False 
uppercase= False
lowercase= False
number= False
symbol= False
length= False
requirements= 0

password= input("what is your password")

password_length = len (password)
   
if password_length >= 8:
    length= True
if password_length <= 8:
    length= False

for letters in password:
    if letters.isupper():
        uppercase= True
    if letters.islower():
            lowercase= True
    if letters.isnumeric():
         number= True
    if letters in "!@#$%^&*[]<>:":
          symbol= True


if length== True:
     class requirements_met:
          ...

     requirements_met += 1
if uppercase== True:
     requirements_met += 1
if lowercase== True:
     requirements_met+= 1 
if number== True:
     requirements_met += 1
if symbol== True:
     requirements_met += 1

if requirements_met == 5:
     password_strength= "Strong"
elif requirements_met >= 4 and requirements_met >= 3:
     password_strength= "Moderate"
else:
     password_strength= "Weak"

print(f"has at least 8 characters: {length}")
print(f"has an uppercase letters: {uppercase}")
print(f"has a lowercase letters: {lowercase}")
print(f"has a numbers: {number}")
print(f"has a symbol: {symbol}")

print(f"your password strength is : {password_strength}")

if password_strength == "Strong":
    print("Good job your password is strong.")
else:
     print("to make it strong:")
     if length == False:
          print("- Make sure your password has at least 8 characters.")
          if uppercase == False:
               print("- Include an uppercase letter.")
          if lowercase == False:
               print("- add a lowercase letter.")
          if number == False:
               print("- add a number.")
          if symbol == False:
               print("- add a symbol.")