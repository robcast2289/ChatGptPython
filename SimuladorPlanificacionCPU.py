from tkinter import Tk, Canvas
from time import sleep
import random
import serial
from serial.tools.list_ports import comports

lag = 500
quantum = 1
count = 0
algoritmo = 2
llegadaProcess = 0
CantProcess = random.randint(25, 30)
    

Procesos = []

for x in range(CantProcess):
    tiempo = random.randint(1, 10)
    llegadaProcess += 1
    Procesos.append({"nombre":f"Proceso {x}","tiempo_llegada":x,"tiempo_ejecucion":tiempo,"tiempo_restante":tiempo})

def setup_serial():
    global puerto
    for port in comports():
        print(port)
    puerto = serial.Serial(comports()[0].device, 9600)
    #puerto = serial.Serial('/dev/ttyACM0',9600)
    sleep(2)

def draw():
    canvas.delete("all")
    for i in range(len(Procesos)):
        x = 50 + i * 30
        ymax = 10
        y = 60 +((ymax-Procesos[i]["tiempo_ejecucion"])*ymax)
        fill_color = "red" if i == count else "blue"
        tag = f"btn{i + 1}"
        canvas.create_rectangle(x, y, x + 20, y+((Procesos[i]["tiempo_ejecucion"]-Procesos[i]["tiempo_restante"])*ymax), fill="white", tags=(tag))
        canvas.create_rectangle(x, y+((Procesos[i]["tiempo_ejecucion"]-Procesos[i]["tiempo_restante"])*ymax), x + 20, 160, fill="red", tags=(tag))

    canvas.create_rectangle(100, 250, 250, 300, fill="green", tags=("Agregar"))
    canvas.create_text(175,275,text="Agregar Proceso",fill="white")

    if algoritmo == 0:
        canvas.create_rectangle(100, 350, 200, 400, fill="black", tags=("roundrobin"))
        canvas.create_text(150,375,text="Round Robin",fill="yellow")
    else:
        canvas.create_rectangle(100, 350, 200, 400, fill="yellow", tags=("roundrobin"))
        canvas.create_text(150,375,text="Round Robin",fill="black")

    if algoritmo == 1:
        canvas.create_rectangle(250, 350, 350, 400, fill="black", tags=("sjf"))
        canvas.create_text(275,375,text="SJF",fill="yellow")
    else:
        canvas.create_rectangle(250, 350, 350, 400, fill="yellow", tags=("sjf"))
        canvas.create_text(275,375,text="SJF",fill="black")

    if algoritmo == 2:
        canvas.create_rectangle(400, 350, 500, 400, fill="black", tags=("fifo"))
        canvas.create_text(425,375,text="FIFO",fill="yellow")
    else:
        canvas.create_rectangle(400, 350, 500, 400, fill="yellow", tags=("fifo"))
        canvas.create_text(425,375,text="FIFO",fill="black")

def agregar_proceso():
    tiempo = random.randint(1, 10)
    global llegadaProcess
    llegadaProcess += 1
    Procesos.append({"nombre":f"Proceso {llegadaProcess}","tiempo_llegada":llegadaProcess,"tiempo_ejecucion":tiempo,"tiempo_restante":tiempo})

    puerto.write(f"{chr(52)}\n".encode())
    puerto.write(f"{chr(53)}\n".encode())
    sleep(0.1)
    puerto.write(f"{chr(101)}\n".encode())
    puerto.write(f"{chr(102)}\n".encode())

def toggle_button(event):
    agregar_proceso()

def cambiar_algoritmo(alg):
    global algoritmo
    algoritmo = alg

    puerto.write(f"{chr(50)}\n".encode())
    puerto.write(f"{chr(51)}\n".encode())
    sleep(0.1)
    puerto.write(f"{chr(99)}\n".encode())
    puerto.write(f"{chr(100)}\n".encode())

def toggle_algoritmo(event):
    algoritmo_local = event.widget.gettags("current")[0]
    global algoritmo
    if algoritmo_local == 'roundrobin':
        cambiar_algoritmo(0)
    if algoritmo_local == 'sjf':
        cambiar_algoritmo(1)
    if algoritmo_local == 'fifo':
        cambiar_algoritmo(2)
    

def round_robin(count):
    if Procesos[count]["tiempo_restante"] - quantum <= 0:
        Procesos[count]["tiempo_restante"] = 0
    else:
        Procesos[count]["tiempo_restante"] -= quantum

    count+=1
    return count

def sjf():
    ProcesosTmp = sorted(Procesos,key=lambda proc: proc["tiempo_restante"])
    if ProcesosTmp[0]["tiempo_restante"] - quantum <= 0:
        ProcesosTmp[0]["tiempo_restante"] = 0
    else:
        ProcesosTmp[0]["tiempo_restante"] -= quantum

def fifo():
    ProcesosTmp = sorted(Procesos,key=lambda proc: proc["tiempo_llegada"])
    if ProcesosTmp[0]["tiempo_restante"] - quantum <= 0:
        ProcesosTmp[0]["tiempo_restante"] = 0
    else:
        ProcesosTmp[0]["tiempo_restante"] -= quantum

def update_canva(count):
    for i in range(len(Procesos)):
        if Procesos[i]["tiempo_restante"] == 0:
            Procesos.remove(Procesos[i])
            break

    if len(Procesos) == 0:
        draw()
        root.after(lag, update_canva, count)
        return
    if count >= len(Procesos):
        count = 0

    if algoritmo == 0:
        count = round_robin(count)
    if algoritmo == 1:
        sjf()
    if algoritmo == 2:
        fifo()

    puerto.write(f"{chr(48)}\n".encode())
    puerto.write(f"{chr(49)}\n".encode())
    sleep(0.25)
    puerto.write(f"{chr(97)}\n".encode())
    puerto.write(f"{chr(98)}\n".encode())

    draw()
    root.after(lag, update_canva, count)

def update_arduino():
    while puerto.in_waiting:
        data = puerto.readline().strip().decode()
        if data in ['F', 'G',]:
            if data == 'G':
                agregar_proceso()
            if data == 'F':
                global algoritmo
                if algoritmo == 2:
                    cambiar_algoritmo(0)
                else:
                    cambiar_algoritmo(algoritmo+1)

    root.after(10, update_arduino)


root = Tk()
width = 1250
height = 500
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
setup_serial()
draw()
for i in range(len(Procesos)):
    canvas.tag_bind(f"btn{i + 1}", "<Button-1>")
canvas.tag_bind("Agregar","<Button-1>",toggle_button)
canvas.tag_bind("roundrobin","<Button-1>",toggle_algoritmo)
canvas.tag_bind("sjf","<Button-1>",toggle_algoritmo)
canvas.tag_bind("fifo","<Button-1>",toggle_algoritmo)
root.after(lag, update_canva, count)
root.after(10, update_arduino)
root.mainloop()