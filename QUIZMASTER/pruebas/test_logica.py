import unittest
from servicios.gestor_preguntas import GestorPreguntas


class PruebasLogicaQuiz(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorPreguntas()

    def test_carga_cuatro_categorias(self):
        self.assertEqual(len(self.gestor.categorias), 4)

    def test_cada_categoria_tiene_diez_preguntas(self):
        for categoria in self.gestor.categorias:
            self.assertEqual(categoria.cantidad_preguntas(), 10)

    def test_respuesta_correcta_suma_puntos(self):
        partida = self.gestor.iniciar_partida("Tecnología", 10)
        pregunta = partida.obtener_pregunta_actual()
        respuesta = pregunta._respuesta_correcta
        self.assertTrue(partida.responder(respuesta))
        self.assertEqual(partida.puntuacion, 10)

    def test_categoria_inexistente_muestra_error(self):
        with self.assertRaises(ValueError):
            self.gestor.iniciar_partida("Historia")

    def test_no_permite_responder_despues_de_terminar(self):
        partida = self.gestor.iniciar_partida("Ciencia", 1)
        pregunta = partida.obtener_pregunta_actual()
        partida.responder(pregunta._respuesta_correcta)
        with self.assertRaises(RuntimeError):
            partida.responder("otra respuesta")


if __name__ == "__main__":
    unittest.main()
