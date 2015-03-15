import time

localtime = time.localtime()
ts = str(localtime.tm_year) + "-" + str(localtime.tm_mon) + "-" + str(localtime.tm_mday) + ":" + str(localtime.tm_hour) + "-" + str(localtime.tm_min)
fName = "logs/" + str(ts)

f = open(fName,'w')
f.write("MoistureData:\n")

def sendData(data):
    f.write(str(data) + "\n")