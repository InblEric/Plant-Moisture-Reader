# Plant-Moisture-Reader
Reads moisture level of soil in order to keep track of watering your plants.


![alt tag](http://i.imgur.com/A4MXf7s.png)

Instructions:

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
11. Results will be written to a local /logs directory on your Pi with timestamps
12. The higher the number, the more moisture is present.
13. You can use whichever software you'd like to graph the data.

I read a value from the moisture sensor every 5 minutes. (Based on the delay in the arduino code).

I added a new file to allow graphing with python. Hopefully this will run automatically and host images to a server in the 
future, but for now it's a simple program that takes a file as a command line argument:
$ python GraphData.py <moisture-data-file-name>

It displays a graphical window plotting each data point (moisture on the vertical axis, time (in intervals of 5 minutes by 
default) on the horizontal axis).

I've been graphing values on Google Sheets. The output file can be imported directly (just make sure you name it "*.txt") to a 
spreadsheet. Choose insert>graph and change the color of the timestamps to no color (otherwise it's impossible to read).

Maybe excel will do a better job of graphing and actually label the horizontal axis instead of spamming the entire graph with 
annotations but I'll have to look into that later.

I will update with more instructions for graphing and hopefully automation for that sort of thing and potentially automatic 
watering controls, as well as instructions for the wiring (with picture).

Possible things coming: 

-Automatic Watering

-Server on RPI with rest API to control from anywhere

-Automatic long-term monitor scheduling

-Graphing on RPI with matplotlib

Current setup:

![alt tag](http://i.imgur.com/uqHtkuu.jpg)
