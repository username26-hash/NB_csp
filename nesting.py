#NB P7

count=2

while count<= 20:
    print(count)
    count+=1


    for number in range (1,21):
        if number % 15== 0:
            print("FizzBuzz")
        elif number% 3 == 0:
            print("Fizz")
        elif number % 5== 0:
            print("Buzz")
        else:
            print(number)
    
    siblings = ["Alex","Katie", "Andre", "Vienna", "Tia", "Treyson", "Xavier", "Jake"]

    count= 1 
    
    while count < len(siblings):
        print(f"{count}. {siblings[count-1]}")
        count+= 1 

