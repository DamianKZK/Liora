import customtkinter as ctk
import json
import os
from PIL import Image 
import MostrarLogo


def info(pestanas, datos):
    if "Perfíl" in pestanas._tab_dict:
        pestanas.delete("Perfíl")
    pestanas.add("Perfíl")
    usuario= datos["usuario"]
    frame = pestanas.tab("Perfíl")
    with open(f"usuarios/{usuario}.json", "r", encoding="utf-8") as archivo:
        datos_actualizados = json.load(archivo)
    
    usuario1 = datos_actualizados["usuario"]
    xp = datos_actualizados["xp"]
    nivel= datos_actualizados["mltp"]
    
    MostrarLogo.Logo(frame, datos)

    ctk.CTkButton(frame, text="Información del perfíl: ", font=("Segoe UI", 30, "bold"),fg_color="#2F419E", hover_color ="#2F419E").place(relx=.5, rely=.2, anchor="center")
    ctk.CTkLabel(frame, text=f"•Nombre de usuario: {usuario1}\n\n•XP: {xp}\n\n•Racha: ---\n\n•Multiplicador activo: {nivel}", 
                font=("Segoe UI ", 20), justify="left").place(relx=.45, rely=.45, anchor="center")