import mysql.connector
import time
from datetime import datetime

fakeDataPoint = [4000]
timeIntervals = [2,1,0.5,0.2]   # In seconds (e.g. 0.2 is 0.2 seconds; 200 milliseconds)

cnx = mysql.connector.connect(user='root', password='#########',
                              host='localhost',
                              database='testdata')

cursor = cnx.cursor()

addData  = ("INSERT INTO testdata "
            "(data) "
            "VALUES (%s)")
queryData = ("SELECT time FROM testdata")

times = []

for interval in timeIntervals:
    for i in range(10):
        instanceTime = datetime.now()
        cursor.execute(addData, fakeDataPoint)
        cnx.commit()
        time.sleep(interval)
        times.append(instanceTime)

cursor.execute(queryData)

returnedTimes = []

for returnedTime in cursor:
    print(returnedTime)
    returnedTimes.append(returnedTime[0])

pairing = []

i = 0
for item in returnedTimes:
    timeTuple = (item, times[i])
    pairing.append(timeTuple)
    i += 1

for pair in pairing:
    delta = pair[0]-pair[1]
    print(delta.total_seconds())