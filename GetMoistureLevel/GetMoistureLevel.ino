// set up the serial connection speed
int ready = 0;
int sensorPin = A0;
int sensorValue = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int inByte;
  if (ready == 1) {
    //mockSensorReading();
    moistureReading();
    //SLEEP SO AS TO
    //NOT OVER-STRESS
    //THE SENSOR
    delay(600000) //delay for 10 minutes
  } else {
    if (Serial.available() > 0) {
      //read data from RPI
      inByte = Serial.read();
    
      //send data to RPI
      Serial.write(inByte);
      Serial.print(" = ");
      Serial.print(inByte);  
      ready = 1;      
    
    }
  }
  
}

void mockSensorReading() {
    if(random(0,2) == 0) {
      Serial.println("We have enough water");
    } else {
      Serial.println("Need more water!");
    }
}

void moistureReading() {
  sensorValue = analogRead(sensorPin);
  Serial.println(sensorValue);
}
