# QUIZ MASTER — Etapa 2: interfaz gráfica

Se agregó una interfaz de escritorio con Tkinter.

## Funcionalidades visibles
1. Pantalla de bienvenida.
2. Selección de categoría.
3. Partida con preguntas aleatorias y opciones seleccionables.
4. Comprobación de respuesta y retroalimentación.
5. Pantalla final con puntos, aciertos, errores y porcentaje.
6. Opción para volver a jugar.

## Ejecutar
Desde la carpeta principal:

```bash
python main.py
```

Tkinter normalmente viene incluido con Python. No se requieren paquetes externos.

La lógica del juego continúa separada de la interfaz. La ventana utiliza `GestorPreguntas` y `Partida`; no calcula las puntuaciones por su cuenta.
