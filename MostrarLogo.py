import customtkinter as ctk
from PIL import Image
import os


def Logo(frame, datos):
    imagen_original = Image.open("assets/LogoN.png")
    imagen_ctk = ctk.CTkImage(light_image=imagen_original, size=(150, 130))
    ctk.CTkLabel(frame, image=imagen_ctk, text="").place(relx=0.09, rely=0.06, anchor="center")
    #se extraen los datos que se pasaron para mostrar el usuario 
    usuario = datos["usuario"]
    xp= datos["xp"]
    
    ctk.CTkButton(frame, text=f"XP: {xp}", font=("Segoe UI", 12, "bold"), fg_color="#2F419E", hover_color="#2F419E", corner_radius=20 ).place(relx=.9, rely=.04, anchor="center")