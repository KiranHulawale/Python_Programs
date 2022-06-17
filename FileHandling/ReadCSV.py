import csv

filename = "demo.csv"
 
# initializing the titles and rows list
fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')
