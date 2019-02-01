import mysql.connector

config = {
  'user': 'your_username',
  'password': 'your_password',
  'host': '127.0.0.1',
  'database': 'your_database',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)
conn.close()