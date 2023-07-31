const int leds[8] = {4,5,6,7, 8,9,10,11};
int sensorValue = 0;
int outputValue = 0;

void setup() {  
  for (int i = 0; i < 8; i++)
    pinMode(leds[i], OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  
  sensorValue = analogRead(A0);
  outputValue = map(sensorValue, 0, 1023, 0, 100);

  Serial.println(outputValue);
  String str = Serial.readString();
  
  if (str.startsWith("led")){
    int pos = str.indexOf(' ');
    String l = str.substring(pos+1, pos+2);
    int led = l.toInt() - 1;
    int state = str.endsWith("True")? HIGH : LOW;
    digitalWrite(leds[led], state);
   }
   
  delay(100);
}
