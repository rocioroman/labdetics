
#define pin_sensor A0
float Analog;


void setup() {
  // put your setup code here, to run once:
  pinMode (pin_sensor, INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Analog = analogRead (pin_sensor)/1023.0;
  Serial.println(Analog);
  delay(100);
}
