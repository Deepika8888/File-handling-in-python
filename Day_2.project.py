#day 2 of making small project to learn file handling better 
#let's make a quote collector

#let's ask for a input 

quote = input("Enter a quote: ")

#let's save that quote in our file. let's create a file too. 

with open ('quotes.txt', 'a') as file: 
    file.write(quote + "\n") 
    
#let's read the quote

print("\nAll the quotes are: ")
with open ('quotes.txt', 'r') as file: 
    lines = file.readlines()
    for i, line in enumerate (lines, start =1): #gives each quote a number starting from 1
        print(f"{i}.{line.strip()}")
        

#if the file already exist and you don't need to create a new file, you can use import os. 
""" let me show you  

you can check it by using: if os.path.exists('filename.txt'):
and continue with your code. and if your file doesn't exist, you will have to create a newfile. """