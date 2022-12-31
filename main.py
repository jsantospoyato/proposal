import sys
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def closing(base, base2) -> None:
    """ 
    Muestra info y borra las ventanas si se ha aceptado
    
    """
    messagebox.showinfo("Has aceptado","Lo sabía... Eres la mejor, no cambies!")
    base2.destroy()
    base.destroy()
    sys.exit(0)

def cannotLeave() -> None:
    """
    Evita que se salga de la app si se intenta cerrar.
    """

    messagebox.showinfo(
        "Has intentado salir", "NO PUEDES SALIR, ELIGE UNA RESPUESTA.")
    main()

def newWindow(base) -> None:
    """ Crea una nueva ventana con el mensaje de aceptar y sale de la aplicación """

    base2 = tk.Tk()
    base2.withdraw()
    base2.protocol("WM_DELETE_WINDOW", closing(base, base2))
    base2.mainloop()

def move(pos) -> None:
    """ 
    Mueve el boton de NO, evitando que se pueda clickar sobre él
    """

    b2.place(x=pos[0], y=pos[1])

def main() -> None:

    # Crear Ventana
    base = tk.Tk()
    base.title("Proposición")
    base.geometry("800x640")
    base.focus_force()
    
    # Creando fondo y frame
    try:
        image =  Image.open("./img/background.jpg")
        bg = ImageTk.PhotoImage(image)

        label2 = tk.Label(base, image=bg)
        label2.pack(pady=10)
    except:
        pass

    # Creando texto de titulo
    label = tk.Label(base, text="Yo quiero pasar el resto de mi vida contigo, ¿y tú?")
    label.config(font=("Raleway", 20))
    label.pack(pady=10)

    # Botones de si o no
    global b2
    pos = 0
    b1 = tk.Button(base, width=10, text='SÍ', fg="White", bg="Black", command=(lambda: newWindow(base)))
    b1.config(font=("Raleway", 20))
    b1.pack(pady=20)
    b2 = tk.Button(base, width=10, text='NO', fg="White", bg="Black",
                   command=(lambda: move([base.winfo_pointerx()+20, b2.winfo_rooty()])))
    b2.config(font=("Raleway", 20))
    b2.pack(pady=20)

    # Bucle de aplicación con protocolo anti-salida
    base.mainloop()
    base.protocol("WM_DELETE_WINDOW", cannotLeave())
    sys.exit(0)

if __name__ == '__main__':
    main()