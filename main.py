from menu import *
import json
from config import *

print('#'*10+' WELCOME '+'#'*10)

def checkUser(email):
    try:
        while True:
            sql = "SELECT email FROM customer WHERE email = '{}'".format(email)
            rows = cursor.execute(sql)
            if rows > 0:
                print('\nUser already exist!!\n')
            else:
                break
            email = input('Enter E-mail address or press Q to exit: ')
            if email.lower() == 'q':main()
        
    except Exception:
        print('\nError occured...\n')
        main()
        
def signup():
        
    name = input('\nEnter Full Name: ')

    email = input('\nEnter E-mail address: ')

    checkUser(email)
    
    mobileNo = input('\nEnter Mobile Number: ')

    password = input('\nEnter password: ')
    
    address = input('\nEnter Address: ')

    try:
        sql = "INSERT INTO customer(email, customer_name, mobile_no, address, password) VALUES('{}', '{}', '{}', '{}', '{}')".format(email, name, mobileNo, address, password)
        cursor.execute(sql)
        connection.commit()
        
    except Exception as e:
        print(e)
        main()
    
    print('\n'+'*'*10+'Signup Successful'+'*'*10+'\n')

    mainFn(name,email)
    main()

def validateEmail(email):
    try:
        while True:
            sql = "SELECT email FROM customer WHERE email = '{}'".format(email)
            rows = cursor.execute(sql)
            if rows == 0:
                print('\nUser does not exist!!\n')
            else: return email
            email = input('\nEnter E-mail ID or press Q to exit: ')
            if email.lower() == 'q':main()
    except :
        print('\nError occured!!!\n')
        main()

def validatePassword(password,email):
    try:
        count = 5
        while True:
            sql = "SELECT password FROM customer WHERE password = '{}' AND email = '{}'".format(password, email)
            rows = cursor.execute(sql)

            if rows > 0:
                return
            
            count -= 1
            print('\nPassword incorrect.',count,'attempt(s) more.\n')

            if count > 0:
                password = input('\nEnter Password: ')
            else:break
        main()
    except Exception as e:
        print('\nError occured\n',e)
        main()

def getUserName(email):
    try:
        sql = "SELECT customer_name FROM customer WHERE email = '{}'".format(email)
        cursor.execute(sql)
        name = cursor.fetchall()
        return name[0][0]
    except:
        print('\nError occured\n')
        main()
        
def login():
        
    while True:
        email = input('\nEnter E-mail ID: ')

        email = validateEmail(email)

        password = input('\nEnter Password: ')

        validatePassword(password,email)    

        name = getUserName(email)
        
        print('\n'+'*'*10+'Login Successful'+'*'*10+'\n')
        
        mainFn(name,email)
        main()
    
def main():     
    while True:
        print('\n'+' '*5+'1. Login\n'+' '*5+'2. Signup\n'+' '*5+'3. Exit\n')
        opt = input('Select an option : ')
        if opt == '3':
            connection.close()
            exit()
        elif opt == '1':
            login()
        elif opt == '2':
            signup()
        else:
            print('\nInvalid option, Enter again\n')
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Oops!',e.__class__,'error occured!!!')
        clear_data()

        

