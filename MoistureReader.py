import serial
import time
import WriteMoistureToFile as writer
import sys

'''set up the serial connection speed'''
ser = serial.Serial('/dev/ttyACM0', 9600)

print "Don't provide input until light on arduino is orange."


'''main loop'''

ready = 0
count = 0
cutoff = 500
listData = []

if(len(sys.argv)>1):
    if(sys.argv[1] > 0):
        try:
            cutoff = int(sys.argv[1])
            print "Cutoff set to " + str(cutoff) + " by argument value" 
        except:
            print "Bad argument value, cutoff set to " + str(cutoff) 
    else:
        print "Using default cutoff value of " + str(cutoff) 

def isReasonable(num):
    try:
        n = float(num)
        if (n < 0) or (n > 1000):           
            return False
    except:
        return False
    return True

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
        '''print "Starting to collect moisture data."'''
        response = ser.readline()
        '''print(response)'''
        if isReasonable(response):
            #MAKE IT SO IT WRITES EVERY TIME
            #WITH A REASONABLE VALUE
            #THE ARDUINO WILL TAKE CARE
            #OF THE SLEEPING
            
            #listData.append(float(response))
            #count += 1
        
            #if count >= cutoff:
        
            '''    #Get average and send
                total = 0.0
                for value in listData:
                    total += value
                dataAvg = float((float(total))/(float(count)))
        
                writer.sendData(dataAvg)
                print "writing data: " + str(dataAvg)
                count = 0
                listData = []'''
            writer.sendData(float(response))
            print "writing data: " + str(response)
            

