import cv2
from PIL import Image, ImageTk
import customtkinter as ctk

def reproducir(frame, ruta_video):
    cap = cv2.VideoCapture(ruta_video)
    etiqueta = ctk.CTkLabel(frame, text="")
    etiqueta.place(relx=.5, rely=.5, anchor="center")

    def actualizar():
        ret, frame_cv = cap.read()
        if ret:
            frame_cv = cv2.resize(frame_cv, (640, 360))  # Ajusta el tamaño del video
            frame_rgb = cv2.cvtColor(frame_cv, cv2.COLOR_BGR2RGB)
            imagen = Image.fromarray(frame_rgb)
            imagen_tk = ImageTk.PhotoImage(imagen)
            etiqueta.configure(image=imagen_tk)
            etiqueta.image = imagen_tk
            frame.after(40, actualizar)
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reinicia el video
            frame.after(40, actualizar)

    actualizar()