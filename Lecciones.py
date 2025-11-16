import customtkinter as ctk
from PIL import Image
import string
import os
import Reproductor  # Asegúrate de tener la función reproducir() en este módulo

def lessonSelector(pestanas, datos):
    if "Lecciones" in pestanas._tab_dict:
        pestanas.delete("Lecciones")
    pestanas.add("Lecciones")
    frame = pestanas.tab("Lecciones")

    imagen_original = Image.open("assets/LOGOSF.png")
    imagen_ctk = ctk.CTkImage(light_image=imagen_original, size=(200, 200))
    ctk.CTkLabel(frame, image=imagen_ctk, text="").place(relx=0.07, rely=0.06, anchor="center")
    
    usuario = datos["usuario"]
    xp= datos["xp"]
    ctk.CTkButton(frame, text=f"XP: {xp}", fg_color="#2441D5", hover_color="#2441D5" ).place(relx=.85, rely=.04, anchor="center")

    ctk.CTkLabel(frame, text="Selecciona tu lección:", text_color="#09001D", font=("Soege UI", 30, "bold")).place(relx=.5, rely=.23, anchor="center")

    img1 = Image.open("assets/abecedarioN.png")
    img_ctk1 = ctk.CTkImage(light_image=img1, size=(200, 200))
    ctk.CTkLabel(frame, image=img_ctk1, text="").place(relx=.2, rely=.6, anchor="center")
    ctk.CTkButton(frame, text="Seleccionar", command=lambda: lesson1(pestanas)).place(relx=.2, rely=.85, anchor="center")

    img2 = Image.open("assets/palabrasComunesN.png")
    img_ctk2 = ctk.CTkImage(light_image=img2, size=(200, 200))
    ctk.CTkLabel(frame, image=img_ctk2, text="").place(relx=.5, rely=.6, anchor="center")
    ctk.CTkButton(frame, text="Seleccionar").place(relx=.5, rely=.85, anchor="center")

    img3 = Image.open("assets/frasesN.png")
    img_ctk3 = ctk.CTkImage(light_image=img3, size=(200, 200))
    ctk.CTkLabel(frame, image=img_ctk3, text="").place(relx=.8, rely=.6, anchor="center")
    ctk.CTkButton(frame, text="Seleccionar").place(relx=.8, rely=.85, anchor="center")


def lesson1(pestanas):
    if "Lección 1" in pestanas._tab_dict:
        pestanas.delete("Lección 1")
    pestanas.add("Lección 1")
    pestanas.set("Lección 1")
    frame = pestanas.tab("Lección 1")

    mostrar_letra(frame, "A")


def mostrar_letra(frame, letra_actual):
    for widget in frame.winfo_children():
        widget.destroy()

    abecedario = list(string.ascii_uppercase)
    indice = abecedario.index(letra_actual)

    imagen_original = Image.open("assets/LOGOSF.png")
    imagen_ctk = ctk.CTkImage(light_image=imagen_original, size=(200, 200))
    ctk.CTkLabel(frame, image=imagen_ctk, text="").place(relx=0.07, rely=0.06, anchor="center")
    
    ctk.CTkLabel(frame, text="¿Listo para aprender el abecedario?", font=("Segoe UI", 30, "bold")).place(relx=0.5, rely=0.05, anchor="center")
    ctk.CTkLabel(frame, text=f"Esta es la letra '{letra_actual}'", font=("Segoe UI", 25)).place(relx=0.5, rely=0.18, anchor="center")

    ruta_video = f"assets/{letra_actual}.mp4"
    if os.path.exists(ruta_video):
        Reproductor.reproducir(frame, ruta_video)
    else:
        ctk.CTkLabel(frame, text="(Video no disponible)", font=("Segoe UI", 16, "italic")).place(relx=0.5, rely=0.4, anchor="center")

    ctk.CTkLabel(frame, text="¡Es tu turno!", font=("Segoe UI", 15, "bold")).place(relx=0.5, rely=0.82, anchor="center")

    if indice > 0:
        letra_anterior = abecedario[indice - 1]
        ctk.CTkButton(frame, text="← Anterior", command=lambda: mostrar_letra(frame, letra_anterior)).place(relx=0.3, rely=0.9, anchor="center")

    if indice < len(abecedario) - 1:
        letra_siguiente = abecedario[indice + 1]
        ctk.CTkButton(frame, text="Siguiente →", command=lambda: mostrar_letra(frame, letra_siguiente)).place(relx=0.7, rely=0.9, anchor="center")
    ctk.CTkButton(frame, text="Ir al quiz").place(relx=.5, rely=.95, anchor="center")