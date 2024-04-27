import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Cambia '/dev/ttyUSB0' al puerto serial correspondiente en tu sistema

while True:
    data = ser.readline().decode().strip()  # Leer los datos y decodificarlos
    values = data.split(',')  # Separar los datos por comas
    pot_value = int(values[0])
    button1_state = int(values[1])
    button2_state = int(values[2])
    button3_state = int(values[3])

    print("Potentiometer:", pot_value)
    print("Button 1 State:", button1_state)
    print("Button 2 State:", button2_state)
    print("Button 3 State:", button3_state)
