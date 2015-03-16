import time

localtime = time.localtime()
ts = str(localtime.tm_year) + "-" + str(localtime.tm_mon) + "-" + str(localtime.tm_mday) + ":" + str(localtime.tm_hour) + "-" + str(localtime.tm_min)
fName = "logs/" + str(ts)

f = open(fName,'w')
f.write("MoistureData:\n")

def sendData(data):
    #INSTEAD, HOLD AN EMPTY LIST
    #AND EVERY 100, entries, AVERAGE THAT
    #AND WRITE THAT WITH A TIMESTAMP
    #THEN CLEAR THE LIST AND RESET THE COUNT
    f.write(str(data) + "\n")
