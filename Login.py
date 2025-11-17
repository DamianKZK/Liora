import customtkinter as ctk
import json
import os
import PantallaPrincipal

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("990x620")
root.iconbitmap("assets/LOGUITO.ico")
root.title("Liora β")

pestanas = ctk.CTkTabview(master=root, width=990, height=620, #fg_color="#D7EAE9",
                        segmented_button_fg_color="#7BA88F",  # Color de fondo de la barra
                        segmented_button_selected_color="#31AB68",
                        segmented_button_unselected_color="#7BA88F"
)
pestanas.pack(fill="both", expand=True)



def verificarContrasena(pass1, pass2, user):
    if "Error" in pestanas._tab_dict:
        pestanas.delete("Error")
    if pass1 != pass2:   
        pestanas.add("Error")
        pestanas.set("Error")
        frame = pestanas.tab("Error")
        ctk.CTkLabel(frame, text="Las contraseñas no coinciden").pack(pady=20)
        register()
        return
    else:
        ruta = f"usuarios/{user}.json"
        if os.path.exists(ruta):
            pestanas.add("Error")
            pestanas.set("Error")
            frame = pestanas.tab("Error")
            ctk.CTkLabel(frame, text="El usuario ya existe").pack(pady=20)
            return
        datos = {
            "usuario": user,
            "contraseña": pass1,
            "quiz1": False,
            "quiz2":False,
            "quiz3":False,
            "xp": 0,
            "mltp":1
        }
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)
        pestanas.delete("Registro")
        login()


def verificarDatos(usuario, contraseña):
    ruta = f"usuarios/{usuario}.json"
    if not os.path.exists(ruta):
        pestanas.add("Error")
        frame = pestanas.tab("Error")
        ctk.CTkLabel(frame, text="Usuario no registrado").pack(pady=20)
        return
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if datos["contraseña"] == contraseña:
        pestanas.delete("Login")
        if "Error" in pestanas._tab_dict:
            pestanas.delete("Error")
        PantallaPrincipal.principal(datos, pestanas)
    else:
        pestanas.add("Error")
        frame = pestanas.tab("Error")
        ctk.CTkLabel(frame, text="Contraseña incorrecta").pack(pady=20)


def login():
    if "Login" in pestanas._tab_dict:
        pestanas.set("Login")  # Solo la activa si ya existe
        return

    pestanas.add("Login")
    pestanas.set("Login")
    frame = pestanas.tab("Login")



    ctk.CTkLabel(frame, text="¡Bienvenido a Liora β!", font=("Segoe UI", 30, "bold")).pack(pady=50)
    ctk.CTkLabel(frame, text="Iniciar sesión", font=("Arial", 20, "bold")).pack()

    entry_usuario = ctk.CTkEntry(frame, placeholder_text="Usuario")
    entry_usuario.pack(pady=5)

    entry_contraseña = ctk.CTkEntry(frame, placeholder_text="Contraseña", show="•")
    entry_contraseña.pack(pady=5)

    ctk.CTkButton(
        frame,
        text="Iniciar sesión",
        command=lambda: verificarDatos(entry_usuario.get(), entry_contraseña.get())
    ).pack(pady=10)

    ctk.CTkLabel(frame, text="¿Aún no tienes cuenta?", font=("Segoe UI", 13)).pack(pady=5)
    ctk.CTkButton(frame, text="Regístrate", command=register).pack()


def register():
    pestanas.delete("Login")
    if "Error" in pestanas._tab_dict:
        pestanas.delete("Error")
    pestanas.add("Registro")
    pestanas.set("Registro")
    frame = pestanas.tab("Registro")

    ctk.CTkLabel(frame, text="Registro", font=("Segoe UI", 30, "bold")).pack(pady=40)

    entry_usuario = ctk.CTkEntry(frame, placeholder_text="Ingrese nombre de usuario")
    entry_usuario.pack(pady=5)

    entry_contraseña = ctk.CTkEntry(frame, placeholder_text="Ingrese contraseña", show="•")
    entry_contraseña.pack(pady=5)

    entry_confirmacion = ctk.CTkEntry(frame, placeholder_text="Confirme contraseña", show="•")
    entry_confirmacion.pack(pady=5)

    ctk.CTkButton(
        frame,
        text="Registrarse",
        command=lambda: verificarContrasena(entry_contraseña.get(), entry_confirmacion.get(), entry_usuario.get())
    ).pack(pady=10)


login()
root.mainloop()