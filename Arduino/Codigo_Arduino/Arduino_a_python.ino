const int NUM_BOTONES = 3;
int ledPins[] = {2, 3, 4, 5, 7, 8};
int boutonPins[] = {10, 11, 12};
int numPins = sizeof(ledPins) / sizeof(ledPins[0]);
int numBoton = sizeof(boutonPins) / sizeof(boutonPins[0]);
char grupo[] = {'A', 'B', 'C'};
char grupo2[] = {'E', 'F', 'G'};
bool botonPresionado[NUM_BOTONES] = {false}; 

void setup() {
  for (int i = 0; i < numPins; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
  for (int i = 0; i < numBoton; i++) {
    pinMode(boutonPins[i], INPUT);
  }
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < numBoton; i++) {
    if (digitalRead(boutonPins[i]) == LOW && !botonPresionado[i]) {
      Serial.println(grupo[i]);
      botonPresionado[i] = true;
      delay(100);
      return;
    } else if (digitalRead(boutonPins[i]) == HIGH && botonPresionado[i]) {
      Serial.println(grupo2[i]);
      botonPresionado[i] = false;
      delay(100);
      return;
    }
  }
  if (Serial.available() > 0) {
    char estadoMonitor = Serial.read();
    int grupoIndex = -1;
    for (int i = 0; i < sizeof(grupo); i++) {
      if (estadoMonitor == grupo[i] || estadoMonitor == grupo2[i]) {
        grupoIndex = i;
        break;
      }
    }
    if (grupoIndex != -1) {
      for (int i = grupoIndex * 2; i < (grupoIndex * 2) + 2; i++) {
        digitalWrite(ledPins[i], (estadoMonitor == grupo[grupoIndex]) ? HIGH : LOW);
      }
      Serial.println((estadoMonitor == grupo[grupoIndex]) ? "1" : "0");
    } else if (estadoMonitor >= '0' && estadoMonitor <= '7') {
      int ledIndex = estadoMonitor - '0';
      digitalWrite(ledPins[ledIndex], HIGH);
      Serial.println("LED encendido");
    } else if (estadoMonitor >= 'a' && estadoMonitor <= 'h') {
      int ledIndex = estadoMonitor - 'a';
      digitalWrite(ledPins[ledIndex], LOW);
    }
  }
}