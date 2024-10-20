# Importing necesary libraries
from flask import Flask, request, jsonify
import csv
import datetime
import mysql.connector
import os

app = Flask(__name__)

# 1. Define the database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="clave",
        database="challenge"
    )

# 2. Create the database
def initialize_database(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS challenge")
    cursor.execute("USE challenge")

# 3. Create the table name based on the CSV file name
def get_table_name(file_name):
    base_name = os.path.basename(file_name).replace(' ', '_') 
    table_name = os.path.splitext(base_name)[0]  # Remove file extension
    return f"`{table_name}`"

# 4. Read CSV file and insert data into MySQL Workbench
def process_csv_and_insert(file_path, cursor):
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader) # First row to see columns names
        first_row = next(csvreader)

        # 4.1 Create the table with the columns based on the CSV
        columns = []
        for i, col in enumerate(header):
            value = first_row[i]

            # Evaluating data types
            if value.isdigit():  # If column is numeric
                num_value = int(value)
                if num_value < -2147483648 or num_value > 2147483647:
                    columns.append(f"`{col}` BIGINT")
                else:
                    columns.append(f"`{col}` INT")
            else:
                try:
                    datetime.datetime.strptime(value, '%Y-%m-%d') # Date data type
                    columns.append(f"`{col}` DATE")
                except ValueError:
                    columns.append(f"`{col}` VARCHAR(1000)") # Otherwise, string type

        # 4.2 Create a table with the name based on the file
        table_name = get_table_name(file_path)
        sql_table = f"CREATE TABLE IF NOT EXISTS {table_name} (" + ', '.join(columns) + ")"
        cursor.execute(sql_table)

        # 4.3 Insert the data into the table
        placeholders = ', '.join(['%s'] * len(first_row))
        sql_insert = f"INSERT INTO {table_name} VALUES ({placeholders})"

        cursor.execute(sql_insert, first_row)
        for row in csvreader:
            cursor.execute(sql_insert, row)

# 5. API endpoint to upload CSV and insert data into the database
@app.route('/upload_csv', methods=['POST'])
#5.1 Reading the file name
def upload_csv():
    if 'file' not in request.files:
        print(request.files)
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Saving the file
    file_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(file_path)

    # 5.2 Process the file and insert data into the database
    mydb = get_db_connection()
    cursor = mydb.cursor()
    try:
        initialize_database(cursor)
        process_csv_and_insert(file_path, cursor)
        mydb.commit()
    except Exception as e:
        mydb.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        mydb.close()

    os.remove(file_path)

    return jsonify({"message": f"CSV data from {file.filename} inserted successfully"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)

