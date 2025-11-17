import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import MostrarLogo
import json


def puntuacion(aciertos, frame, pestanas, datos, count):
    for widget in frame.winfo_children():
        widget.destroy()
    usuario  = datos["usuario"]

    MostrarLogo.Logo(frame, datos)
    puntos =( (aciertos*count)/100)*100
    complete = datos["quiz1"]
    ctk.CTkLabel(frame, text="¡Muy bien! tu puntuacion final es:", font=("Segoe UI", 25, "bold")).place(relx=.5, rely=.3, anchor="center")
    if aciertos==0:
        puntos=0
        
    if puntos>=85:
        ctk.CTkLabel(frame, text=puntos, font=("Segoe UI", 30, "bold"), text_color="#40E00F").place(relx=.5, rely=.7, anchor="center")
        ctk.CTkLabel(frame, text="Quiz completado\n\nCalificación sobresaliente", font=("Segoe UI", 30, "bold"), text_color="#40E00F").place(relx=.5, rely=.6, anchor="center")

        complete = True
        datos["quiz1"] = complete
    elif puntos<80 and puntos>70:
        ctk.CTkLabel(frame, text=f"{puntos}\n\nQuiz completado\nCalificación regular", font=("Segoe UI", 30, "bold"), text_color="#E3E321").place(relx=.5, rely=.6, anchor="center")
        complete = True
        datos["quiz1"] = complete
        
    else:
        ctk.CTkLabel(frame, text=f"{puntos}\n\nCalificación baja", font=("Segoe UI", 30, "bold"), text_color="#E02E0F").place(relx=.5, rely=.6, anchor="center")
        ctk.CTkLabel(frame, text="¡Vuelve a la lección intentalo de Nuevo!", font=("Segoe UI", 20, "bold"), text_color="#000000").place(relx=.5, rely=.8, anchor="center")
        complete = False
        datos["quiz1"] = complete
    with open(f"{usuario}.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)