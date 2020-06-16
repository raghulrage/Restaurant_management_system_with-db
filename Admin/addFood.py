from config import *

def addFood():
    foodName = input('Enter Food Name: ')
    cost = input('Enter Price per Food: ')
    try:
        sql = "INSERT INTO food(food_name, price) VALUES('{}','{}')".format(foodName,cost)
        cursor.execute(sql)
        connection.commit()
        print('\nFood added successfully..\n')
    except:
        print('\nSomething went wrong\n')
        main()
def main():
    while True:
        option = input('\n\n1. Add Food\n2. Delete Food\n3. Exit\n')
        if option == '1':
            addFood()
        elif option == '2':
            deleteFood()
        elif option == '3':
            exit()
        else:
            print('\nInvalid input\n')

main()
