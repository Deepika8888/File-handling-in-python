#using 'with' statement 
#autocloses the file when done

#with open('my_file.txt', 'r') as  file:
   # content = file.read()
   # file.close() 
   
with open ('mynew_file.txt', 'w') as file:
    file.write("I am a idiot.")
    file.close()