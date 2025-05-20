#using DICTREADER

import csv 

name = input("Enter name: ")
phone = input("Enter phone number: ")

#let's open a new csv file. 

with open('contacts_dict.csv', 'a', newline= '') as file: 
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    if file.tell() == 0:
        writer.writeheader()
        
    writer.writerow({"Name": name, "Phone": phone})