from datetime import datetime
from pytz import timezone
import json
from menu import *
from config import *
def updateOrder(total,ordered_list,customer):
    try:
        sql = "INSERT INTO orders(customer_id, total) VALUES('{}', '{}')".format(customer.customer_id, total)
        orderId = cursor.execute(sql)
        connection.commit()
        orderId = cursor.lastrowid
        for food in ordered_list:
            sql = "INSERT INTO order_details(order_id, food_id, quantity) VALUES('{}', '{}', '{}')".format(orderId, food.food_id, food.quantity)
            cursor.execute(sql)
        connection.commit()
        
    except Exception as e:
        print(e)
        print('\nError Occured\n')
        
def report(total, ordered_list, customer):

    updateOrder(total,ordered_list,customer)

    file = open('Report/report.txt','a')
    report_data = '\n' + '\t\t' + '*'*40 + '\n'

    now = datetime.now()
    date = '-'.join(list(map(str,[now.day,now.month,now.year])))

    now_utc = datetime.now(timezone('UTC'))
    time = now_utc.astimezone(timezone('Asia/Kolkata'))
    time = time.strftime("%I:%M:%S %p" )

    report_data += '\t\t' + date.center(40,' ') + '\n' + '\t\t' + time.center(40,' ') + '\n' + '\t\t' + '-'*40 + '\n'
    
    for i,item in enumerate(ordered_list):
        temp = '\t\t  ' + str(i+1) + ' '*2 +  item.name.ljust(15,' ') + str(item.quantity) + ' x ' + str(item.price) + ' = ' + 'Rs. '+str(item.total) + '\n'
        report_data += temp
        
    report_data += '\t\t' + '_'*40 + '\n' + '\t\t' + '  Total' + ' '*20 + 'Rs. ' + str(total) + '\n\n'
    report_data += '\t\t' + '*'*40 + '\n'

 
    report_data +='\t\t'+customer.customer_name.center(40,' ') + '\n' + '\t\t' + customer.mobile_no.center(40,' ')+'\n\n'
    report_data += '\t\t' + '*'*40 + '\n\n'                                                                                                       
    
    file.write(report_data)

def view_report():
        report = open('Report/report.txt','r').read()
        print(report)
