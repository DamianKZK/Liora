import customtkinter as ctk
import csv
import PantallaPrincipal
import json
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Ventana raíz oculta
root = ctk.CTk()
root.withdraw()


# Función para mostrar pantalla de carga y luego login
def abrirPantallaCarga(ventana_actual):
    ventana_actual.destroy()

    carga = ctk.CTkToplevel()
    carga.geometry("400x200")
    carga.title("Cargando...")

    ctk.CTkLabel(carga, text="Preparando entorno...", font=("Segoe UI", 18)).pack(pady=40)

    carga.after(200, lambda: [carga.destroy(), login()])

# Verifica contraseñas y muestra pantalla de carga
def verificarContrasena(pass1, pass2, user, ventana_actual):
    if pass1 != pass2:
        error = ctk.CTkToplevel()
        error.transient(ventana_actual) 
        error.focus()
        error.grab_set()
        error.geometry("300x100")
        error.title("Error")
        ctk.CTkLabel(error, text=" Las contraseñas no coinciden").pack(pady=20)
        return
        
    else:      
        ruta = f"usuarios/{user}.json"
        if os.path.exists(ruta):
            print("El usuario ya existe.")
            return
        datos = {
            "usuario":user,
            "contraseña":pass1,
            "nivel": 0,
            "xp":0
                }
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)
        print("Usuario registrado correctamente")
        login()

# Verifica login
def verificarDatos(usuario, contraseña, ventana_actual):
    ruta = f"usuarios/{usuario}.json"
    if not os.path.exists(ruta):
        noReg = ctk.CTkToplevel()
        noReg.transient(ventana_actual) 
        noReg.grab_set()
        noReg.focus()
        noReg.geometry("300x100")
        noReg.title("Error")
        ctk.CTkLabel(noReg, text="Usuario no registrado").pack(pady=20)
        print("Usuario no registrado")
        return False
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if datos["contraseña"]==contraseña:
        print("Login exitoso")
        PantallaPrincipal.principal(usuario, ventana_actual)
        ventana_actual.destroy()
        return
    else:
        error = ctk.CTkToplevel()
        error.transient(ventana_actual) 
        error.grab_set()
        error.focus()
        error.geometry("300x100")
        error.title("Error")
        ctk.CTkLabel(error, text="ContraseñaIncorrecta").pack(pady=20)    

# Ventana de login
def login():
    WinLog = ctk.CTkToplevel()
    WinLog.geometry("900x620")
    WinLog.title("Liora")

    ctk.CTkLabel(WinLog, text="¡Bienvenido a Liora β!", font=("Segoe UI", 30, "bold")).pack(pady=50)
    ctk.CTkLabel(WinLog, text="Iniciar sesión", font=("Arial", 20, "bold")).pack()

    entry_usuario = ctk.CTkEntry(WinLog, placeholder_text="Usuario")
    entry_usuario.pack(pady=5)

    entry_contraseña = ctk.CTkEntry(WinLog, placeholder_text="Contraseña", show="*")
    entry_contraseña.pack(pady=5)

    ctk.CTkButton(
        WinLog,
        text="Iniciar sesión",
        command=lambda: verificarDatos(entry_usuario.get(), entry_contraseña.get(), WinLog)
    ).pack(pady=10)

    ctk.CTkLabel(WinLog, text="¿Aún no tienes cuenta?", font=("Segoe UI", 13)).pack(pady=5)

    ctk.CTkButton(WinLog, text="Regístrate", command=lambda: register(WinLog)).pack()

# Ventana de registro
def register(ventana_login):
    ventana_login.destroy()

    WinReg = ctk.CTkToplevel()
    WinReg.geometry("900x620")
    WinReg.title("¡Regístrate!")

    ctk.CTkLabel(WinReg, text="Registro", font=("Segoe UI", 30, "bold")).pack(pady=40)

    entry_usuario = ctk.CTkEntry(WinReg, placeholder_text="Ingrese nombre de usuario")
    entry_usuario.pack(pady=5)

    entry_contraseña = ctk.CTkEntry(WinReg, placeholder_text="Ingrese contraseña", show="°")
    entry_contraseña.pack(pady=5)

    entry_confirmacion = ctk.CTkEntry(WinReg, placeholder_text="Confirme contraseña", show="°")
    entry_confirmacion.pack(pady=5)

    ctk.CTkButton(
        WinReg,
        text="Registrarse",
        command=lambda: verificarContrasena(entry_contraseña.get(), entry_confirmacion.get(), entry_usuario.get(), WinReg)
    ).pack(pady=10)

# Inicia la app
login()
root.mainloop()