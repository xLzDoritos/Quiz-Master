# INFORME TÉCNICO – QUIZ MASTER

## 1. Análisis del problema

### 1.1 Necesidad identificada

Se identificó la necesidad de desarrollar una aplicación sencilla que permita practicar conocimientos generales mediante preguntas interactivas.

La aplicación busca ofrecer una experiencia fácil de utilizar, en la que el usuario pueda responder preguntas, comprobar sus conocimientos y conocer su puntuación.

### 1.2 Público objetivo

La aplicación está dirigida a estudiantes y personas interesadas en practicar sus conocimientos sobre diferentes temas.

### 1.3 Funcionalidades

- Mostrar preguntas organizadas por categorías.
- Permitir responder preguntas de diferentes tipos.
- Validar las respuestas.
- Calcular los puntos obtenidos.
- Mostrar los resultados de la partida.
- Permitir jugar nuevamente.

### 1.4 Limitaciones

- La aplicación funciona como un programa de escritorio.
- Las preguntas están definidas dentro del proyecto.
- No cuenta con cuentas de usuario.
- No almacena un historial permanente de partidas.
- No requiere conexión a Internet para su funcionamiento básico.

## 2. Diseño inicial

Para desarrollar QUIZ MASTER se identificaron las principales clases necesarias para representar los elementos del juego.

| Clase | Responsabilidad |
|---|---|
| Pregunta | Definir la estructura general de una pregunta. |
| PreguntaMultiple | Representar preguntas con varias opciones. |
| PreguntaVerdaderoFalso | Representar preguntas de verdadero o falso. |
| Categoria | Organizar las preguntas por temas. |
| Partida | Administrar el desarrollo y resultado de una partida. |
| GestorPreguntas | Administrar las categorías y proporcionar preguntas. |
| VentanaPrincipal | Mostrar la interfaz gráfica y permitir la interacción del usuario. |

El diseño separa la lógica del juego de la interfaz gráfica para facilitar la organización del código.

## 3. Arquitectura

El proyecto está organizado en diferentes carpetas, cada una con una responsabilidad específica.

### 3.1 Modelos

La carpeta `modelos` contiene las clases principales del juego:

- `pregunta.py`
- `pregunta_multiple.py`
- `pregunta_verdadero_falso.py`
- `categoria.py`
- `partida.py`

Estas clases representan los elementos que intervienen en una partida.

### 3.2 Servicios

La carpeta `servicios` contiene `gestor_preguntas.py`, encargado de organizar las preguntas y categorías y proporcionar la información necesaria para iniciar una partida.

### 3.3 Interfaz

La carpeta `interfaz` contiene `ventana_principal.py`, donde se desarrolla la ventana gráfica utilizando Tkinter.

### 3.4 Pruebas

La carpeta `pruebas` contiene `test_logica.py`, utilizado para comprobar el funcionamiento de la lógica del programa.

### 3.5 Archivo principal

El archivo `main.py` inicia la aplicación y llama a la función encargada de abrir la interfaz gráfica.

## 4. Diseño y relaciones entre clases

La clase `Pregunta` funciona como estructura general para los diferentes tipos de preguntas.

Las clases `PreguntaMultiple` y `PreguntaVerdaderoFalso` especializan esa estructura.

Por otra parte, `Categoria` permite organizar preguntas y `Partida` administra el desarrollo de una ronda. `GestorPreguntas` proporciona las preguntas y categorías que utiliza el juego.

La clase `VentanaPrincipal` permite que el usuario interactúe con la aplicación gráfica.

El diagrama de clases se encuentra en el archivo `DIAGRAMA_DE_CLASES.md`.

## 5. Aplicación de programación orientada a objetos (POO)

En el desarrollo de QUIZ MASTER se aplicaron los siguientes conceptos:

| Concepto | Clase o método | Archivo | Explicación |
|---|---|---|---|
| Clases y objetos | Pregunta, Categoria y Partida | `modelos/` | Se utilizan clases para representar los elementos del juego y crear objetos durante la ejecución. |
| Encapsulamiento | Atributos y métodos de Partida | `modelos/partida.py` | La información y las operaciones relacionadas con una partida se organizan dentro de una misma clase. |
| Herencia | PreguntaMultiple y PreguntaVerdaderoFalso | `modelos/pregunta_multiple.py` y `modelos/pregunta_verdadero_falso.py` | Las dos clases especializan la clase base Pregunta. |
| Polimorfismo | `obtener_opciones()` y `verificar_respuesta()` | Archivos de los tipos de pregunta | Los distintos tipos de preguntas implementan comportamientos propios para operaciones comunes. |
| Abstracción | Pregunta | `modelos/pregunta.py` | La clase base define una estructura general y los métodos que deben implementar los tipos de pregunta. |
| Relaciones | Categoria, Pregunta y Partida | `modelos/` | Las clases colaboran para organizar preguntas y desarrollar una partida. |

### 5.1 Ejemplo de herencia

Las clases `PreguntaMultiple` y `PreguntaVerdaderoFalso` heredan de `Pregunta`.

Esto permite compartir una estructura general y adaptar el comportamiento según el tipo de pregunta.

### 5.2 Ejemplo de abstracción

La clase `Pregunta` define los comportamientos generales que deben implementar las clases derivadas.

De esta manera, no es necesario definir toda la lógica de cada tipo de pregunta en la clase base.

### 5.3 Ejemplo de polimorfismo

Los diferentes tipos de preguntas pueden utilizar métodos con el mismo nombre, como `verificar_respuesta()`, pero cada clase comprueba la respuesta de acuerdo con su propio funcionamiento.

### 5.4 Encapsulamiento

La clase `Partida` agrupa información como el puntaje y el estado de la partida, junto con los métodos que permiten administrarla.

**Nota técnica:** antes de entregar, identifica en el código los atributos y métodos concretos que implementan el control del estado. No afirmes que un atributo es privado si no está declarado como tal.

## 6. Construcción de la interfaz

### 6.1 Biblioteca seleccionada

Se utilizó Tkinter, una biblioteca de Python que permite crear interfaces gráficas de escritorio.

### 6.2 Diseño de la interfaz

La aplicación cuenta con una ventana principal desde la cual el usuario puede interactuar con el juego.

### 6.3 Controles implementados

La interfaz utiliza controles gráficos para presentar información y recibir las acciones del usuario. Según la pantalla implementada, estos pueden incluir botones, etiquetas y opciones de respuesta.

### 6.4 Eventos y callbacks

La interfaz utiliza funciones asociadas a las acciones del usuario. Por ejemplo, al pulsar un botón, la aplicación ejecuta la operación correspondiente para iniciar una partida, comprobar una respuesta o continuar el juego.

Los nombres exactos de los callbacks deben verificarse en `interfaz/ventana_principal.py`.

### 6.5 Comunicación con las clases

La interfaz utiliza el gestor de preguntas y los objetos de partida para presentar las preguntas, recibir las respuestas y mostrar los resultados.

### 6.6 Evidencias

Agregar capturas reales de las siguientes pantallas:

- Ventana principal.
- Presentación de preguntas.
- Selección de una respuesta.
- Mensaje de respuesta correcta o incorrecta.
- Resultado final.

## 7. Proceso de desarrollo

El proyecto se desarrolló siguiendo estas etapas:

1. **Formulación de la idea:** se definió una aplicación de preguntas y respuestas.
2. **Identificación de funcionalidades:** se establecieron categorías, tipos de preguntas y sistema de puntuación.
3. **Diseño de clases:** se identificaron las clases necesarias para representar la lógica del juego.
4. **Construcción de la lógica:** se desarrollaron los modelos y el gestor de preguntas.
5. **Desarrollo de la interfaz:** se creó la ventana gráfica con Tkinter.
6. **Integración:** se conectó la interfaz con la lógica del programa.
7. **Pruebas y correcciones:** se ejecutaron pruebas para verificar el funcionamiento y corregir problemas.

## 8. Pruebas

Se realizaron pruebas automáticas para verificar el funcionamiento de la lógica del programa.

Para ejecutarlas se utiliza el siguiente comando desde la carpeta principal:

```bash
python -m unittest discover -s pruebas -v
```

### Casos de prueba

| Prueba | Acción realizada | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| Prueba 1 | Consultar las categorías disponibles. | Mostrar las cuatro categorías. | Correcto. |
| Prueba 2 | Consultar las preguntas de cada categoría. | Mostrar 10 preguntas por categoría. | Correcto. |
| Prueba 3 | Responder correctamente una pregunta. | Sumar 10 puntos. | Correcto. |
| Prueba 4 | Iniciar una partida con una categoría inválida. | Generar y controlar un error de validación. | Correcto. |
| Prueba 5 | Intentar responder después de terminar la partida. | Impedir responder nuevamente. | Correcto. |

Los resultados anteriores corresponden a las pruebas de lógica que se ejecutaron durante el desarrollo. Se deben conservar únicamente si la ejecución final continúa mostrando que todas pasan.

## 9. Problemas y soluciones

### 9.1 Problema al ejecutar el programa

**Diagnóstico:** Python no encontraba el archivo `main.py` porque se estaba ejecutando desde una ubicación diferente a la que contenía el archivo principal.

**Solución:** se organizó el archivo `main.py` en la carpeta principal del proyecto y se ejecutó desde esa ubicación.

### 9.2 Problema con el inicio de la interfaz

**Diagnóstico:** el archivo principal todavía contenía el código de prueba por consola de la primera etapa y también el inicio de la interfaz gráfica.

**Solución:** se dejó `main.py` como punto de entrada de la aplicación gráfica, llamando a la función `iniciar_aplicacion()` desde `interfaz.ventana_principal`.

## 10. Conclusiones

El desarrollo de QUIZ MASTER permitió aplicar los conceptos de programación orientada a objetos mediante una aplicación funcional.

Durante el proyecto se trabajó con clases, objetos, herencia, abstracción, polimorfismo y relaciones entre clases. También se desarrolló una interfaz gráfica utilizando Tkinter y se realizaron pruebas para comprobar la lógica del juego.

La organización del proyecto en modelos, servicios, interfaz y pruebas permitió separar las responsabilidades del programa y facilitar su mantenimiento.

Como mejoras futuras se podrían agregar nuevas categorías, niveles de dificultad, almacenamiento de resultados y más opciones de personalización.

