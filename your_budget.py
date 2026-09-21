# NB, your budget 

while True:
    try:
        income = float(input("what is your monthly income?"))
        break
    except:
           print("you forgot to put your monthly income")


while True:
    try:
        rent = float(input("what is your monthly rent/mortgage?"))
        break
    except:
           print("you forgot to put your rent/mortgage")

while True:
    try:
        utilities = float(input("what is your monthly utilities?"))
        break
    except:
           print("you forgot to put your monthy utilities")           


while True:
    try:
        grocieries= float(input("what is your monthly groceries?"))
        break
    except:
           print("you forgot to put your monthly grocieries")  


while True:
    try:
        transportation = float(input("what is your monthly transportation?"))
        break
    except:
           print("you forgot to put your monthly transportation") 

save= round(income/10,2)

print(f"your rent is ${rent:.2f} and that is {round(rent/income*100)} % of your income")

print(f"your utilities is ${utilities:.2f} and that is {round(utilities/income*100)} % of your income ")

print(f"your groceries are ${grocieries:.2f} and that is {round(grocieries/income*100)} % of your inocome")

print(f"your transportation is ${transportation:.2f} and that is {round(transportation/income*100)} % of your income")

print(f"you should save ${save:.2f} a month that is 10% of your income")

print(f"you have ${income-rent-utilities-grocieries-transportation-save:.2f} of spending money each month!")