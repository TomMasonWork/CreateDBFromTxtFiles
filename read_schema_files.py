import sqlite3
import os

# Function to create a SQLite database from a text file
def create_db_from_txt(txt_file, db_file):
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    sql_create_table = '''
        CREATE TABLE IF NOT EXISTS Schema (
            id INTEGER PRIMARY KEY,
            Ordinal INT,
            GUID TEXT,
            KeyItem TEXT,
            SNLxlKeyField INT,
            ProductCaption TEXT,
            DataType TEXT,
            Magnitude TEXT,
            Length INT)
        '''

    sql_insert_data = '''
        INSERT INTO Schema (
            Ordinal,
            GUID,
            KeyItem,
            SNLxlKeyField,
            ProductCaption,
            DataType,
            Magnitude,
            Length) VALUES (?,?,?,?,?,?,?,?)
        '''

    # create table
    cursor.execute(sql_create_table)

    # read data from text file
    with open(txt_file, 'r') as file:
        for line in file:
            values = line.strip().split('|')
            values_tuple = ()
            for i in range(len(values)):
                values_tuple = values_tuple + (values[i],)
            cursor.execute(sql_insert_data, values_tuple)

    # commit changes
    conn.commit()
    # close connection
    conn.close()

# replace with the file path where your schema txt files are located
folder_name = 'PATH/TO/YOUR/FILES/'

# loop through all files in directory
for file_name in os.listdir(folder_name):
    file_path = folder_name + file_name
    # check if file, not directory
    if os.path.isfile(file_path):
        # creates a local file called database.db that you can query with SQL
        create_db_from_txt(file_path,'database.db')