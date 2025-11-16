import customtkinter as ctk
import cv2
from PIL import Image, ImageTk

# Inicializar CustomTkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Crear ventana principal
ventana = ctk.CTk()
ventana.geometry("900x600")
ventana.title("Reproductor en pestañas")

# Crear pestañas
pestanas = ctk.CTkTabview(master=ventana, width=850, height=550)
pestanas.pack(pady=20)

# Pestaña de video
pestanas.add("Lección en video")
frame_video = pestanas.tab("Lección en video")

# Etiqueta donde se mostrará el video
etiqueta_video = ctk.CTkLabel(frame_video, text="")
etiqueta_video.pack(expand=True, fill="both")

# Cargar video con OpenCV
cap = cv2.VideoCapture("assets/ejemplo.mp4")  # Asegúrate de tener este archivo

def reproducir():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imagen = Image.fromarray(frame)
        imagen_tk = ImageTk.PhotoImage(image=imagen)
        etiqueta_video.configure(image=imagen_tk)
        etiqueta_video.image = imagen_tk
        ventana.after(30, reproducir)
    else:
        cap.release()

# Botón para iniciar reproducción
ctk.CTkButton(frame_video, text="Reproducir video", command=reproducir).pack(pady=10)

# Otra pestaña de ejemplo
pestanas.add("Información")
frame_info = pestanas.tab("Información")
ctk.CTkLabel(frame_info, text="Aquí puedes mostrar contenido adicional.").pack(pady=20)

ventana.mainloop()