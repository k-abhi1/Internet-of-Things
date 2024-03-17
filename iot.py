/* Comment this out to disable
prints and save space */ 
#define
BLYNK_PRINT Serial
#include
<ESP8266WiFi.h>
#include
<BlynkSimpleEsp8266.
h>
// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "2301f2e9572a41aeb096fe4bb31a3fa6";
// Your WiFi credentials.
// Set password to "" for
open networks. char ssid[]
= "Questease Solutions";
char pass[] =
"Fareeha08";
void setup()
{

// Debug console
Serial.begin(9600);
Blynk.begin(auth,
ssid, pass);
// You can also specify server:
//Blynk.begin(auth, ssid, pass, "blynk-cloud.com", 80);
//Blynk.begin(auth, ssid, pass, IPAddress(192,168,1,100), 8080);
}
void loop()
{
Blynk.run();
}
void setup() {

// put your setup code
here, to run once:
pinMode(D4,OUTPUT); .
}
void loop() {
// put your main code here, to
run repeatedly:
digitalWrite(D4,HIGH);
delay(5000);
digitalWrite(D4
,LOW);
delay(5000);
}
void setup() {
// put your setup code
here, to run once:
pinMode(5,OUTPUT);
pinMode(7,OUTPUT);
pinMode(9,OUTPUT);
}
void loop() {

// put your main code here, to
run repeatedly:
digitalWrite(5,HIGH);
delay(5000);
digitalWrite(5,
LOW);
delay(5000);
digitalWrite(7,
HIGH);
delay(500);
digitalWrite(7,
LOW);
delay(500);
digitalWrite(7,
HIGH);
delay(500);
21
digitalWrite(7,
LOW);
delay(500);
digitalWrite(7,
HIGH);
delay(500);
digitalWrite(7,
LOW);
delay(500);
digitalWrite(7,
HIGH);
delay(500);
digitalWrite(7,
LOW);
delay(500);
digitalWrite(9,
HIGH);
delay(5000);
digitalWrite(9,
LOW);
delay(5000);
} 

#python code................     <-----------

# Import required libraries
import BlynkLib
import network
import machine
import time

# Blynk authentication token
auth = '2301f2e9572a41aeb096fe4bb31a3fa6'

# WiFi credentials
ssid = 'Questease Solutions'
password = 'Fareeha08'

# Initialize Blynk
blynk = BlynkLib.Blynk(auth, server='blynk-cloud.com')

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    pass

# Setup pin modes
pin_D4 = machine.Pin(2, machine.Pin.OUT)
pin_5 = machine.Pin(5, machine.Pin.OUT)
pin_7 = machine.Pin(7, machine.Pin.OUT)
pin_9 = machine.Pin(9, machine.Pin.OUT)

# Main loop
while True:
    # Blynk.run()
    blynk.run()

    # Toggle D4 pin
    pin_D4.on()
    time.sleep(5)
    pin_D4.off()
    time.sleep(5)

    # Toggle 5 pin
    pin_5.on()
    time.sleep(5)
    pin_5.off()
    time.sleep(5)

    # Toggle 7 pin multiple times
    for _ in range(3):
        pin_7.on()
        time.sleep(0.5)
        pin_7.off()
        time.sleep(0.5)

    # Toggle 9 pin
    pin_9.on()
    time.sleep(5)
    pin_9.off()
    time.sleep(5)
