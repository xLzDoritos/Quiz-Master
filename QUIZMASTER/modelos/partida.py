import random


class Partida:
    def __init__(self, categoria, cantidad_preguntas=10):
        if categoria.cantidad_preguntas() == 0:
            raise ValueError("Esta categoría no tiene preguntas.")
        if cantidad_preguntas <= 0:
            raise ValueError("La cantidad de preguntas debe ser mayor que cero.")

        self._categoria = categoria
        self._preguntas = random.sample(
            list(categoria.preguntas),
            min(cantidad_preguntas, categoria.cantidad_preguntas())
        )
        self._indice_actual = 0
        self._puntuacion = 0
        self._respuestas_correctas = 0
        self._respuestas_incorrectas = 0
        self._terminada = False
        self._historial = []

    @property
    def categoria(self):
        return self._categoria

    @property
    def puntuacion(self):
        return self._puntuacion

    @property
    def respuestas_correctas(self):
        return self._respuestas_correctas

    @property
    def respuestas_incorrectas(self):
        return self._respuestas_incorrectas

    @property
    def terminada(self):
        return self._terminada

    @property
    def total_preguntas(self):
        return len(self._preguntas)

    @property
    def numero_pregunta(self):
        return min(self._indice_actual + 1, self.total_preguntas)

    def obtener_pregunta_actual(self):
        if self._terminada:
            return None
        return self._preguntas[self._indice_actual]

    def responder(self, respuesta):
        if self._terminada:
            raise RuntimeError("La partida ya terminó.")

        pregunta = self.obtener_pregunta_actual()
        es_correcta = pregunta.verificar_respuesta(respuesta)

        if es_correcta:
            self._puntuacion += pregunta.puntos
            self._respuestas_correctas += 1
        else:
            self._respuestas_incorrectas += 1

        self._historial.append({
            "pregunta": pregunta.enunciado,
            "respuesta": respuesta,
            "correcta": es_correcta
        })

        self._indice_actual += 1
        if self._indice_actual >= self.total_preguntas:
            self._terminada = True

        return es_correcta

    def obtener_resultado(self):
        if not self._terminada:
            raise RuntimeError("El resultado estará disponible al terminar.")

        porcentaje = (
            self._respuestas_correctas / self.total_preguntas
        ) * 100

        return {
            "categoria": self._categoria.nombre,
            "total_preguntas": self.total_preguntas,
            "respuestas_correctas": self._respuestas_correctas,
            "respuestas_incorrectas": self._respuestas_incorrectas,
            "puntuacion": self._puntuacion,
            "porcentaje": round(porcentaje, 1),
            "historial": tuple(self._historial)
        }
