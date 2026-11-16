
# Diagrama de clases 

El siguiente diagrama representa las principales clases del proyecto y sus relaciones.

```mermaid
classDiagram
    class Pregunta {
        <<abstract>>
        +enunciado
        +obtener_opciones()
        +verificar_respuesta()
    }

    class PreguntaMultiple {
        +opciones
        +respuesta_correcta
        +obtener_opciones()
        +verificar_respuesta()
    }

    class PreguntaVerdaderoFalso {
        +respuesta_correcta
        +obtener_opciones()
        +verificar_respuesta()
    }

    class Categoria {
        +nombre
        +preguntas
        +cantidad_preguntas()
    }

    class Partida {
        +puntaje
        +terminada
        +responder()
        +obtener_resultado()
    }

    class GestorPreguntas {
        +categorias
        +iniciar_partida()
    }

    Pregunta <|-- PreguntaMultiple
    Pregunta <|-- PreguntaVerdaderoFalso
    Categoria o-- Pregunta
    Partida o-- Pregunta
    GestorPreguntas o-- Categoria
```

## Explicación

- Pregunta: clase base de los tipos de preguntas.
- PreguntaMultiple: representa preguntas de selección múltiple.
- PreguntaVerdaderoFalso: representa preguntas de verdadero o falso.
- Categoria: organiza las preguntas por temas.
- Partida: controla el desarrollo y los resultados de una partida.
- GestorPreguntas: administra las categorías y preguntas.

**Nota:** verificar los atributos, métodos y relaciones con el código definitivo antes de entregar.
