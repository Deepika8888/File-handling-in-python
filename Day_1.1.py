#reading from a file 

#use 'r' mode to read a file


file = open('my_file.txt', 'r')
file_content = file.read
print(file_content)
file.close()