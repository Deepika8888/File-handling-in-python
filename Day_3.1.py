#lets read and show all the contacts

import csv 
import os

print('\all the contacts:')

try: 
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader, start=1):
            name, phone = row
            print(f"{i}.Name:{name}. Phone:{phone}")
except FileNotFoundError:
    print("file is not founed. file doesn't exist yet.")                 