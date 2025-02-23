import random

class AgenteRecomendacion:
    def __init__(self):
        self.peliculas = {
            "acción": ["Misión Imposible", "John Wick", "Mad Max"],
            "comedia": ["Supercool", "Los Bridgerton", "Deadpool"],
            "drama": ["Forrest Gump", "El Padrino", "Titanic"],
            "ciencia ficción": ["Interestelar", "Matrix", "Blade Runner"]
        }

    def recomendar(self):
        print("Géneros disponibles: acción, comedia, drama, ciencia ficción")
        genero = input("Ingresa tu género favorito: ").strip().lower()

        if genero in self.peliculas:
            recomendacion = random.choice(self.peliculas[genero])
            print(f"Te recomiendo la película: {recomendacion}")
        else:
            print("Género no válido.")

# Ejecutar el agente
recomendador = AgenteRecomendacion()
recomendador.recomendar()