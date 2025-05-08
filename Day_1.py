#day 1 of file hadling lesson 
#let's open a file fil and write some text in it 
#using 'w' mode to write in the file. and if the file does not exist, it will be created. 

file = open('my_file.txt', 'w')
file.write("My name is Deepika Chand.\n")
file.write("I want to learn file handling in python.\n")
file.write("I think i am going to learn it this time.\n")
file.write("I hope to learn it as soon as possible.\n")
file.write("Let's learn it together.")
file.close()
