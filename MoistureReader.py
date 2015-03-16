import serial
import time

'''set up the serial connection speed'''
ser = serial.Serial('/dev/ttyACM2', 9600)

print "Don't provide input until light on arduino is orange."


'''main loop'''

ready = 0

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