from openai import OpenAI

client = OpenAI(api_key = "")

# Define funcion para interactuar con ChatGPT
def enviar_pregunta(pregunta):
    # Llamar a la API de OpenAI para obtener una respuesta a la pregunta
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        #prompt=prompt,
        messages=[
            {
                "role":"user",
                "content":pregunta
            }
        ],
        max_tokens=500
    )
    return respuesta.choices[0].message.content

    

#Clase para representar procesos
class Proceso:
    def __init__(self,id,nombre,estado):
        self.id = id
        self.nombre = nombre
        self.estado = estado

# Funciones para siular el sistea operativo
def asignar_recursos(proceso:Proceso):
    # Simular asignacion de recursos
    proceso.estado = "Listo"

def ejecutar_proceso(proceso:Proceso):
    #Simular ejecucion de proceso
    proceso.estado = "Ejecutando"
    # Preguntar a ChatGPT como proceder
    respuesta = enviar_pregunta(f"Esta es una simulacion del proceso {proceso.nombre} y necesita asignarle mas memoria")
    print(f"Respuesta de ChatGPT: {respuesta}")
    # Actualizar estado del proceso segun la respuesta
    proceso.estado = respuesta

# Ejemplo de uso
if __name__=="__main__":
    proceso1 = Proceso(1,"ProcesoA","Nuevo")
    asignar_recursos(proceso1)
    ejecutar_proceso(proceso1)