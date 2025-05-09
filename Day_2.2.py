#let's learn to check if file exists or not before reading
# it's not very important, however, good if you learn. 

import os 

if os.path.exists('somefile.txt'):
    with open ('somefile.txt', 'r') as file:
      print(file.read())  
else: 
    with open ('somefile.txt', 'w') as file: 
        file.write("I am a idiot")
      