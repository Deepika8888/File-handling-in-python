#lets learn to write using in csv files. 

import csv 

#taking name and contact info 
name = input ("Enter your name: ") 
contact = input("Enter your contact number: ") 

#now writing the contacts into the csv file 

with open("contacts.csv", "a", newline='') as file: 
    writer = csv.writer(file) 
    writer.writerow([name, contact])
    
print("Contact saved!")