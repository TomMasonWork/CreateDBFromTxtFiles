# CreateDBFromTxtFiles
Creates a sqlite database using statutory insurance data from .txt files, which are downloadable via FTP.

Here's how to connect Power BI to the database you just created.

1. Open Power BI and start a new report.
2. Click on the Get Data button on the top left of the Home tab. Click on More from the dropdown.
![Get_data](https://github.com/user-attachments/assets/d8bee55f-3c7a-4217-8f00-b1fe4a9a4387)

3. Type in odbc, then select ODBC on the right and click Connect.
   
![odbc](https://github.com/user-attachments/assets/44132c9c-058d-4447-891a-06c6f08773c9)

5. Choose SQLite3 from the dropdown as your Data Source Name and click Advanced Options. Type in database = and the path to where your db file is stored.
   
![sqlite](https://github.com/user-attachments/assets/634e2a98-1201-4590-9f4a-ff5b9bb03756)

Troubleshooting:
If you don't see SQLite as an option, you might need to download the driver. This is the one we use: http://www.ch-werner.de/sqliteodbc.
You might also have to sign in. I use my Windows authentication for that.

6. Pull in the tables you want.

![navigator3](https://github.com/user-attachments/assets/52d8a6bd-5c80-44b1-88b2-d4153c8f20de)

