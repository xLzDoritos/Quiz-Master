import tkinter as tk
from tkinter import ttk, messagebox
from servicios.gestor_preguntas import GestorPreguntas


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("QUIZ MASTER")
        self.root.geometry("850x620")
        self.root.minsize(700, 540)
        self.root.configure(bg="#101827")
        self.gestor = GestorPreguntas()
        self.partida = None
        self.respuesta_seleccionada = tk.StringVar()
        self._configurar_estilos()
        self.mostrar_inicio()

    def _configurar_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Quiz.TRadiobutton", background="#1e293b",
                         foreground="#f8fafc", font=("Segoe UI", 12), padding=10)
        estilo.map("Quiz.TRadiobutton", background=[("active", "#334155")],
                   foreground=[("active", "#ffffff")])

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def crear_contenedor(self):
        self.limpiar_ventana()
        marco = tk.Frame(self.root, bg="#101827")
        marco.pack(fill="both", expand=True, padx=35, pady=30)
        return marco

    def crear_titulo(self, marco, texto, tamano=28):
        tk.Label(marco, text=texto, bg="#101827", fg="#38bdf8",
                 font=("Segoe UI", tamano, "bold")).pack(pady=(15, 10))

    def crear_boton(self, marco, texto, comando, color="#2563eb"):
        return tk.Button(marco, text=texto, command=comando, bg=color,
                         fg="white", activebackground="#1d4ed8",
                         activeforeground="white", font=("Segoe UI", 12, "bold"),
                         relief="flat", cursor="hand2", padx=20, pady=10)

    def mostrar_inicio(self):
        marco = self.crear_contenedor()
        self.crear_titulo(marco, "QUIZ MASTER", 34)
        tk.Label(marco, text="Pon a prueba tus conocimientos", bg="#101827",
                 fg="#cbd5e1", font=("Segoe UI", 16)).pack(pady=8)
        tk.Label(marco, text="Elige una categoría, responde las preguntas y consigue la mayor puntuación.",
                 bg="#101827", fg="#94a3b8", font=("Segoe UI", 11),
                 wraplength=600).pack(pady=12)
        self.crear_boton(marco, "COMENZAR", self.mostrar_categorias).pack(pady=25)
        tk.Label(marco, text="4 categorías  •  40 preguntas  •  10 puntos por acierto",
                 bg="#101827", fg="#64748b", font=("Segoe UI", 10)).pack(side="bottom", pady=10)

    def mostrar_categorias(self):
        marco = self.crear_contenedor()
        self.crear_titulo(marco, "Selecciona una categoría")
        tk.Label(marco, text="Cada partida tendrá hasta 10 preguntas aleatorias.",
                 bg="#101827", fg="#cbd5e1", font=("Segoe UI", 12)).pack(pady=10)
        nombres = [categoria.nombre for categoria in self.gestor.categorias]
        self.categoria_seleccionada = tk.StringVar(value=nombres[0])
        ttk.Combobox(marco, textvariable=self.categoria_seleccionada,
                     values=nombres, state="readonly", font=("Segoe UI", 13),
                     width=28).pack(pady=20, ipady=6)
        self.crear_boton(marco, "INICIAR PARTIDA", self.iniciar_partida).pack(pady=12)
        self.crear_boton(marco, "VOLVER", self.mostrar_inicio, "#475569").pack(pady=5)

    def iniciar_partida(self):
        try:
            self.partida = self.gestor.iniciar_partida(self.categoria_seleccionada.get(), 10)
            self.mostrar_pregunta()
        except (ValueError, RuntimeError) as error:
            messagebox.showerror("No se pudo iniciar", str(error))

    def mostrar_pregunta(self):
        pregunta = self.partida.obtener_pregunta_actual()
        if pregunta is None:
            self.mostrar_resultados()
            return
        marco = self.crear_contenedor()
        tk.Label(marco, text=f"CATEGORÍA: {self.partida.categoria.nombre.upper()}",
                 bg="#101827", fg="#38bdf8", font=("Segoe UI", 11, "bold")).pack(pady=(5, 8))
        tk.Label(marco, text=f"Pregunta {self.partida.numero_pregunta} de {self.partida.total_preguntas}",
                 bg="#101827", fg="#cbd5e1", font=("Segoe UI", 12)).pack(pady=5)
        tk.Label(marco, text=pregunta.enunciado, bg="#1e293b", fg="#f8fafc",
                 font=("Segoe UI", 16, "bold"), wraplength=680, justify="center",
                 padx=25, pady=25).pack(fill="x", pady=20)
        self.respuesta_seleccionada = tk.StringVar(value="")
        opciones = tk.Frame(marco, bg="#101827")
        opciones.pack(fill="x", padx=40, pady=5)
        for opcion in pregunta.obtener_opciones():
            ttk.Radiobutton(opciones, text=opcion, value=opcion,
                            variable=self.respuesta_seleccionada,
                            style="Quiz.TRadiobutton").pack(fill="x", pady=4)
        self.etiqueta_mensaje = tk.Label(marco, text="", bg="#101827",
                                         fg="#facc15", font=("Segoe UI", 11, "bold"))
        self.etiqueta_mensaje.pack(pady=10)
        botones = tk.Frame(marco, bg="#101827")
        botones.pack(pady=8)
        self.boton_responder = self.crear_boton(botones, "COMPROBAR RESPUESTA", self.comprobar_respuesta)
        self.boton_responder.pack(side="left", padx=6)
        self.boton_siguiente = self.crear_boton(botones, "SIGUIENTE", self.siguiente_pregunta, "#0f766e")
        self.boton_siguiente.pack(side="left", padx=6)
        self.boton_siguiente.config(state="disabled")
        tk.Label(marco, text=f"Puntuación actual: {self.partida.puntuacion} puntos",
                 bg="#101827", fg="#94a3b8", font=("Segoe UI", 10)).pack(side="bottom", pady=5)

    def comprobar_respuesta(self):
        respuesta = self.respuesta_seleccionada.get()
        if not respuesta:
            messagebox.showwarning("Falta tu respuesta", "Selecciona una opción antes de continuar.")
            return
        try:
            correcta = self.partida.responder(respuesta)
            if correcta:
                self.etiqueta_mensaje.config(text="¡Respuesta correcta! +10 puntos", fg="#4ade80")
            else:
                self.etiqueta_mensaje.config(text="Respuesta incorrecta. ¡Sigue intentando!", fg="#fb7185")
            self.boton_responder.config(state="disabled")
            self.boton_siguiente.config(state="normal")
        except (ValueError, RuntimeError) as error:
            messagebox.showerror("Error", str(error))

    def siguiente_pregunta(self):
        if self.partida.terminada:
            self.mostrar_resultados()
        else:
            self.mostrar_pregunta()

    def mostrar_resultados(self):
        resultado = self.partida.obtener_resultado()
        marco = self.crear_contenedor()
        self.crear_titulo(marco, "¡Partida terminada!", 30)
        tk.Label(marco, text=resultado["categoria"], bg="#101827", fg="#cbd5e1",
                 font=("Segoe UI", 14)).pack(pady=5)
        tk.Label(marco, text=f'{resultado["puntuacion"]} PUNTOS', bg="#101827",
                 fg="#4ade80", font=("Segoe UI", 30, "bold")).pack(pady=15)
        resumen = (f'Preguntas: {resultado["total_preguntas"]}\n'
                   f'Respuestas correctas: {resultado["respuestas_correctas"]}\n'
                   f'Respuestas incorrectas: {resultado["respuestas_incorrectas"]}\n'
                   f'Porcentaje de aciertos: {resultado["porcentaje"]}%')
        tk.Label(marco, text=resumen, bg="#1e293b", fg="#f8fafc",
                 font=("Segoe UI", 14), justify="center", padx=35, pady=25).pack(pady=12)
        botones = tk.Frame(marco, bg="#101827")
        botones.pack(pady=15)
        self.crear_boton(botones, "JUGAR OTRA VEZ", self.mostrar_categorias).pack(side="left", padx=6)
        self.crear_boton(botones, "SALIR", self.root.destroy, "#475569").pack(side="left", padx=6)


def iniciar_aplicacion():
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    iniciar_aplicacion()
