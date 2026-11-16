# QUIZ MASTER — Etapa 1: lógica del juego

Esta etapa contiene el motor del cuestionario, todavía sin interfaz gráfica.

## Qué incluye
- 4 categorías: Tecnología, Ciencia, Cultura general y Deportes.
- 10 preguntas por categoría.
- Preguntas de selección múltiple y verdadero/falso.
- Selección aleatoria de preguntas.
- 10 puntos por respuesta correcta.
- Control de respuestas y resultados.
- Validaciones para evitar categorías inexistentes y respuestas después de terminar.

## Ejecutar una prueba manual
Desde la carpeta principal:

```bash
python main.py
```

## Ejecutar pruebas automáticas

```bash
python -m unittest discover -s pruebas -v
```

No se necesitan bibliotecas externas para esta etapa. Se utiliza Python y sus módulos incluidos.
