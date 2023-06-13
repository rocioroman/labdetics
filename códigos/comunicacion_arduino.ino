
#define pin_sensor A0
float Analog;


void setup() {
  // put your setup code here, to run once:
  pinMode (pin_sensor, INPUT);
  Serial.begin(9600);

}

void loop() {
  char buffer[30];
  char destination[8];
  float Analog = analogRead(pin_sensor)*(5.0 / 1023.0);
  dtostrf(Analog,5,2,destination); /*Double converted to string*/
  snprintf(buffer,  sizeof(buffer), "%s", destination);
  Serial.println(buffer);
  delay(100);
  
}
