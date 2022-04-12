import mysql.connector # pip install mysql-connector-python

db = mysql.connector.connect(
    host='localhost',
    database='ArmaPanel', # Your database name
    user='****', # Your username in mysql
    password='*****' # Your password in mysql
)

mycursor = db.cursor()

sql = "INSERT INTO db_name.table_name (column_1, column_2, column_3, column_4) VALUES (%s, %s, %s, %s)" # Chnage the number of "%s" and column according to the number of column in your table
val = [
    ('***', '***', ***, '***'), # char, char, int/float, char
    ('***', '***', ***, '***'), # char, char, int/float, char
]

mycursor.executemany(sql, val)
db.commit() 
