import sqlite3
import csv
import os

# Load the csv file and insert it into a new SQLite3 database
def load(dataset="/Users/liuliangcheng/Desktop/Duke/IDS_DE/IDS_DE_SQL_T/US_birth.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    # Prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('BirthDataDB.db')
    c = conn.cursor()
    
    # Drop the existing table if it exists and create a new one with the correct columns
    c.execute("DROP TABLE IF EXISTS BirthDataDB")
    c.execute("""
        CREATE TABLE BirthDataDB (
            year INTEGER, 
            month INTEGER, 
            date_of_month INTEGER, 
            day_of_week INTEGER, 
            births INTEGER
        )
    """)
    
    # Insert data into the table
    c.executemany("INSERT INTO BirthDataDB VALUES (?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    
    return "BirthDataDB.db"


