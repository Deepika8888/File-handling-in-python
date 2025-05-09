#let's learn to write multiple lines using .writelines()
lines_to_write = ['My name is Deepika Chand\n', 'Nice to meet you again :) \n', 'lets learn together\n']
with open ('new_file.txt', 'w') as file: 
    file.writelines(lines_to_write)