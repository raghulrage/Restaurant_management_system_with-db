import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'restaurant_billing_system')

cursor = connection.cursor()
