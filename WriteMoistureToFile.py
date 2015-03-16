import time

localtime = time.localtime()
ts = str(localtime.tm_year) + "-" + str(localtime.tm_mon) + "-" + str(localtime.tm_mday) + ":" + str(localtime.tm_hour) + "-" + str(localtime.tm_min)
fName = "logs/" + str(ts)

f = open(fName,'w')
f.write("MoistureData:\n")

def sendData(data):
    curtime = time.localtime()
    ts = str(curtime.tm_year) + "-" + str(curtime.tm_mon) + "-" + str(curtime.tm_mday) + ":" + str(curtime.tm_hour) + "-" + str(curtime.tm_min)
        
    f.write(str(data) + ", " + str(ts) + "\n")
