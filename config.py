import pymysql
try:
    connection = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'restaurant_billing_system')

    cursor = connection.cursor()
except Exception as e:
    print(e)
