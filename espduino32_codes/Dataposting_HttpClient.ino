/**
   Created the Erbynn, Josiah, Ike
   date 20/05/2019

    

*/
//////////////////Sensor Libraries ///////////////////////
#include <Wire.h>
#include <Adafruit_ADS1015.h>

#include <OneWire.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 14               // GPIO pin on which the DS18B20 is connected :D5 on esp12e

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature DS18B20(&oneWire);

///////////////////pins numbers and thier declarations //////////////////
// lcd ----- SDA=D2/GPIO4,  SCL=D1/GPIO5
const int trigPin = D7;
const int echoPin = D8;
// defines variables
long duration;
int distance;
int tankheight=27;
int mydistance;


#define analogpin A0
int sensorval=0;
long int avgval;
float b;
// #define turbpin adc0
int buf[10],temp ;
int senseRawValue; //Some variable
float senseTurbidity; //Some floating variable


//SDA=D2/GPIO4,  SCL=D1/GPIO5 to connect the adc1115 properly.

Adafruit_ADS1115 ads(0x48);
float Voltage = 0.0;

////////////////////////////////////////////

#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#include <ESP8266HTTPClient.h>

#include <WiFiClient.h>

ESP8266WiFiMulti WiFiMulti;

void setup() {

  Serial.begin(115200);
  // Serial.setDebugOutput(true);

  Serial.println();
  Serial.println();
  Serial.println();

  for (uint8_t t = 4; t > 0; t--) {
    Serial.printf("[SETUP] WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }

  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP("WorkSHop", "inf12345");

////////////////////Setup for the sensors//////////////////////


  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  ads.begin(); //  enables the ADC1115 
  Serial.println("Initializing All Sensors..................");
    
///////////////////////////////////////////////////
}

void loop() {
  //////// capturing sensor data values///////////////
 float temp,turb,ph,level;

 temp= mytemp();
 turb=myturb();
 ph=myph();
 level=mylevel();
  
  // wait for WiFi connection
  if ((WiFiMulti.run() == WL_CONNECTED)) {

    WiFiClient client;

    HTTPClient http;
   

    Serial.print("[HTTP] begin...\n");
    if (http.begin(client, "http://10.10.65.28:5050/postData")) {  // HTTP or ip address to connect to

    String data = String(temp)+","+String(turb)+","+String(ph)+","+String(level);
    Serial.println(data);
      Serial.print("[HTTP] GET...\n");
      http.addHeader("Content-Type","text/plain");
      // start connection and send HTTP header
      int httpCode = http.POST(data);

      // httpCode will be negative on error
      if (httpCode > 0) {
        // HTTP header has been send and Server response header has been handled
        Serial.printf("[HTTP] GET... code: %d\n", httpCode);

        // file found at server
        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          String payload = http.getString();
          Serial.println(payload);
        }
      } else {
        Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
      }

      http.end();
    } else {
      Serial.printf("[HTTP} Unable to connect\n");
    }
  }

  delay(10000);
}


///////////////////////Various Sensor functions/////////////////////////
float myph(){
  
  for(int i=0;i<10;i++){
    buf[i]= analogRead(analogpin);
    delay(100);
    }
  for(int i=0;i<9;i++){
    for(int j=i;j<10;j++){
      if(buf[i]>buf[j]){
        temp=buf[j];
        buf[i]=buf[j];
        buf[j]=temp;       
        
        }      
      }
       
    }  
  avgval=0;
  for(int i=2;i<8;i++){avgval+=buf[i];    }

  float phvol=(float)avgval*5.0/1024/6 ;
  float phval= -3.6585*phvol+21.864;   /// to calculate the ph of various substance
  Serial.print("pH Value:  ");
  Serial.println(phval);
  return phval;
  //Serial.print("Voltage = ");
  //Serial.println(phvol);
  delay(1000);
  
  }

float myturb(){
  int16_t adc0;  // we read from the ADC, we have a sixteen bit integer as a result

  adc0 = ads.readADC_SingleEnded(0);
  Voltage = (adc0 * 0.1875)/1000;
  float volt5= Voltage+1 ;        ///to round Voltage above to 5V(reqire voltage)
 // Serial.println(adc0); 
 // Serial.println(volt5);        // print nw voltage that would bbe read by turb sensor
//senseRawValue = analogRead(adc0); //Read input raw value fromt the sensor
senseTurbidity = volt5;    //senseRawValue * (5.0 / 1024.0); //Convert analog data from 0 -1024 to voltage 0 - 5v;
Serial.print("TURBIDITY VALUE:  "); //Print the output data to the serial
Serial.print(senseTurbidity);
Serial.print("\n");
return senseTurbidity;
delay(1000);

 // increased turbidity, our voltage drops 

  if (senseTurbidity>3.2 ){
     Serial.print("\t Water is clear \n");
    }
   
  if (senseTurbidity<3.2 && senseTurbidity>2.9 ){
     Serial.print("\t Water is a little cloudy \n");
    }

   
  else if(senseTurbidity<2.9)
    Serial.print("\t Warning!!. Water is muddy/very cloudy!!! \n");
   
  }

 float mylevel(){
  
      // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
    // Calculating the distance
    mydistance= duration*0.034/2;
    distance= tankheight-mydistance;
    return distance;
    // Prints the distance on the Serial Monitor
    Serial.print("Distance: ");
    Serial.print(distance);
          if (distance<10&& distance>=5){
    Serial.print("\t The water level: FULL \n");
    }

      else if (distance>10 && distance<16){
    Serial.print("\t The water level: NORMAL\n");
    }

      else if (distance>16){
    Serial.print("\t The water level: LOW \n");
    }
    
    delay(1000);


  }

  float mytemp(){
    float temp;
  DS18B20.requestTemperatures(); 
  temp=DS18B20.getTempCByIndex(0);
  Serial.print("Temperature: ");
  Serial.println(temp);
  return temp;
  delay(1000);
  }
