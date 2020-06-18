import pymysql
try:
    connection = pymysql.connect(
        host = 'localhost',
        user = 'raghul',
        password = 'dhanya295939',
        database = 'restaurant_billing_system')

    cursor = connection.cursor()
except Exception as e:
    print(e)
