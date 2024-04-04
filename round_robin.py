def round_robin(procesos,quantum):
    tiempo_actual=0
    while procesos:
        for proceso in procesos[:]:
            proceso["tiempo_ejecucion_original"]=proceso["tiempo_ejecucion"]
            if proceso["tiempo_ejecucion"] > 0:
                if proceso["tiempo_ejecucion"] > quantum:
                    tiempo_actual+=quantum
                    proceso["tiempo_ejecucion"]-=quantum
                else:
                    tiempo_actual+=proceso["tiempo_ejecucion"]
                    proceso["tiempo_espera"] = tiempo_actual-proceso["tiempo_llegada"]-proceso["tiempo_ejecucion_original"]
                    proceso["tiempo_ejecucion"] = 0
                    procesos.remove(proceso)
    return procesos

procesos = [
    {"nombre":"Proceso A","tiempo_llegada":0,"tiempo_ejecucion":8},
    {"nombre":"Proceso B","tiempo_llegada":1,"tiempo_ejecucion":4},
    {"nombre":"Proceso C","tiempo_llegada":2,"tiempo_ejecucion":5},
]

quantum=3

round_robin(procesos,quantum)
#for proceso in resultado_rr:
#    print(f"{proceso['nombre']}:Tiempo de espera = {proceso['tiempo_espera']}")


                