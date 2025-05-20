#using DictReader
import csv
with open ('contacts_dict.csv', 'r') as file: 
    reader = csv.DictReader(file)
    
    print('\nAll the Contacts:')
    for i, row in enumerate(reader, start=1):
        print(f"{i}. {row['Name']}- {row['Phone']}")