#let's practice a Mini Project: Contact Book (CSV + Error Handling)

#let's ask the name and contact info first.

name = input("Enter your name: ")
phone = input("Enter your phone number: ")

import csv
#let's open a new csv file. 

with open('MYcontacts.csv', 'a', newline='') as file: 
    writer = csv.writer(file)
    writer.writerow([name,phone])
    
#let's see all our saved contacts.

print("\nAll the contacts:")

try: 
    with open('MYcontacts.csv', 'r') as file: 
        reader = csv.reader(file)
        for i, row in enumerate(reader, start=1):
            print(f"{i}.{row[0]} - {row[1]}")
except FileNotFoundError:
    print("File not found. File doesn't exist yet.")