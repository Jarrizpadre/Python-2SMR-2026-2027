
import tkinter as tk

# COLORES
BG = "#030604"
YELLOW = "#f5ed00"
PANEL = "#101410"
WHITE = "#eeeeee"
GREEN = "#39ff65"
BORDER = "#414943"

# ESTADO
municion_actual = 12
ojos_abiertos = True

# VENTANA
ventana = tk.Tk()
ventana.title("SKIPPY")
ventana.geometry("1200x800")
ventana.minsize(950, 700)
ventana.configure(bg=BG)

# ENCABEZADO
tk.Label(
    ventana,
    text="SKIPPY",
    font=("Consolas", 29, "bold"),
    fg=YELLOW, bg=BG
).pack(pady=(22, 3))

tk.Label(
    ventana,
    text="●  SISTEMA ACTIVO",
    font=("Consolas", 14, "bold"),
    fg=GREEN, bg=BG
).pack(pady=(0, 12))

# CARA DEL ROBOT
marco_cara = tk.Frame(
    ventana, bg=BORDER, padx=2, pady=2
)
marco_cara.pack(fill="x", padx=100, pady=10)

cara = tk.Canvas(
    marco_cara,
    height=240,
    bg=BG,
    highlightthickness=0
)
cara.pack(fill="both", expand=True)


def dibujar_cara():
    cara.delete("all")

    ancho = cara.winfo_width()
    if ancho < 100:
        ancho = 900

    centro = ancho / 2
    cara.create_rectangle(
        8, 8, ancho - 8, 232,
        outline="#303832", width=3
    )

    # Cejas
    cara.create_arc(
        centro - 205, 35, centro - 85, 105,
        start=25, extent=130,
        style="arc", outline=YELLOW, width=9
    )
    cara.create_arc(
        centro + 85, 35, centro + 205, 105,
        start=25, extent=130,
        style="arc", outline=YELLOW, width=9
    )

    # Ojos circulares
    for x in (centro - 130, centro + 130):
        if ojos_abiertos:
            cara.create_arc(
                x - 48, 75, x + 48, 175,
                start=35, extent=290,
                style="arc", outline=YELLOW, width=11
            )
            cara.create_oval(
                x - 28, 91, x + 28, 151,
                outline=YELLOW, width=7
            )
            cara.create_arc(
                x - 18, 99, x + 18, 143,
                start=45, extent=270,
                style="arc", outline=YELLOW, width=6
            )
        else:
            cara.create_line(
                x - 43, 125, x + 43, 125,
                fill=YELLOW, width=8
            )

    # Sonrisa
    cara.create_arc(
        centro - 48, 145, centro + 48, 195,
        start=205, extent=130,
        style="arc", outline=YELLOW, width=7
    )


def animar_ojos():
    global ojos_abiertos
    ojos_abiertos = not ojos_abiertos
    dibujar_cara()
    ventana.after(700, animar_ojos)


cara.bind("<Configure>", lambda evento: dibujar_cara())

# PANELES DE INFORMACIÓN
paneles = tk.Frame(ventana, bg=BG)
paneles.pack(fill="x", padx=65, pady=18)

def crear_panel(titulo, valor, columna):
    panel = tk.Frame(
        paneles, bg=PANEL,
        highlightbackground=YELLOW,
        highlightthickness=1
    )
    panel.grid(
        row=0, column=columna,
        padx=12, sticky="nsew"
    )

    tk.Label(
        panel, text=titulo,
        font=("Consolas", 15, "bold"),
        fg=YELLOW, bg=PANEL
    ).pack(pady=(16, 5))

    dato = tk.Label(
        panel, text=valor,
        font=("Consolas", 24, "bold"),
        fg=YELLOW, bg=PANEL
    )
    dato.pack(pady=(0, 16))

    return dato


panel_municion = crear_panel(
    "▮  MUNICIÓN", "12 / 12", 0
)
panel_velocidad = crear_panel(
    "◉  VELOCIDAD del disparo", "0 m/s", 1
)

paneles.columnconfigure(0, weight=1)
paneles.columnconfigure(1, weight=1)

# MENSAJE
mensaje = tk.Label(
    ventana,
    text="Skippy a la espera para matar.",
    font=("Consolas", 16),
    fg=WHITE, bg=BG
)
mensaje.pack(pady=12)


# FUNCIONES DE LOS BOTONES
def gastar_municion():
    global municion_actual

    if municion_actual > 0:
        municion_actual -= 1

    panel_municion.config(
        text=f"{municion_actual} / 12"
    )

    if municion_actual == 0:
        mensaje.config(text="Recarga gilipollas")
    elif municion_actual <= 3:
        mensaje.config(text="Illo te quedan pocas balas recarga o muere")
    else:
        mensaje.config(text="una bala menos una muerte más jaja.")


def recargar():
    global municion_actual
    municion_actual = 12
    panel_municion.config(text="12 / 12")
    mensaje.config(text="Reiniciando simulación.")


def saludar():
    mensaje.config(
        text="Hola Franmi. ¡Todo listos para matar!"
    )


# BOTONES
botones = tk.Frame(ventana, bg=BG)
botones.pack(fill="x", padx=55, pady=15)

def crear_boton(texto, funcion, columna, principal=False):
    fondo = YELLOW if principal else BG
    letra = BG if principal else YELLOW

    boton = tk.Button(
        botones,
        text=texto,
        command=funcion,
        font=("Consolas", 14, "bold"),
        bg=fondo,
        fg=letra,
        activebackground=YELLOW,
        activeforeground=BG,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=10,
        pady=18
    )
    boton.grid(
        row=0, column=columna,
        padx=10, sticky="nsew"
    )

    # Borde amarillo alrededor del botón
    boton.configure(
        highlightbackground=YELLOW,
        highlightcolor=YELLOW,
        highlightthickness=1
    )


crear_boton("🎙  HABLAR", saludar, 0, True)
crear_boton(
    "▮  SIMULAR CONSUMO",
    gastar_municion, 1
)
crear_boton("↻  REINICIAR", recargar, 2)

for columna in range(3):
    botones.columnconfigure(columna, weight=1)

# INICIAR
ventana.after(200, dibujar_cara)
ventana.after(700, animar_ojos)
ventana.mainloop()
