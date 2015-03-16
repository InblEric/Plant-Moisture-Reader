import serial
import time
import WriteMoistureToFile as writer

'''set up the serial connection speed'''
ser = serial.Serial('/dev/ttyACM0', 9600)

print "Don't provide input until light on arduino is orange."


'''main loop'''

ready = 0
count = 0
cutoff = 100
listData = []

while 1:
    if ready == 0:
        c = raw_input('Enter a char: ')
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
        print(response)
        listData.append(float(response))
        count += 1
        
        if count >= cutoff:
        
            #Get average and send
            total = 0.0
            for value in listData:
                total += value
            dataAvg = float((float(total))/(float(count)))
        
            writer.sendData(dataAvg)
            count = 0
            listData = []
