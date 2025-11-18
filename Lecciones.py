import customtkinter as ctk
from PIL import Image
import string
import os
import Reproductor  # Asegúrate de tener la función reproducir() en este módulo
import MostrarLogo

def lessonSelector(pestanas, datos):
    if "Lecciones" in pestanas._tab_dict:
        pestanas.delete("Lecciones")
    pestanas.add("Lecciones")
    frame = pestanas.tab("Lecciones")

    usuario = datos["usuario"]
    xp= datos["xp"]
    MostrarLogo.Logo(frame, datos)

    
    ctk.CTkLabel(frame, text="¡Selecciona tu lección!", font=("Segoe UI", 35, "bold")).place(relx=.5, rely=.19, anchor="center")
    img1 = Image.open("assets/abecedarioN.png")
    img_ctk1 = ctk.CTkImage(light_image=img1, size=(200, 200))
    ctk.CTkLabel(frame, image=img_ctk1, text="").place(relx=.2, rely=.6, anchor="center")
    ctk.CTkButton(frame, text="Seleccionar", command=lambda: lesson1(pestanas, datos)).place(relx=.2, rely=.85, anchor="center")

    img2 = Image.open("assets/palabrasComunesN.png")
    img_ctk2 = ctk.CTkImage(light_image=img2, size=(200, 200))
    ctk.CTkLabel(frame, image=img_ctk2, text="").place(relx=.5, rely=.6, anchor="center")
    ctk.CTkButton(frame, text="Seleccionar", command=lambda: lesson2(pestanas, datos)).place(relx=.5, rely=.85, anchor="center")

    img3 = Image.open("assets/frasesN.png")
    img_ctk3 = ctk.CTkImage(light_image=img3, size=(200, 200))
    ctk.CTkLabel(frame, image=img_ctk3, text="").place(relx=.8, rely=.6, anchor="center")
    ctk.CTkButton(frame, text="Seleccionar").place(relx=.8, rely=.85, anchor="center")


def lesson1(pestanas, datos):
    if "Lección 1" in pestanas._tab_dict:
        pestanas.delete("Lección 1")
    if "Nivel 1" in pestanas._tab_dict:
        pestanas.delete("Nivel 1")
    pestanas.add("Lección 1")
    pestanas.set("Lección 1")
    frame = pestanas.tab("Lección 1")

    mostrar_letra(frame, "A", datos)


def mostrar_letra(frame, letra_actual, datos):
    for widget in frame.winfo_children():
        widget.destroy()

    abecedario = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    indice = abecedario.index(letra_actual)

    MostrarLogo.Logo(frame, datos)
    
    
    
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
        ctk.CTkButton(frame, text="←  Anterior", command=lambda: mostrar_letra(frame, letra_anterior, datos)).place(relx=0.3, rely=0.9, anchor="center")

    if indice < len(abecedario) - 1:
        letra_siguiente = abecedario[indice + 1]
        ctk.CTkButton(frame, text="Siguiente  →", command=lambda: mostrar_letra(frame, letra_siguiente, datos)).place(relx=0.7, rely=0.9, anchor="center")
    
def lesson2(pestanas, datos):
    if "Lección 2" in pestanas._tab_dict:
        pestanas.delete("Lección 2")
    if "Nivel 2" in pestanas._tab_dict:
        pestanas.delete("Nivel 2")
    pestanas.add("Lección 2")
    pestanas.set("Lección 2")
    frame = pestanas.tab("Lección 2")
    MostrarFrase(frame, "Hola", datos)

def MostrarFrase(frame, fraseAct, datos):
    for widget in frame.winfo_children():
        widget.destroy()
    listaFrases = ["Hola", "ComoEstas", "Bien", "Mal", "Gracias", "MiNombreEs"]
    indice = listaFrases.index(fraseAct)
    
    MostrarLogo.Logo(frame, datos)
    
    ctk.CTkLabel(frame, text="Frases de interacción", font=("Segoe UI", 30, "bold")).place(relx=0.5, rely=0.05, anchor="center")
    ctk.CTkLabel(frame, text=f"'{fraseAct}'", font=("Segoe UI", 25)).place(relx=0.5, rely=0.18, anchor="center")
    ruta_video = f"assets/{fraseAct}.mp4"
    if os.path.exists(ruta_video):
        Reproductor.reproducir(frame, ruta_video)
    else:
        ctk.CTkLabel(frame, text="(Video no disponible)", font=("Segoe UI", 16, "italic")).place(relx=0.5, rely=0.4, anchor="center")

    ctk.CTkLabel(frame, text="¡Es tu turno!", font=("Segoe UI", 15, "bold")).place(relx=0.5, rely=0.82, anchor="center")
    
    if indice > 0:
        letra_anterior = listaFrases[indice - 1]
        ctk.CTkButton(frame, text="←  Anterior", command=lambda: MostrarFrase(frame, letra_anterior, datos)).place(relx=0.3, rely=0.9, anchor="center")

    if indice < len(listaFrases) - 1:
        letra_siguiente = listaFrases[indice + 1]
        ctk.CTkButton(frame, text="Siguiente  →", command=lambda: MostrarFrase(frame, letra_siguiente, datos)).place(relx=0.7, rely=0.9, anchor="center")