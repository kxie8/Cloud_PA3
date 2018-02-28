
































import pymysql

import sys
import datetime

lastname = sys.argv[1]
date = sys.argv[4]
date_converted = datetime.datetime.strptime(date, '%Y-%m-%d')
check = date_converted.weekday()

conn = pymysql.connect(host='medicalcenter.martyhumphrey.info', port=3306, user='aardvark9', passwd='sparky12', db='Medical')
cur2 = conn.cursor()
statement2 = "SELECT Lastname FROM nurses"
cur2.execute(statement2)
cur2.close()

temp = False
for name in cur2:
    if lastname == name[0]:
        temp = True

if (temp == False):
    print("I am not aware of that person.")


if (check<5):    

    cur = conn.cursor()

    statement = "SELECT SlotStart,SlotEnd FROM nurses n JOIN nurse_sched ns ON n.ID = ns.NurseID Where SlotDate = '"+ date +"' AND Lastname = '"+lastname+"'"

    cur.execute(statement)
 

    for row in cur:
    
        print((row[0]))
        print(" to ")
        print((row[1]))
        print(".")


    cur.close()
    conn.close()
else: 
    
    print("The clinic is closed at that time.")
