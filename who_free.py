































import pymysql
import sys
import datetime

question = sys.argv[1]

parselist = question.split(" ")

time = sys.argv[1]
date = sys.argv[3]

conn = pymysql.connect(host='medicalcenter.martyhumphrey.info', port=3306, user='aardvark9', passwd='sparky12', db='Medical')

year,month,day = (int(x) for x in date.split('-'))
time_converted = datetime.datetime.strptime(time, '%H:%M:%S')
workhourS = datetime.datetime.strptime('09:00:00', '%H:%M:%S')
workhourE = datetime.datetime.strptime('17:00:00', '%H:%M:%S')
date_converted = datetime.datetime.strptime(date, '%Y-%m-%d')
check = date_converted.weekday()


if (check<5 and (workhourS <= time_converted <= workhourE )):

    cur = conn.cursor()

    statement = "SELECT * FROM nurses n JOIN nurse_sched ns ON n.ID = ns.NurseID Where SlotDate = '" + date  + "' AND (SlotStart <= '" + time +"' AND SlotEnd >= '" + time  + "' )"


    cur.execute(statement)



    for row in cur:
        print(row[1] + " "+ row[2] + ".")

    
    cur.close()
    conn.close()

else:
    print ("The clinic is closed at that time.")


