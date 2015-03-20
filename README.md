# Plant-Moisture-Reader
Reads moisture level of soil in order to keep track of watering your plants.


![alt tag](http://i.imgur.com/A4MXf7s.png)

Upload the GetMoistureLevel.ino sketch to an arduino (I use an UNO).
On a Raspberry Pi (Or any machine connected to the arduino via USB) run the python script named MoistureReader.py. (You might 
have to change the location of the serial connection to the arduino on the line that has "ser = 
serial.Serial('/dev/ttyACM0', 9600)" based on which USB port you use.

I read a value from the moisture sensor every 5 minutes. (Based on the delay in the arduino code).

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
