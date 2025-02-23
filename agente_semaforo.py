import time
import random

class AgenteSemaforo:
    def __init__(self):
        self.estado = "rojo"  # Estado inicial del semáforo
        self.tiempo_verde = 10  # Tiempo inicial en verde
        self.tiempo_amarillo = 3  # Tiempo en amarillo
        self.tiempo_rojo = 5  # Tiempo en rojo

    def detectar_vehiculos(self):
        # Simula la detección de vehículos (número aleatorio entre 0 y 20)
        return random.randint(0, 20)

    def ajustar_tiempo(self, vehiculos):
        # Ajusta el tiempo en verde según el número de vehículos
        if vehiculos > 15:
            self.tiempo_verde = 15
        elif vehiculos > 10:
            self.tiempo_verde = 10
        else:
            self.tiempo_verde = 5

    def cambiar_estado(self):
        while True:
            vehiculos = self.detectar_vehiculos()
            self.ajustar_tiempo(vehiculos)

            # Cambiar a verde
            self.estado = "verde"
            print(f"Semáforo en {self.estado} por {self.tiempo_verde} segundos. Vehículos detectados: {vehiculos}")
            time.sleep(self.tiempo_verde)

            # Cambiar a amarillo
            self.estado = "amarillo"
            print(f"Semáforo en {self.estado} por {self.tiempo_amarillo} segundos.")
            time.sleep(self.tiempo_amarillo)

            # Cambiar a rojo
            self.estado = "rojo"
            print(f"Semáforo en {self.estado} por {self.tiempo_rojo} segundos.")
            time.sleep(self.tiempo_rojo)

# Ejecutar el agente
semaforo = AgenteSemaforo()
semaforo.cambiar_estado()