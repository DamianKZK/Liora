import customtkinter as ctk
import json
import os


def info(pestanas, datos):
    if "Perfil" in pestanas._tab_dict:
        pestanas.delete("Perfil")
    pestanas.add("Perfil")
    frame = pestanas.tab("Perfil")
    
    usuario = datos["usuario"]
    xp = datos["xp"]
    ctk.CTkLabel(frame, text="Perfíl: ", font=("Segoe UI", 30, "bold")).place(relx=.2, rely=.1, anchor="center")
    ctk.CTkLabel(frame, text=f"Nombre de usuario: {usuario}\nXP: {xp}", 
                font=("Segoe UI ", 20), justify="left").place(relx=.2, rely=.2, anchor="center")