#Task3 List Practice 
import csv 

with open("../csv/employees.csv", newline ="") as file:
    reader = csv.reader(file)
    employees = []

    for row in reader: 
        employees.append(row)

names = [
    row[0] + " " + row[1]
    for row in employees[1:]
]
print(names)

e_names = [name for name in names if "e" in name.lower()]
print(e_names)
