void setup() {
  Serial.begin(9600);
  pinMode(button1Pin, INPUT);
  pinMode(button2Pin, INPUT);
  pinMode(button3Pin, INPUT);
}

void loop() {
  int potValue = analogRead(A0);
  int button1State = digitalRead(button1Pin);
  int button2State = digitalRead(button2Pin);
  int button3State = digitalRead(button3Pin);

  Serial.print(potValue);
  Serial.print(",");
  Serial.print(button1State);
  Serial.print(",");
  Serial.print(button2State);
  Serial.print(",");
  Serial.println(button3State);

  delay(10);
}
