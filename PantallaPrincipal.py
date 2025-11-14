import customtkinter as ctk


def principal(usuario, ventana_actual):
    ventana_actual.destroy()
    principalWin = ctk.CTkToplevel()
    principalWin.geometry("990x620")
    principalWin.title("Liora")

    principalWin.update_idletasks()
    ancho = principalWin.winfo_width()
    alto = principalWin.winfo_height()

    print("Ancho:", ancho)
    print("Alto:", alto)

    # Menú superior
    ctk.CTkLabel(principalWin, text="Liora β", font=("Segoe UI", 30, "bold")).place(relx=0.1, rely=0.06, anchor="center")
    ctk.CTkButton(principalWin, text="Inicio").place(relx=0.3, rely=0.067, anchor="center")
    ctk.CTkButton(principalWin, text="Lecciones", fg_color="light grey", text_color="black").place(relx=0.450, rely=0.067, anchor="center")
    ctk.CTkButton(principalWin, text="Llamadas", fg_color="light grey", text_color="black").place(relx=0.6, rely=0.067, anchor="center")
    ctk.CTkButton(principalWin, text="Perfil", fg_color="light grey", text_color="black").place(relx=0.75, rely=0.067, anchor="center")

    # Título de bienvenida
    ctk.CTkLabel(principalWin, text=f"¡BIENVENIDO {usuario}!", font=("Segoe UI", 50, "bold")).place(relx=0.5, rely=0.2, anchor="center")

    # Marco de introducción
    marco_info = ctk.CTkFrame(
        master=principalWin,
        width=750,
        height=250,
        corner_radius=20,
        fg_color="#f0f0f0"
    )
    marco_info.place(relx=0.5, rely=0.55, anchor="center")

    # Título dentro del marco
    ctk.CTkLabel(
        master=marco_info,
        text="¿Qué es LIORA?",
        font=("Segoe UI", 24, "bold"),
        text_color="#333333"
    ).pack(pady=(20, 10))

    # Texto explicativo
    ctk.CTkLabel(
        master=marco_info,
        text="""Liora es una plataforma educativa para aprender y practicar Lengua de Señas Mexicana.
Cuenta con recursos visuales, quizzes para poner en práctica lo aprendido y próximamente la función de llamadas
para poner a prueba tus conocimientos con personas que están aprendiendo, ¡al igual que tú!""",
        font=("Segoe UI", 16),
        text_color="#444444",
        wraplength=700,
        justify="center"
    ).pack(pady=(0, 20))

    