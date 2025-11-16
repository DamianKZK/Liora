import customtkinter as ctk
from PIL import Image
import Lecciones
import Perfil

def principal(datos, pestanas):
    pestanas.add("Inicio")
    pestanas.add("Perfil")
    frame = pestanas.tab("Inicio")

    #se imprime el logo
    imagen_original = Image.open("assets/LOGOSF.png")
    imagen_ctk = ctk.CTkImage(light_image=imagen_original, size=(200, 200))
    ctk.CTkLabel(frame, image=imagen_ctk, text="").place(relx=0.07, rely=0.06, anchor="center")
    #se extraen los datos que se pasaron para mostrar el usuario 
    usuario = datos["usuario"]
    xp= datos["xp"]
    
    ctk.CTkButton(frame, text=f"XP: {xp}", fg_color="#2441D5", hover_color="#2441D5" ).place(relx=.85, rely=.04, anchor="center")
    
    

    ctk.CTkLabel(frame, text=f"¡BIENVENIDO {usuario}!", font=("Segoe UI", 50, "bold")).place(relx=0.5, rely=0.2, anchor="center")

    marco_info = ctk.CTkFrame(master=frame, width=750, height=250, corner_radius=20, fg_color="#f0f0f0")
    marco_info.place(relx=0.5, rely=0.55, anchor="center")

    ctk.CTkLabel(marco_info, text="¿Qué es LIORA?", font=("Segoe UI", 24, "bold"), text_color="#333333").pack(pady=(20, 10))
    ctk.CTkLabel(marco_info, text="""Liora es una plataforma educativa para aprender y practicar Lengua de Señas Mexicana.
Cuenta con recursos visuales, quizzes para poner en práctica lo aprendido y próximamente la función de llamadas
para poner a prueba tus conocimientos con personas que están aprendiendo, ¡al igual que tú!""",font=("Segoe UI", 16), text_color="#444444", wraplength=700, justify="center").pack(pady=(0, 20))        
    Lecciones.lessonSelector(pestanas, datos)
    Perfil.info(pestanas, datos)   