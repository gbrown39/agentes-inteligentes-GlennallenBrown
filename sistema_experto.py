class SistemaExperto:
    def __init__(self):
        self.reglas = {
            "fiebre": "Posible gripe o infección.",
            "tos": "Posible resfriado o alergia.",
            "dolor de cabeza": "Posible migraña o tensión.",
            "dolor de garganta": "Posible faringitis.",
            "fatiga": "Posible anemia o estrés."
        }

    def diagnosticar(self):
        print("Ingresa tus síntomas (separados por comas):")
        sintomas = input().split(",")

        diagnostico = []
        for sintoma in sintomas:
            sintoma = sintoma.strip().lower()
            if sintoma in self.reglas:
                diagnostico.append(self.reglas[sintoma])

        if diagnostico:
            print("\nDiagnóstico:")
            for resultado in diagnostico:
                print(f"- {resultado}")
        else:
            print("No se pudo determinar un diagnóstico con los síntomas ingresados.")

# Ejecutar el sistema experto
experto = SistemaExperto()
experto.diagnosticar()