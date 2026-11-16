# QUIZ MASTER

## 1. Nombre del proyecto

**QUIZ MASTER – Aplicación de preguntas y respuestas**

QUIZ MASTER es una aplicación de escritorio desarrollada en Python que permite a los usuarios poner a prueba sus conocimientos mediante preguntas organizadas por categorías. Cuenta con una interfaz gráfica que facilita la interacción con el juego.

## 2. Descripción del problema

En ocasiones, las personas buscan una manera sencilla e interactiva de practicar sus conocimientos sobre diferentes temas. Sin embargo, no siempre cuentan con una herramienta que les permita responder preguntas, comprobar sus respuestas y conocer sus resultados.

Por esta razón, se desarrolló QUIZ MASTER, una aplicación que organiza preguntas por categorías y permite realizar partidas de manera fácil y entretenida.

## 3. Objetivos

### Objetivo general

Desarrollar una aplicación de preguntas y respuestas utilizando Python y programación orientada a objetos, que permita al usuario responder preguntas y obtener una puntuación según sus resultados.

### Objetivos específicos

- Organizar preguntas en diferentes categorías.
- Implementar diferentes tipos de preguntas.
- Validar las respuestas seleccionadas por el usuario.
- Calcular la puntuación obtenida durante una partida.
- Desarrollar una interfaz gráfica sencilla.
- Aplicar los conceptos de programación orientada a objetos.

## 4. Funcionalidades

La aplicación cuenta con las siguientes funcionalidades:

- Presentación de una interfaz gráfica.
- Organización de preguntas por categorías: Tecnología, Ciencia, Cultura general y Deportes.
- Preguntas de selección múltiple y verdadero o falso.
- Selección de preguntas para iniciar una partida.
- Validación de las respuestas.
- Asignación de 10 puntos por cada respuesta correcta.
- Visualización de los resultados.
- Posibilidad de iniciar una nueva partida.

## 5. Tecnologías utilizadas

| Tecnología | Utilización |
|---|---|
| Python | Lenguaje principal de programación |
| Tkinter | Desarrollo de la interfaz gráfica |
| Visual Studio Code | Editor de código |
| Git | Control de versiones |
| GitHub | Almacenamiento y entrega del proyecto |

## 6. Instalación

### Requisitos

- Tener Python instalado.
- Contar con Visual Studio Code u otro editor compatible.
- Descargar o clonar el repositorio del proyecto.

**Versión de Python:** verificar la versión utilizada durante el desarrollo antes de publicar el repositorio.

### Dependencias

La aplicación utiliza Tkinter, que normalmente viene incluido con las instalaciones de Python para Windows.

No se requieren bibliotecas externas adicionales en la versión básica del proyecto.

## 7. Ejecución

Para iniciar la aplicación:

1. Abrir la carpeta `QUIZ-MASTER` en Visual Studio Code.
2. Abrir una terminal en la carpeta principal.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

La aplicación abrirá la ventana gráfica de QUIZ MASTER.

## 8. Manual de usuario

### Inicio de la aplicación

El usuario ejecuta el programa y aparece la ventana principal de QUIZ MASTER.

**Captura 1: Pantalla inicial**

> Insertar aquí una captura real de la ventana principal.

### Desarrollo de una partida

El usuario utiliza las opciones disponibles en la interfaz para comenzar una partida y responder las preguntas.

**Captura 2: Pantalla de preguntas**

> Insertar aquí una captura real donde se vea una pregunta y sus opciones.

### Responder preguntas

El usuario selecciona una opción y la aplicación comprueba si la respuesta es correcta o incorrecta.

**Captura 3: Validación de respuesta**

> Insertar aquí una captura real del mensaje que aparece después de responder.

### Resultados

Al finalizar la partida, el programa presenta el resultado obtenido por el usuario.

**Captura 4: Resultado final**

> Insertar aquí una captura real de la pantalla de resultados.

## 9. Estructura del proyecto

```text
QUIZ-MASTER/
│
├── main.py
├── README.md
│
├── interfaz/
│   ├── __init__.py
│   └── ventana_principal.py
│
├── modelos/
│   ├── __init__.py
│   ├── pregunta.py
│   ├── pregunta_multiple.py
│   ├── pregunta_verdadero_falso.py
│   ├── categoria.py
│   └── partida.py
│
├── servicios/
│   ├── __init__.py
│   └── gestor_preguntas.py
│
├── pruebas/
│   ├── __init__.py
│   └── test_logica.py
│
└── docs/
    ├── INFORME_TECNICO.md
    ├── DIAGRAMA_DE_CLASES.md
    └── imagenes/
```

### Descripción de las carpetas

- **interfaz:** contiene los archivos encargados de mostrar la ventana gráfica.
- **modelos:** contiene las clases que representan las preguntas, categorías y partidas.
- **servicios:** contiene la administración de las preguntas y categorías.
- **pruebas:** contiene las pruebas automáticas del programa.
- **docs:** almacena los documentos técnicos y las evidencias del proyecto.

## 10. Autor

**Estudiante:** David

**Proyecto académico:** QUIZ MASTER

**Programa académico:** Técnico Profesional en Programación de Computadores.