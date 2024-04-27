from tkinter import Tk, Canvas
import serial
from serial.tools.list_ports import comports
from time import sleep

estado_leds = [0, 0, 0, 0, 0, 0]
estado_botones = [0, 0, 0]
color = ["red", "red", "yellow", "yellow", "green", "green"]

def setup_serial():
    global puerto
    for port in comports():
        print(port)
    puerto = serial.Serial(comports()[0].device, 9600)
    #puerto = serial.Serial('/dev/ttyACM0',9600)
    sleep(2)
def draw():
    canvas.delete("all")
    for i, estado in enumerate(estado_leds):
        x = 50 + i * 150
        fill_color = color[i] if estado_leds[i] == 1 else "white"
        tag = f"led{i + 1}"
        canvas.create_oval(x, 100, x + 100, 200, fill=fill_color, tags=(tag))
    for i in range(len(estado_botones)):
        x = 50 + i * 150
        fill_color = "black" if estado_botones[i] == 1 else "white"
        tag = f"btn{i + 1}"
        canvas.create_rectangle(x, 400, x + 100, 300, fill=fill_color, tags=(tag))
def toggle_group(event):
    group = int(event.widget.gettags("current")[0][-1]) - 1
    estado_botones[group] = 1 - estado_botones[group]
    group_leds = [group * 2, group * 2 + 1]
    led_color = color[group] if estado_botones[group] == 1 else "white"
    for led in group_leds:
        estado_leds[led] = estado_botones[group]
    puerto.write(f"{chr(group + 65) if estado_botones[group] == 1 else chr(group + 69)}\n".encode())
    draw()
def toggle_led(event):
    tag = event.widget.find_withtag("current")[0]
    tag_str = event.widget.gettags(tag)[0]
    led_index = int(tag_str[3]) - 1
    toggle_led_state(led_index)
def toggle_led_state(led_index):
    estado_leds[led_index] = 1 - estado_leds[led_index]
    if estado_leds[led_index] == 1:
        puerto.write(f"{chr(led_index + 48)}\n".encode())
    else:
        puerto.write(f"{chr(led_index + 97)}\n".encode())
    draw()
def update_from_arduino():
    global estado_botones
    while puerto.in_waiting:
        data = puerto.readline().strip().decode()
        if data in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            group = ord(data) - ord('A') if data in ['A', 'B', 'C', 'D'] else ord(data) - ord('E')
            estado_botones[group] = 1 if data in ['A', 'B', 'C', 'D'] else 0
            group_leds = [group * 2, group * 2 + 1]
            for led in group_leds:
                estado_leds[led] = estado_botones[group]
                puerto.write(f"{data}\n".encode())
            draw()
        elif ',' in data:
            pin, estado = map(int, data.split(','))
            estado_leds[pin] = estado
            draw()
    root.after(10, update_from_arduino)


root = Tk()
width = 1250
height = 500
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
setup_serial()
draw()
for i in range(3):
    canvas.tag_bind(f"btn{i + 1}", "<Button-1>", toggle_group)
for i in range(6):
    canvas.tag_bind(f"led{i + 1}", "<Button-1>", toggle_led)
root.after(10, update_from_arduino)
root.mainloop()
puerto.close()