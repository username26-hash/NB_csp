# NB fixing user inputs 

While True:
color=input("tell me a color:").strip().lower()
print("That is a number not a color!")

elif " " in color: 
print("i said one word.")

else:
break 

print(f"we painted the walls{color}!")