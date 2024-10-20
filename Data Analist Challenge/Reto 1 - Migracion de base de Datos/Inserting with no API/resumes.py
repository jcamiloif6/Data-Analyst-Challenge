# 1. Import libraries
import csv
import datetime
import mysql.connector

# 2. Define database parameters
mydb = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password = "Clave-123",
)

cursor = mydb.cursor()

#3. Creating database in Mysql 
sql_database = "create DATABASE IF NOT EXISTS challenge"
cursor.execute(sql_database)

cursor.execute("USE challenge")

# 4. Insert data into table
filename = "resumes - resumes.csv"

# 4.1 Reading csv resumes file and creating the table
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    first_row = next(csvreader) # First row of csv file to categorize columns names

    # 4.2 Validating format columns
    columns = []
    for i, col in enumerate(header):
        value = first_row[i]

        if value.isdigit():
            num_value = int(value)
            # Check if the value fits in BIGINT
            if num_value < -2147483648 or num_value > 2147483647:
                columns.append(f"`{col}` BIGINT")  # Use BIGINT for larger numbers
            else:
                columns.append(f"`{col}` INT")  # If column is digit, use INT
                
        else:
            try:  
                datetime.datetime.strptime(value, '%Y-%m-%d') # If column is a date
                columns.append(f"`{col}` DATE")
            except ValueError:
                columns.append(f"`{col}` VARCHAR(1000)") # Else, column is a text
    
     # 4.3 creating profiles table
    sql_table = "CREATE TABLE IF NOT EXISTS resumes (" + ', '.join(columns) + ")"
    cursor.execute(sql_table)

    placeholders = ', '.join(['%s'] * len(first_row))

    # 4.4 Insert data into tabl
    sql_insert = f"INSERT INTO  resumes VALUES ({placeholders})"
    cursor.execute(sql_insert, first_row)

    for row in csvreader:
        cursor.execute(sql_insert, row)

mydb.commit()

print(mydb)