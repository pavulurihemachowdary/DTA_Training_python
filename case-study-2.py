import csv
with open('employee_data.csv') as file:
    csv_reader=csv.DictReader(file)
    #to read csv files with a header we use dictreader
    with open('updated_employee_data.csv','w',newline="") as csvfile:
        headernames=['FullName','Age','UpdatedSalary']
        csv_writer=csv.DictWriter(csvfile,headernames)
        csv_writer.writeheader()
        for i in csv_reader:
            csv_writer.writerow({'FullName': i['FirstName']+i['LastName'],
                                 'Age':2024-int(i['YearOfBirth']),
                                 'UpdatedSalary':int(i['Salary'])+int(i['Bonus'])})

