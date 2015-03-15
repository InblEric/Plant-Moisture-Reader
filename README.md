# Plant-Moisture-Reader
Reads moisture level of soil in order to keep track of watering your plants.

Upload the GetMoistureLevel.ino sketch to an arduino (I use an UNO).
On a Raspberry Pi (Or any machine connected to the arduino via USB) run the python script named MoistureReader.py. (You will likely have to change the location of the serial connection to the arduino on the line that has "ser = serial.Serial('/dev/ttyACM1', 9600)" based on which USB port you use.

