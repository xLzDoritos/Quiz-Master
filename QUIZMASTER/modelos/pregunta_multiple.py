from modelos.pregunta import Pregunta


class PreguntaMultiple(Pregunta):
    def __init__(self, enunciado, opciones, respuesta_correcta, puntos=10):
        if len(opciones) < 2:
            raise ValueError("Una pregunta debe tener al menos dos opciones.")
        if respuesta_correcta not in opciones:
            raise ValueError("La respuesta correcta debe estar entre las opciones.")

        self._opciones = tuple(opciones)
        super().__init__(enunciado, respuesta_correcta, puntos)

    def obtener_opciones(self):
        return self._opciones

    def verificar_respuesta(self, respuesta):
        return str(respuesta).strip().casefold() == str(
            self._respuesta_correcta
        ).strip().casefold()
