#Task1 in diary.py

#Task2 Read a CSV File: 
import csv 
import traceback
def read_employees():
    employee = {}
    rows = []
    try: 
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader): 
                if index == 0:
                    employee["fields"] = row
                else:
                    rows.append(row)
            employee["rows"] = rows 
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(f"File:{trace[0]}, Line:{trace [1]}, Func.Name: {trace[2]}, Message: {trace[3]}"  
            )
        print(f"Exception type: {type(e).__name__}")

        message = str(e)

        if message: 
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

    return employee
employees = read_employees()
print(employees)

#Task3 Find the Column Index:
def column_index(column_name):
    return employees["fields"].index(column_name) 

employee_id_column = column_index("employee_id")

#Task4 Find the Employee First Name: 
def first_name(row_number):
    col_idx = column_index("first_name")
    return employees["rows"][row_number][col_idx]

#Task5 Find the Employee:
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task6 Finde the Employee Lambda: 
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

#Task7 Sort the Rows:
def sort_by_last_name(): 
    last_name_column = column_index("last_name")
    employees["rows"].sort(
        key = lambda row: row[last_name_column]
    )
    return employees["rows"]
sort_by_last_name()
print(employees)

#Task8 Create a Dict:
def employee_dict(row):
    employee = {}
    headers = employees["fields"]
    for i in range(len(headers)):
        header = headers[i]
        value = row[i]
        if header != "employee_id":
            employee[header] = value
    return employee
test_row = employees["rows"][0]
print(employee_dict(test_row))

#Task9 A dict of dicts:
def all_employees_dict():
    all_employees = {}
    for row in employees["rows"]: 
        dict2 = employee_dict(row)
        id2 = row[employee_id_column]
        all_employees[id2] = dict2
    return all_employees

#Task10 Use the os Module: 
import os 

def get_this_value():
    return os.getenv("THISVALUE")


#Task11 Custom Module:
import custom_module

def set_that_secret(secret):
    custom_module.set_secret(secret)
set_that_secret("hello")
print(custom_module.secret)

#Task12 Read Minutes:
import csv 
def read_csv_file(filename):
    data = {}
    rows = []
    try: 
        with open(filename, "r") as file:
            reader = csv.reader(file)
        
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row
                else: 
                    rows.append(tuple(row))
        data["rows"] = rows
        return data 
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")

        message = str(e)

        if message:
            print(f"Exception message: {message}")

        print(f"Stack trace: {stack_trace}")

        exit()

def read_minutes():
    minutes1 = read_csv_file("../csv/minutes1.csv")
    minutes2 = read_csv_file("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

#Task13 Create Minutes:
def create_minutes_set():
    minutes_set = set(minutes1["rows"]) | set(minutes2["rows"])
    return minutes_set

minutes_set = create_minutes_set()
print(minutes_set)



#Task14 Convert to datetime
from datetime import datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(
        map(
            lambda x: (
                x[0],
                datetime.strptime(x[1], "%B %d, %Y")
            ),
            minutes_list
        )
    )
    return minutes_list
minutes_list = create_minutes_list()
print(minutes_list)

#Task15 Write Out Sorted List
def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key = lambda x: x[1])
    converted_list = list(
        map(
            lambda x: (
                x[0],
                datetime.strftime(x[1], "%B %d, %Y")
            ), sorted_minutes
        )
    )
    with open("minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list
write_sorted_list()