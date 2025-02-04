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
            sp_id INTEGER PRIMARY KEY,
            SNLStatKey TEXT,
            NAICCompanyCode TEXT,
            PeriodEnded TEXT,
            DateEnded DATE,
            AnnualizationFactor REAL,
            FiscalPeriod TEXT,
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
                AnnualizationFactor,
                FiscalPeriod,
                LineOfBusiness,
                Geography,
                DirectPremiumsWritten,
                DirectSimpleCombinedRatio) VALUES (?,?,?,?,?,?,?,?,?,?)
        '''

        values_list = [1,2,3,4,5,6,7,8,9,26]

    if 'GE0003' in txt_file:

        sql_create_table = '''
        CREATE TABLE IF NOT EXISTS StateStatus (
            ss_id INTEGER PRIMARY KEY,
            SNLStatKey TEXT,
            NAICCompanyCode TEXT,
            PeriodEnded TEXT,
            DateEnded DATE,
            AnnualizationFactor REAL,
            FiscalPeriod TEXT,
            Geography TEXT,
            ActiveStatus TEXT)
        '''

        sql_insert_data = '''
            INSERT INTO StateStatus (
                SNLStatKey,
                NAICCompanyCode,
                PeriodEnded,
                DateEnded,
                AnnualizationFactor,
                FiscalPeriod,
                Geography,
                ActiveStatus) VALUES (?,?,?,?,?,?,?,?)
        '''

        values_list = [1,2,3,4,5,6,7,9]

    if 'SI0001' in txt_file:

        sql_create_table = '''
            CREATE TABLE IF NOT EXISTS StatIndex (
                si_id INTEGER PRIMARY KEY,
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
                gd_id INTEGER PRIMARY KEY,
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

    if 'CorporateCompanyInformation' in txt_file:

        sql_create_table = '''
            CREATE TABLE IF NOT EXISTS CorporateCompanyInformation (
                cci_id INTEGER PRIMARY KEY,
                FilingCompany TEXT,
                SERFFFilingEntityEventKey INT,
                DispositionDate DATE,
                EntityName TEXT,
                NAICCompanyCode TEXT,
                SNLStatKey TEXT)
        '''

        sql_insert_data = '''
            INSERT INTO CorporateCompanyInformation (
                FilingCompany,
                SERFFFilingEntityEventKey,
                DispositionDate,
                EntityName,
                NAICCompanyCode,
                SNLStatKey) VALUES (?,?,?,?,?,?)
        '''

        values_list = [1,2,3,4,6,14]

    if 'DispositionInformation' in txt_file:

        sql_create_table = '''
            CREATE TABLE IF NOT EXISTS DispositionInformation (
                disp_id INTEGER PRIMARY KEY,
                FilingCompany TEXT,
                SERFFFilingEntityEventKey INT,
                DispositionDate DATE,
                PctIndicatedChange FLOAT,
                PctRateImpact FLOAT,
                WrittenPremiumChange BIGINT,
                NumberOfPolicyholders BIGINT,
                WrittenPremium BIGINT
                )
        '''

        sql_insert_data = '''
            INSERT INTO DispositionInformation (
                FilingCompany,
                SERFFFilingEntityEventKey,
                DispositionDate,
                PctIndicatedChange,
                PctRateImpact,
                WrittenPremiumChange,
                NumberOfPolicyholders,
                WrittenPremium) VALUES (?,?,?,?,?,?,?,?)
        '''

        values_list = [1,2,3,5,6,7,8,9]

    if 'GeneralInformation' in txt_file:

        sql_create_table = '''
            CREATE TABLE IF NOT EXISTS GeneralInformation (
                gi_id INTEGER PRIMARY KEY,
                FilingCompany TEXT,
                SERFFFilingEntityEventKey INT,
                TypeOfInsurance TEXT,
                SubTypeOfInsurance TEXT,
                FilingStatus TEXT
                )
        '''

        sql_insert_data = '''
            INSERT INTO GeneralInformation (
                FilingCompany,
                SERFFFilingEntityEventKey,
                TypeOfInsurance,
                SubTypeOfInsurance,
                FilingStatus) VALUES (?,?,?,?,?)
        '''

        values_list = [1,2,7,9,21]

    if 'RateFilingsCompanyInformation' in txt_file:

        sql_create_table = '''
            CREATE TABLE IF NOT EXISTS RateFilingsCompanyInformation (
                rfci_id INTEGER PRIMARY KEY,
                FilingCompany TEXT,
                SERFFFilingEntityEventKey INT,
                FilingState TEXT
                )
        '''

        sql_insert_data = '''
            INSERT INTO RateFilingsCompanyInformation (
                FilingCompany,
                SERFFFilingEntityEventKey,
                FilingState) VALUES (?,?,?)
        '''

        values_list = [1,2,4]

    # create table
    cursor.execute(sql_create_table)

    # read data from text file
    with open(txt_file,'r',encoding='utf-8') as file:
        for line in file:
            values = line.strip().split('|')
            values_tuple = ()
            for i in range(len(values)):
                if i in values_list:
                    values_tuple = values_tuple + (values[i],)
            cursor.execute(sql_insert_data,values_tuple)

    # commit changes
    conn.commit()
    # close connection
    conn.close()

def process_files(file_names,folder_name,db_file):
    for file_name in file_names:
        file_path = folder_name + file_name
        # creates a local file called database.db that you can query with SQL
        create_db_from_txt(file_path,db_file)

# create name for your local database
db_file = 'database.db'

# replace with the file path where your txt files are located
folder_name = 'PATH/TO/YOUR/FILES'

file_names = ["StatIndex_SI0001_PC_20250117_1.txt",
              "StatIndex_SI0002_PC_20250117_1.txt",
              "PC_Geographic_2023Y_GE0001_20250118_1.txt",
              "PC_Geographic_2023Y_GE0003_20250118_1.txt",
              "PC_Geographic_2022Y_GE0001_20250118_1.txt",
              "PC_Geographic_2022Y_GE0003_20250118_1.txt",
              "PC_Geographic_2021Y_GE0001_20250118_1.txt",
              "PC_Geographic_2021Y_GE0003_20250118_1.txt",
              "PC_InsuranceProductFilings_2024Y_CorporateCompanyInformation_20250111_1.txt",
              "PC_InsuranceProductFilings_2024Y_DispositionInformation_20250111_1.txt",
              "PC_InsuranceProductFilings_2024Y_GeneralInformation_20250111_1.txt",
              "PC_InsuranceProductFilings_2024Y_RateFilingsCompanyInformation_20250111_1.txt"
              ]

process_files(file_names,folder_name,db_file)