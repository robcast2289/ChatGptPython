void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  //pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  //pinMode(9, OUTPUT);

  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  //pinMode(13, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int button1 = digitalRead(10);
  int button2 = digitalRead(11);
  int button3 = digitalRead(12);
  if (Serial.available() > 0) {
    char estadoMonitor = Serial.read();
    if (estadoMonitor == 'A') {
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      Serial.println("Grupo Led A Encendidos");
    } else if (estadoMonitor == 'B') {
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
      Serial.println("Grupo Led B Encendidos");
    } else if (estadoMonitor == 'C') {
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      Serial.println("Grupo Led C Encendidos");
    /*} else if (estadoMonitor == 'D') {
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      Serial.println("Grupo Led D Encendidos");*/
    } else if (estadoMonitor == 'E') {
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      Serial.println("Grupo Led A Apagados");
    } else if (estadoMonitor == 'F') {
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
      Serial.println("Grupo Led B Apagados");
    } else if (estadoMonitor == 'G') {
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      Serial.println("Grupo Led C Apagados");
    /*} else if (estadoMonitor == 'H') {
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      Serial.println("Grupo Led D Apagados");*/      
    } else {
      Serial.println("Comando no reconocido");      
    }
  } else if (button1 == 1) {
    //Serial.write('A');
    int valor = digitalRead(2);
    Serial.println(valor);
    digitalWrite(2, !valor);
    digitalWrite(3, !valor);
    delay(500);
  } else if (button2 == 1) {
    int valor = digitalRead(4);
    digitalWrite(4, !valor);
    digitalWrite(5, !valor);
    delay(500);
  } else if (button3 == 1) {
    //Serial.write('C');
    int valor = digitalRead(7);
    digitalWrite(7, !valor);
    digitalWrite(8, !valor);
    delay(500);
  /*} else if (digitalRead(13) == LOW) {
    Serial.write('D');
    delay(100);*/
  } 
}