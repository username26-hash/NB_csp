#NB P7 reading and writing to Files

with open("practice.txt","r+") as file: #r+ lets you read and write.
    content= file.read()
    content= "Chapter 1: \n" + content + "And Christopher Robin was sitting on his doorstep putting on his big boots" 
    file.write(content)
    print(content)

with open("practice.txt", "a") as file:
    file.write("\nwinnnie the pooh and the blustery day")