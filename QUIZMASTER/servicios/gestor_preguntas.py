from modelos.categoria import Categoria
from modelos.pregunta_multiple import PreguntaMultiple
from modelos.pregunta_verdadero_falso import PreguntaVerdaderoFalso
from modelos.partida import Partida


class GestorPreguntas:
    def __init__(self):
        self._categorias = {}
        self._cargar_preguntas_iniciales()

    @property
    def categorias(self):
        return tuple(self._categorias.values())

    def agregar_categoria(self, categoria):
        clave = categoria.nombre.casefold()
        if clave in self._categorias:
            raise ValueError("Esa categoría ya existe.")
        self._categorias[clave] = categoria

    def obtener_categoria(self, nombre):
        if not nombre:
            raise ValueError("Debes indicar una categoría.")
        categoria = self._categorias.get(nombre.strip().casefold())
        if categoria is None:
            raise ValueError("La categoría seleccionada no existe.")
        return categoria

    def iniciar_partida(self, nombre_categoria, cantidad_preguntas=10):
        categoria = self.obtener_categoria(nombre_categoria)
        return Partida(categoria, cantidad_preguntas)

    def _cargar_preguntas_iniciales(self):
        datos = {
            "Tecnología": [
                ("¿Qué significa CPU?", ["Unidad Central de Procesamiento", "Control Personal de Usuario", "Código Principal Universal", "Unidad de Memoria"], "Unidad Central de Procesamiento"),
                ("¿Cuál de estos es un lenguaje de programación?", ["HTML", "Python", "HTTP", "Wi-Fi"], "Python"),
                ("¿Qué componente almacena datos de forma permanente?", ["RAM", "Procesador", "SSD", "Caché"], "SSD"),
                ("¿Qué significa URL?", ["Localizador Uniforme de Recursos", "Usuario Registrado Local", "Unidad de Red Lógica", "Ruta Universal Libre"], "Localizador Uniforme de Recursos"),
                ("¿Cuál es un sistema operativo?", ["Windows", "Google", "Intel", "Python"], "Windows"),
                ("¿Qué dispositivo permite mover el cursor?", ["Monitor", "Mouse", "Impresora", "Parlante"], "Mouse"),
                ("¿Qué extensión suele identificar un archivo de Python?", [".py", ".html", ".jpg", ".mp3"], ".py"),
                ("¿Qué es Internet?", ["Una red mundial de redes", "Un programa de dibujo", "Una memoria USB", "Un sistema operativo"], "Una red mundial de redes"),
                ("Python es un lenguaje de programación.", True),
                ("La memoria RAM conserva todos los datos al apagar el equipo.", False)
            ],
            "Ciencia": [
                ("¿Cuál es el planeta más cercano al Sol?", ["Venus", "Mercurio", "Marte", "Júpiter"], "Mercurio"),
                ("¿Qué gas necesitan las personas para respirar?", ["Oxígeno", "Helio", "Hidrógeno", "Nitrógeno"], "Oxígeno"),
                ("¿Cuántos huesos tiene aproximadamente un adulto?", ["106", "206", "306", "406"], "206"),
                ("¿Cuál es el órgano que bombea la sangre?", ["Pulmón", "Cerebro", "Corazón", "Hígado"], "Corazón"),
                ("¿En qué estado se encuentra el agua congelada?", ["Líquido", "Gaseoso", "Sólido", "Plasma"], "Sólido"),
                ("¿Qué estrella ilumina la Tierra?", ["Sirio", "El Sol", "La Luna", "Polaris"], "El Sol"),
                ("¿Cuál es la unidad básica de los seres vivos?", ["Átomo", "Célula", "Tejido", "Órgano"], "Célula"),
                ("¿Qué instrumento mide la temperatura?", ["Barómetro", "Termómetro", "Brújula", "Cronómetro"], "Termómetro"),
                ("La Tierra gira alrededor del Sol.", True),
                ("Los seres humanos tienen tres pulmones.", False)
            ],
            "Cultura general": [
                ("¿Cuál es la capital de Colombia?", ["Medellín", "Bogotá", "Cali", "Barranquilla"], "Bogotá"),
                ("¿En qué continente está Egipto?", ["Asia", "Europa", "África", "Oceanía"], "África"),
                ("¿Cuántos días tiene un año bisiesto?", ["364", "365", "366", "367"], "366"),
                ("¿Quién escribió Cien años de soledad?", ["Jorge Luis Borges", "Gabriel García Márquez", "Mario Vargas Llosa", "Pablo Neruda"], "Gabriel García Márquez"),
                ("¿Cuál es el océano más grande?", ["Atlántico", "Índico", "Ártico", "Pacífico"], "Pacífico"),
                ("¿Cuántos lados tiene un hexágono?", ["Cinco", "Seis", "Siete", "Ocho"], "Seis"),
                ("¿Cuál es la moneda de Japón?", ["Yuan", "Won", "Yen", "Dólar"], "Yen"),
                ("¿En qué país se encuentra la Torre Eiffel?", ["Italia", "Francia", "España", "Alemania"], "Francia"),
                ("La capital de Colombia es Bogotá.", True),
                ("El océano Pacífico es más pequeño que el Atlántico.", False)
            ],
            "Deportes": [
                ("¿Cuántos jugadores tiene un equipo de fútbol en el campo?", ["9", "10", "11", "12"], "11"),
                ("¿Cada cuántos años se celebran normalmente los Juegos Olímpicos?", ["2", "3", "4", "5"], "4"),
                ("¿En qué deporte se utiliza una raqueta?", ["Natación", "Tenis", "Fútbol", "Ciclismo"], "Tenis"),
                ("¿Cuánto dura un partido de fútbol profesional sin tiempo añadido?", ["60 minutos", "80 minutos", "90 minutos", "100 minutos"], "90 minutos"),
                ("¿Qué país es conocido por el sumo?", ["China", "Japón", "Brasil", "Canadá"], "Japón"),
                ("¿En qué deporte se encesta un balón?", ["Baloncesto", "Béisbol", "Golf", "Voleibol"], "Baloncesto"),
                ("¿Qué color tiene la tarjeta que indica expulsión en fútbol?", ["Azul", "Verde", "Amarilla", "Roja"], "Roja"),
                ("¿En qué deporte compite un ciclista?", ["Ciclismo", "Atletismo", "Boxeo", "Rugby"], "Ciclismo"),
                ("En el voleibol, cada equipo tiene seis jugadores en cancha.", True),
                ("Un maratón mide 10 kilómetros.", False)
            ]
        }

        for nombre, preguntas in datos.items():
            categoria = Categoria(nombre, "Preguntas de " + nombre.lower())
            for dato in preguntas:
                if isinstance(dato[1], list):
                    categoria.agregar_pregunta(
                        PreguntaMultiple(dato[0], dato[1], dato[2])
                    )
                else:
                    categoria.agregar_pregunta(
                        PreguntaVerdaderoFalso(dato[0], dato[1])
                    )
            self.agregar_categoria(categoria)
