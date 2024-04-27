import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

# Configura tu clave de API
client = OpenAI(api_key = "")

# Historial de la conversación
conversation_history = []

# Función para enviar un mensaje al modelo y actualizar la conversación
def send_message():
    user_message = user_input.get("1.0", "end-1c")
    conversation_history.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        max_tokens=500
    )
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})
    update_chat()

# Función para actualizar el contenido de la ventana de chat
def update_chat():
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "Tu: " + conversation_history[-2]['content'] + "\n")
    chat_window.insert(tk.END, "ChatGPT: " + conversation_history[-1]['content'] + "\n")
    chat_window.config(state=tk.DISABLED)
    user_input.delete("1.0", tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("ChatGPT Assistant")

# Crear la ventana de chat
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_window.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
chat_window.config(state=tk.DISABLED)

# Entrada de texto para el usuario
user_input = tk.Text(root, wrap=tk.WORD, width=40, height=5)
user_input.grid(row=1, column=0, padx=10, pady=10)

# Botón para enviar mensaje
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Iniciar la interfaz de usuario
root.mainloop()
