from abc import ABC, abstractmethod


class Pregunta(ABC):
    def __init__(self, enunciado, respuesta_correcta, puntos=10):
        if not enunciado or not enunciado.strip():
            raise ValueError("El enunciado no puede estar vacío.")
        if puntos <= 0:
            raise ValueError("Los puntos deben ser mayores que cero.")

        self._enunciado = enunciado.strip()
        self._respuesta_correcta = respuesta_correcta
        self._puntos = puntos

    @property
    def enunciado(self):
        return self._enunciado

    @property
    def puntos(self):
        return self._puntos

    @abstractmethod
    def obtener_opciones(self):
        pass

    @abstractmethod
    def verificar_respuesta(self, respuesta):
        pass
