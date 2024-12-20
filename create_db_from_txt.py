import sqlite3

# Function to create a SQLite database from a text file
def create_db_from_txt(txt_file, db_file):
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    values_list = []

    if 'GE0001' in txt_file:

        sql_create_table = '''
        CREATE TABLE IF NOT EXISTS StatePages (
            id INTEGER PRIMARY KEY,
            SNLStatKey TEXT,
            NAICCompanyCode TEXT,
            PeriodEnded TEXT,
            DateEnded DATE,
            LineOfBusiness TEXT,
            Geography TEXT,
            DirectPremiumsWritten REAL,
            DirectSimpleCombinedRatio REAL)
        '''

        sql_insert_data = '''
            INSERT INTO StatePages (
                SNLStatKey,
                NAICCompanyCode,
                PeriodEnded,
                DateEnded,
                LineOfBusiness,
                Geography,
                DirectPremiumsWritten,
                DirectSimpleCombinedRatio) VALUES (?,?,?,?,?,?,?,?)
        '''

        values_list = [1,2,3,4,7,8,9,26]

    if 'SI0001' in txt_file:

        sql_create_table = '''
            CREATE TABLE IF NOT EXISTS StatIndex (
                id INTEGER PRIMARY KEY,
                SNLStatKey TEXT,
                NAICCompanyCode TEXT,
                EntityName TEXT,
                PNCCombined TEXT,
                SNLInstnKey TEXT)
        '''

        sql_insert_data = '''
            INSERT INTO StatIndex (
                SNLStatKey,
                NAICCompanyCode,
                EntityName,
                PNCCombined,
                SNLInstnKey) VALUES (?,?,?,?,?)
        '''

        values_list = [1,2,4,10,24]

    if 'SI0002' in txt_file:

        sql_create_table = '''
            CREATE TABLE IF NOT EXISTS GroupData (
                id INTEGER PRIMARY KEY,
                SNLStatKey TEXT,
                NAICCompanyCode TEXT,
                SNLGroupName TEXT,
                UltParentName TEXT,
                UltParentInstnKey INT,
                CrossSectorName TEXT,
                CrossSectorStatKey TEXT)
        '''

        sql_insert_data = '''
            INSERT INTO GroupData (
                SNLStatKey,
                NAICCompanyCode,
                SNLGroupName,
                UltParentName,
                UltParentInstnKey,
                CrossSectorName,
                CrossSectorStatKey) VALUES (?,?,?,?,?,?,?)
        '''

        values_list = [1,2,4,10,12,13,14]
    

    # create table
    cursor.execute(sql_create_table)

    # read data from text file
    with open(txt_file, 'r') as file:
        for line in file:
            values = line.strip().split('|')
            values_tuple = ()
            for i in range(len(values)):
                if i in values_list:
                    values_tuple = values_tuple + (values[i],)
            cursor.execute(sql_insert_data, values_tuple)

    # commit changes
    conn.commit()
    # close connection
    conn.close()

# replace with the file path where your txt files are located
folder_name = 'PATH/TO/YOUR/FILES'

file_names = ['StatIndex_SI0001_PC_20241219_1.txt','StatIndex_SI0002_PC_20241219_1.txt','PC_Geographic_2023Y_GE0001_20241214_1.txt']
for file_name in file_names:
    file_path = folder_name + file_name
    # creates a local file called database.db that you can query with SQL
    create_db_from_txt(file_path,'database.db')