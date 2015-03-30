# Plant-Moisture-Reader
Reads moisture level of soil in order to keep track of watering your plants.


![alt tag](http://i.imgur.com/A4MXf7s.png)

Instructions:
-------------

1. Clone this repo to a Raspberry Pi (I run Debian Wheezy on mine).
2. Download the Arduino IDE onto your Raspberry Pi.
3. Connect your Arduino to your Raspberry Pi via USB.
4. Verify which serial port on your Pi your Arduino is connected to (check for /dev/ttyA*)
5. Change line 7 of MoistureReader.py (ser = serial.Serial('/dev/ttyACM0', 9600)) to use the correct serial port.
6. Attach your moisture sensor to your Arduino as shown in the diagram above.
7. Place moisture sensor into soil in area you would like to monitor.
8. Upload the GetMoistureLevel sketch to your arduino.
9. Run the MoistureReader python script on your Raspberry Pi
10. Kill the python process when you want to stop. (Plan to make this more elegant later)




    $ python MoistureReader.py
    
10. Kill the python process when you want to stop. (Plan to make this more elegant later)
11. Results will be written to a local /logs directory on your Pi with timestamps
12. The higher the number, the more moisture is present.
13. You can use whichever software you'd like to graph the data, or you can see the graphing section below.

Overview:
---------

I read a value from the moisture sensor every 5 minutes. (Based on the delay in the arduino code). I now also read data from a
water sensor. This is used to measure how much water is in the bucket I will use for my reservoir. All it does right now is 
print the value to console.

Graphing:
---------

I added a new file to allow graphing with python. Hopefully this will run automatically and host images to a server in the 
future, but for now it's a simple program that takes a file as a command line argument:

    $ python GraphData.py <moisture-data-file-name>

It displays a graphical window plotting each data point (moisture on the vertical axis, time (in intervals of 5 minutes by 
default) on the horizontal axis).

You can graph the raw data in excel or google sheets if you prefer (or whatever you want).

Future plans: 
-------------

-Automatic Watering

-Automatic email to remind user to fill water reservoir

-Server on RPI with rest API to control/monitor from anywhere

-Automatic long-term monitor scheduling

-Automatic graphing on RPI with matplotlib

Current setup:
--------------

![alt tag](http://i.imgur.com/uqHtkuu.jpg)
