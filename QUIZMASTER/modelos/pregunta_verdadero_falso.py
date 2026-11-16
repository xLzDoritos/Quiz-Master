from modelos.pregunta import Pregunta


class PreguntaVerdaderoFalso(Pregunta):
    def __init__(self, enunciado, respuesta_correcta, puntos=10):
        if not isinstance(respuesta_correcta, bool):
            raise ValueError("La respuesta correcta debe ser True o False.")

        super().__init__(enunciado, respuesta_correcta, puntos)

    def obtener_opciones(self):
        return ("Verdadero", "Falso")

    def verificar_respuesta(self, respuesta):
        if isinstance(respuesta, bool):
            respuesta_usuario = respuesta
        else:
            texto = str(respuesta).strip().casefold()
            if texto not in ("verdadero", "falso"):
                return False
            respuesta_usuario = texto == "verdadero"

        return respuesta_usuario == self._respuesta_correcta
