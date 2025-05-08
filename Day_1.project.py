#let's make a name logger to understand file handling better. 

#let's ask the name first 

name = input("Please enter your name: ")

#now, let's save the name in new file by creating it. 

with open ('names_txt', 'a') as file:
    file.write(name + '\n')
    
#now the name has been added. 

#let's read the names

print("All the names are: ")
with open ('names_txt', 'r') as file:
    for line in file: 
        print(line.strip())
           