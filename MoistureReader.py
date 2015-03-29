import serial
import time
import WriteMoistureToFile as writer
import sys
import re

'''set up the serial connection speed'''
ser = serial.Serial('/dev/ttyACM0', 9600)

print "Don't press enter until the arduino light is orange."
ready = 0

def isReasonable(num):
    try:
        n = float(num)
        if (n < 0) or (n > 1000):           
            return False
    except:
        return False
    return True

'''main loop'''
while 1:
    if ready == 0:
        c = 'a' 
        raw_input('Press Enter to start ')
        if len(c) == 1:
            '''send write data back to arduino'''
            ser.write(c.encode())

            '''receive data from the arduino'''
            response = ser.readline()
 
            print(response)
            ready = 1
            
    else:
        response = ser.readline()
        if 'bucket' in response:
            response = re.sub("[^0-9]", "", response)
            if isReasonable(response):
                print "bucket water level: " + str(response)          
        elif 'moisture' in response:
            response = re.sub("[^0-9]", "", response)
            if isReasonable(response):            
                writer.sendData(float(response))
                print "writing data: " + str(response)            
        
            

