import random
import time

class AgenteBuscador:
    def __init__(self):
        self.fila_agente = 0
        self.columna_agente = 0
        self.fila_objeto = random.randint(0, 4)
        self.columna_objeto = random.randint(0, 4)

    def mostrar_cuadricula(self):
        for fila in range(5):
            for columna in range(5):
                if fila == self.fila_agente and columna == self.columna_agente:
                    print("A", end=" ")  # Posición del agente
                elif fila == self.fila_objeto and columna == self.columna_objeto:
                    print("O", end=" ")  # Posición del objeto
                else:
                    print(".", end=" ")  # Espacio vacío
            print()

    def mover_agente(self):
        while (self.fila_agente != self.fila_objeto) or (self.columna_agente != self.columna_objeto):
            if self.fila_agente < self.fila_objeto:
                self.fila_agente += 1
            elif self.fila_agente > self.fila_objeto:
                self.fila_agente -= 1

            if self.columna_agente < self.columna_objeto:
                self.columna_agente += 1
            elif self.columna_agente > self.columna_objeto:
                self.columna_agente -= 1

            print("\nMovimiento del agente:")
            self.mostrar_cuadricula()
            time.sleep(1)

        print("\n¡Objeto encontrado!")

# Ejecutar el agente
buscador = AgenteBuscador()
print("Posición inicial:")
buscador.mostrar_cuadricula()
buscador.mover_agente()