from report import *
from config import *

#initialization
food_list = []
ordered_list = []
customer = ''

class Customer:
        def __init__(self, customer_id, email, customer_name, mobile_no ):
                self.customer_id = customer_id
                self.customer_name = customer_name
                self.mobile_no = mobile_no
                self.email = email
        
class Food:
        def __init__(self, food_id, name, price):
                self.food_id = food_id
                self.name = name
                self.price = int(price)

class Order(Food):
        def __init__(self, food_id, name, price, quantity):
                self.quantity = quantity
                self.total = quantity*price

                Food.__init__(self, food_id, name, price)

def getcustomerDetails(email):
        try:
                global customer
                sql = "SELECT * FROM customer WHERE email = '{}'".format(email)
                cursor.execute(sql)
                customer_details = cursor.fetchall()[0]
                customer = Customer(customer_details[0],customer_details[1],customer_details[2],customer_details[3])
        except Exception as e:
                print(e)
                print('\nError occured\n')
                
def load_food():
        try:
                global food_list
                sql = 'SELECT * FROM food'
                cursor.execute(sql)
                food_items = cursor.fetchall()
                for food in food_items:
                        food_list.append(Food(food[0],food[1],food[2]))
        except Exception as e:
                print(e)
                print('\nError Occured\n')
                
def menu():
        while True:
                print('\n'*5)
                print(' MAIN MENU '.center(60,'*')+'\n\n\t(O)Order Food\n\t(C)View Cart\n\t(R)Report\n\t(E)Exit\n'+'_'*60+'\n')
                option = input('Select an Option: ').upper()

                if option == 'O':
                        order_food()
                if option == 'C':
                        view_cart()
                if option == 'L':
                        logout()
                if option == 'E':
                        exit_menu()
                if option == 'R':
                        view_report()
                else:
                        print('Invalid option, Enter Again!!!')

def order_food():
        while True:
                print('\n'*5)
                print(' ORDER FOOD '.center(60,'*'))
                print('\n'+'\t'+'|NO|'.ljust(6,' ')+'|FOOD NAME|'.ljust(20,' ')+'|PRICE|'.ljust(10,' '))
                for i,food in enumerate(food_list):
                        print('\t{:<6}{:<20}Rs. {}'.format(i+1,food.name,food.price))
                print('\n'+'(M)Main Menu'+' '*10+'(C)View Cart'+' '*10+'(E)Exit')
                print('_'*60+'\n')

                food_id = input('Select Your Option: ')
                print()
                if food_id.isdigit():
                        if 0 < int(food_id) <= len(food_list):
                                while True:
                                    quantity = input('How many do you want to order(1-10) : ')
                                    if quantity.isdigit() and 0<int(quantity)<=10:
                                        quantity = int(quantity)
                                        break
                                    else:
                                        print('\nEnter valid data!!!!\n')
                                food = food_list[int(food_id)-1]
                                for i,item in enumerate(ordered_list):
                                        if item.name == food.name:
                                                print(ordered_list)
                                                ordered_list[i].quantity+=quantity
                                                ordered_list[i].total+=quantity*ordered_list[i].price
                                                break
                                else:
                                        ordered_list.append(Order(food.food_id,food.name,food.price,quantity))
                        else:
                                print('Enter valid data!!!')

                elif food_id.upper() == 'E':
                        exit_menu()
                elif food_id.upper() == 'C':
                        view_cart()
                elif food_id.upper() == 'M':
                        menu()
                else:
                        print('Invalid option, Enter Again!!!')

def view_cart():
        while 1:
                print('\n'*5)
                print(' CART '.center(60,'*')+'\n')
                total = 0
                if ordered_list:

                        print('\t|NO|'.ljust(5,' ')+'|FOOD NAME|'.ljust(15,' ')+'|PRICE x QUANTITY = TOTAL|'+'\n')
                        for i,food in enumerate(ordered_list):
                                total +=food.total
                                print('\t{:<5}{:<15}{:<5}x   {:<5} =  Rs.{:<4}'.format(i+1,food.name,food.price,food.quantity,food.total))
                        print('\t'+'-'*46)
                        print('\tTotal    '+('Rs. '+str(total)).rjust(35,' '))
                        print('\n(M)Main Menu'+' '*3+'(R)Remove Item'+' '*3+'(O)Order Food'+'\n'+'(P)Payment'+' '*5+'(E)Exit')
                        print('_'*60+'\n')
                        
                        option = input().upper()

                        if option == 'M':
                                menu()
                                
                        elif option == 'P':
                                payment(total)
                                
                        elif option == 'E':
                                exit_menu()
                                
                        elif option == 'O':
                                order_food()
                                
                        elif option == 'R':
                                remove_item()
                                
                        else:
                                print('Invalid option, Enter Again!!!')


                else:
                        print('\n'+'Cart is empty'.center(60,'-'))
                        menu()

def remove_item():
        option = input('\nEnter Number to Remove: ')
        
        if option.isalpha() or int(option) >  len(ordered_list):
                print('Invalid Input!!!')
        else:
                item = ordered_list.pop(int(option)-1)
                print(item.name+' Removed...')

def payment(total):
        if ordered_list:
                print('\nTotal amount: Rs.',total)
                report(total,ordered_list,customer)
                print('\n'+'Payment Successful!!!\n')
                
                clear_data()
        else:
                print('Cart is empty')
        menu()

def clear_data():
        global ordered_list
        ordered_list = []

def logout():
        global username, ordered_list
        username = ''
        orderedlist = []
        main()
        
def exit_menu():
        print('\n'+'THANK YOU'.center(50,'*'))
        quit()

def mainFn(name='',email=''):
        try:
                if name and email:
                        getcustomerDetails(email)
                        load_food()
                        menu()
                else:
                        print('Session Expired')
        except Exception as e:
                print(e)
                print('\nError Occured\n')
                menu()
