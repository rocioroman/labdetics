
#define pin_sensor A0
float Analog;
char buffer[50]


void setup() {
  // put your setup code here, to run once:
  pinMode (pin_sensor, INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Analog = analogRead (pin_sensor);
  sprintf(buffer,Analog)
  //sprintf(buffer,"%02X",Analog)
  Serial.println(buffer);
  delay(100);
}
