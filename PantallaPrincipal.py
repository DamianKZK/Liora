import customtkinter as ctk
from PIL import Image
import Lecciones
import Perfil
import Quiz
import MostrarLogo

def principal(datos, pestanas):
    pestanas.add("Inicio")
    #pestanas.add("Perfil")
    frame = pestanas.tab("Inicio")


    usuario = datos["usuario"]
    xp= datos["xp"]
    MostrarLogo.Logo(frame, datos)    
    

    ctk.CTkLabel(frame, text=f"¡Bienvenido {usuario}!", font=("Segoe UI", 50, "bold")).place(relx=0.5, rely=0.2, anchor="center")

    marco_info = ctk.CTkFrame(master=frame, width=750, height=250, corner_radius=20, fg_color="#CBEDCF")
    marco_info.place(relx=0.5, rely=0.55, anchor="center")

    ctk.CTkLabel(marco_info, text="¿Qué es LIORA?", font=("Segoe UI", 24, "bold"), text_color="#333333", fg_color="#61B461").pack(pady=(0, 8))
    ctk.CTkLabel(marco_info, text="""Liora es una plataforma educativa para aprender y practicar Lengua de Señas Mexicana.
Cuenta con recursos visuales, quizzes para poner en práctica lo aprendido y próximamente la función de llamadas para poner a prueba tus conocimientos con personas que están aprendiendo, ¡al igual que tú!"""
,font=("Segoe UI", 16), text_color="#444444", wraplength=700, fg_color="#CBEDCF", justify="left").pack(pady=(0, 20))        
    
    Lecciones.lessonSelector(pestanas, datos)
    Quiz.quiz(pestanas, datos) 
    Perfil.info(pestanas, datos) 