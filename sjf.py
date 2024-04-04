def sjf(procesos):
    procesos_ordenados=sorted(procesos,key=lambda x: x["tiempo_ejecucion"])
    tiempo_total=0
    for proceso in procesos_ordenados:
        tiempo_total+=proceso["tiempo_ejecucion"]
        proceso["tiempo_espera"]=tiempo_total-proceso["tiempo_llegada"]-proceso["tiempo_ejecucion"]
    return procesos_ordenados

procesos = [
    {"nombre":"Proceso A","tiempo_llegada":0,"tiempo_ejecucion":3},
    {"nombre":"Proceso B","tiempo_llegada":1,"tiempo_ejecucion":5},
    {"nombre":"Proceso C","tiempo_llegada":2,"tiempo_ejecucion":2},
]

resultado_rr=sjf(procesos)
for proceso in resultado_rr:
    print(f"{proceso['nombre']}:Tiempo de espera = {proceso['tiempo_espera']}")