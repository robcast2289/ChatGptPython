import serial, time

cone = serial.Serial('/dev/ttyACM0',9600)
valor = "A"
#time.sleep(2)
#cone.write(valor.encode('ascii'))
#cone.write(b"B")
#b=cone.readline()
#cone.close()
#
#print(b.decode("utf-8"))
time.sleep(2)

while True:
    prompt = input("\nOpcion: ")

    if prompt == "exit":
        break

    option = prompt.encode()

    cone.write(option)
    b=cone.readline()
    
    print(b.decode("utf-8"))