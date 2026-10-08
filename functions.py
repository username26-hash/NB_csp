#NB functions notes
def stupid_proof(money):
    while True:
        try:
        amount= float(input(f"what is your monthly{money}: "))
        return amount
except:
print("that isint a number :")
 
# Writre all your varibles 
income= stupid_proof("income")
rent= stupid_proof("rent")
utilities= stupid_proof("utilities")
grocieries= stupid_proof("grocieries")
transportation=stupid_proof("transportation")
saveing=income *.1

# Write any function you are using 
def calc_percent (income,bill):
    return round(bill/income *100)


# Outputs for user 
print(f"your rent is ${rent:.2f} that is {calc_percent (income,rent)} % of your income")
print(f"your utilities is ${utilities:.2f} that is {calc_percent (income,utilities)} % of your income")
print(f"your grocieries is ${grocieries:.2f} that is {calc_percent (income,grocieries)} % of your income")
print(f"your transportation is ${transportation:.2f} that is {calc_percent (income,transportation)} % of your income")
print(f"you should save $" )