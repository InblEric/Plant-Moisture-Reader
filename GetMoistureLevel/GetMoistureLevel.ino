// set up the serial connection speed
int ready = 0;
int sensorPin = A0;
int sensorValue = 0;
int bucketPin = A5;
int bucketValue = 0;
int count = 0;

void setup() {
    Serial.begin(9600);
}

void loop() {
    int inByte;  
    if (ready == 1) {
        //mockSensorReading();
        moistureReading();
        count++;
        if(count >= 12) {
            //read water in bucket once an hour.
            bucketReading();
            count = 0;
        }
        delay(300000); //delay for 5 minutes
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

void mockBucketReading() {
    if(random(0,2) == 0) {
        Serial.println("We have enough water in the bucket");
    } else {
        Serial.println("Need more water in the bucket!");
    }
}

void mockSensorReading() {
    if(random(0,2) == 0) {
        Serial.println("We have enough water in the soil");
    } else {
        Serial.println("Need more water in the soil!");
    }
}

void moistureReading() {
    sensorValue = analogRead(sensorPin);
    Serial.print("moisture");
    Serial.println(sensorValue);
}

void bucketReading() {
    bucketValue = analogRead(bucketPin);
    Serial.print("bucket");
    Serial.println(bucketValue);
}
