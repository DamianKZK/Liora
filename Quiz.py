import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import Reproductor
import MostrarLogo
import random
import Puntuacion
import json
import os

def quiz(pestanas, datos):
    if "Quizzes" in pestanas._tab_dict:
        pestanas.delete("Quizzes")
    pestanas.add("Quizzes")
    frame = pestanas.tab("Quizzes")
    
    xp = datos["xp"]
    completado = datos["quiz1"]
    MostrarLogo.Logo(frame, datos)

    ctk.CTkLabel(frame, text="¡Pon a prueba lo aprendido!", font=("Segoe UI", 35, "bold")).place(relx=.5, rely=.19, anchor="center")
    
    img1 = Image.open("assets/Nivel1.png")
    img_ctk1 = ctk.CTkImage(light_image=img1, size=(200, 200))
    ctk.CTkLabel(frame, image=img_ctk1, text="").place(relx=.2, rely=.6, anchor="center")
    ctk.CTkButton(frame, text="Seleccionar", command=lambda:crearPestana1(pestanas, datos)).place(relx=.2, rely=.85, anchor="center")
    if completado==True:
        ctk.CTkLabel(frame, text="Quiz completado", font=("Segoe UI", 15, "bold")).place(relx=.2, rely=.37, anchor="center")
    else:
        ctk.CTkLabel(frame, text="Se recomienda completar la lección 1\nprimero", font=("Segoe UI", 15, "bold")).place(relx=.2, rely=.37, anchor="center")

    img2 = Image.open("assets/Nivel2.png")
    img_ctk2 = ctk.CTkImage(light_image=img2, size=(200, 200))
    ctk.CTkLabel(frame, image=img_ctk2, text="").place(relx=.5, rely=.6, anchor="center")
    ctk.CTkButton(frame, text="Seleccionar").place(relx=.5, rely=.85, anchor="center")

    img3 = Image.open("assets/Level3.png")
    img_ctk3 = ctk.CTkImage(light_image=img3, size=(200, 200))
    ctk.CTkLabel(frame, image=img_ctk3, text="").place(relx=.8, rely=.6, anchor="center")
    ctk.CTkButton(frame, text="Seleccionar").place(relx=.8, rely=.85, anchor="center")
    
def crearPestana1(pestanas, datos):
    if "Nivel 1" in pestanas._tab_dict:
        pestanas.delete("Nivel 1")
    if "Lección 1" in pestanas._tab_dict:
        pestanas.delete("Lección 1")
    pestanas.add("Nivel 1")
    pestanas.set("Nivel 1")
    frame = pestanas.tab("Nivel 1")
    quiz1(frame, datos, pestanas, count=0, correctAns=0)

def quiz1(frame, datos, pestanas, count, correctAns):
    for widget in frame.winfo_children():
        widget.destroy()
    
    xp = datos["xp"]
    mltp = datos["mltp"]
    MostrarLogo.Logo(frame, datos)
    
    abecedario = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    letra1, letra2, letra3, letraCorrecta = random.sample(abecedario, 4)
    
    listaLetras = [letra1, letra2, letra3, letraCorrecta]

    ctk.CTkLabel(frame, text="¿De qué letra se trata?", font=("Segoe UI", 30, "bold")).place(relx=.5, rely=.18, anchor="center")
    ruta1 = f"assets/{letraCorrecta}.mp4"
    Reproductor.reproducir(frame, ruta1)
    
    letraSel1, letraSel2, letraSel3, letraSel4 = random.sample(listaLetras, 4)
    
    ctk.CTkLabel(frame, text=f"Multiplicador de XP: x{mltp}", font= ("Segoe UI", 20)).place(relx=.13, rely=.18, anchor="center")
    ctk.CTkLabel(frame, text=f"Pregunta {count+1}/10", font= ("Segoe UI", 20, "bold")).place(relx=.87, rely=.18, anchor="center")
    
    

    ctk.CTkButton(frame, text=letraSel1, font=("Segoe UI", 15, "bold"), width=255, height=50,
                fg_color="#2275EA", hover_color="#0C229B", border_color="#6077EA",
                command=lambda:verificar(letraSel1, datos, frame, letraCorrecta, pestanas, count, correctAns)).place(relx=.499, rely=.831, anchor="e")
    
    ctk.CTkButton(frame, text=letraSel2, font=("Segoe UI", 15, "bold"), width=255, height=50,
                fg_color="#DE8730", hover_color="#C7770E", border_color="#E2AF5B",
                command=lambda:verificar(letraSel2, datos, frame, letraCorrecta, pestanas, count, correctAns)).place(relx=.499, rely=.93, anchor="e")
    
    ctk.CTkButton(frame, text=letraSel3, font=("Segoe UI", 15, "bold"), width=255, height=50,
                fg_color="#20D95B", hover_color="#087724", border_color="#83DF88",
                command=lambda:verificar(letraSel3, datos, frame, letraCorrecta, pestanas, count, correctAns)).place(relx=.501, rely=.831, anchor="w")
    
    ctk.CTkButton(frame, text=letraSel4, font=("Segoe UI", 15, "bold"), width=255, height=50,
                fg_color="#E12F2F", hover_color="#B51111", border_color="#F85252",
                command=lambda:verificar(letraSel4, datos, frame, letraCorrecta, pestanas, count, correctAns)).place(relx=.501, rely=.93, anchor="w")

def verificar(opcion, datos, frame, letraCorrecta, pestanas, count, correctAns):
    for widget in frame.winfo_children():
        widget.destroy()
    MostrarLogo.Logo(frame, datos)

    mltp = datos["mltp"]
    xpGanada = 0

    if opcion == letraCorrecta:
        mltp += 1
        xpGanada = (xpGanada + 1) * mltp
        datos["xp"] =datos["xp"] +(xpGanada * mltp)
        datos["mltp"] = mltp
        correctAns += 1
        ctk.CTkButton(frame, text="¡Correcto!", font=("Segoe UI", 40, "bold"),
                    hover_color="#32CF42", fg_color="#32CF42", corner_radius=18).place(relx=.5, rely=.4, anchor="center")
        usuario = datos["usuario"]
        with open(f"usuarios/{usuario}.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
    else:
        mltp = 1
        datos["mltp"] = mltp
        ctk.CTkButton(frame, text="Incorrecto :(", font=("Segoe UI", 40, "bold"),
                    hover_color="#AC1C1C", fg_color="#AC1C1C", corner_radius=18).place(relx=.5, rely=.3, anchor="center")
        ctk.CTkLabel(frame, text=f"La respuesta correcta es: {letraCorrecta}", font=("Segoe UI", 20, "bold")).place(relx=.5, rely=.5, anchor="center")
        usuario = datos["usuario"]
        with open(f"usuarios/{usuario}.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    count += 1

    usuario = datos["usuario"]
    

    if count < 10:
        ctk.CTkButton(frame, text="Siguiente ->", font=("Segoe UI", 20, "bold"), fg_color="#223FA7",
                    command=lambda:quiz1(frame, datos, pestanas, count, correctAns)).place(relx=.5, rely=.7, anchor="center")
    else:
        Puntuacion.puntuacion(correctAns, frame, pestanas, datos, count)