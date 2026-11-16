class Categoria:
    def __init__(self, nombre, descripcion=""):
        if not nombre or not nombre.strip():
            raise ValueError("La categoría debe tener un nombre.")

        self._nombre = nombre.strip()
        self._descripcion = descripcion.strip()
        self._preguntas = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def preguntas(self):
        return tuple(self._preguntas)

    def agregar_pregunta(self, pregunta):
        if not hasattr(pregunta, "verificar_respuesta"):
            raise TypeError("El elemento agregado no es una pregunta válida.")
        self._preguntas.append(pregunta)

    def cantidad_preguntas(self):
        return len(self._preguntas)
