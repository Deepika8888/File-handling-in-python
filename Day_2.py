#day 2 of file handling lessons
# let's learn to read files line by line using .readlines()

with open ('my_file.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())