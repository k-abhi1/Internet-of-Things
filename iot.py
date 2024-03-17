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