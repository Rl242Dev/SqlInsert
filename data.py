import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database='ArmaPanel',
    user='rl242',
    password='31#Nigi2'
)

mycursor = db.cursor()

sql = "INSERT INTO ArmaPanel.ArmaData (name, gang, bank, weapon) VALUES (%s, %s, %s, %s)"
val = [
    ('Ramuel Eag', 'Mercenaires', 7.2, 'Zafir 7.62'),
    ('Antonio Zook', 'Mercenaires', 14.7, 'Zafir 7.62'),
    ('Jack Andersonn', 'RLT', 2.1, 'Mk1 7.62'),
    ('Tac Campbell', 'Police', 4.4, 'Lynx 12.7'),
    ('Pierre pierron', 'BouBoule Gang', 17.4, 'Zafir 7.62'),
    ('Calvin M', 'Police', 8.9, 'Lynx 12.7'),
    ('Rachid L', 'RLT', 1.7, 'Zafir 7.62'),
    ('Raphael Nerleur', 'Medecins', 5.1, 'Null'),
    ('Nass Paco', 'CFRG', 2.8, 'Mk1 7.62'),
    ('Ali Boulawa', 'RLT', 1.8, 'Mk1 7.62'),
    ('Julien Gambini', 'Police', 11.2, 'Zafir 7.62'),
    ('Null', 'Null', 0.0, 'Null')
]

mycursor.executemany(sql, val)
db.commit()