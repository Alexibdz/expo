import tkinter as tk
import time
import random

# Ventana principal
ventana_principal = tk.Tk()
ventana_principal.title('Carrera de autos')
ventana_principal.geometry('1600x800+60+0')
ventana_principal.config(background='white')

class auto_de_carrera:
    def __init__(self, nombre, nro):
        self.name = nombre
        self.id = nro
        self.vuelta = 0
        self.auto_url = tk.PhotoImage(file=f"Carrera_de_autos/images/auto{nro}.png").zoom(4).subsample(50)
        self.pista = tk.Canvas(label_frame, width=1600, height=100, bg='grey')
        self.posicion_x = 0
        self.auto_imagen = self.pista.create_image(self.posicion_x, 50, anchor="nw", image=self.auto_url)
        self.pista.pack(pady=5)

# Configurar cada canvas
label_frame = tk.LabelFrame(ventana_principal, text="Pistas")
label_frame.pack(padx=5, pady=5)

auto1 = auto_de_carrera('Azul',1)
auto2 = auto_de_carrera('Negro',2)
auto3 = auto_de_carrera('Rojo',3)
auto4 = auto_de_carrera('Verde',4)
competidores = [auto1, auto2, auto3, auto4]

def reiniciar():
    global competidores
    global label_ganador
    for competidor in competidores:
        competidor.posicion_x = 0
        competidor.pista.coords(competidor.auto_imagen, competidor.posicion_x, 50)
    ventana_principal.update()
    empezar_juego()

def empezar_juego():
    global competidores
    global ganador
    ganador = None
    
    while ganador is None:
        ventana_principal.update()  # Actualiza la ventana principal
        
        time.sleep(0.05)
        for competidor in competidores:
            nueva_posicion = random.randint(0, 10)
            if nueva_posicion == 10:
                nueva_posicion_boost = random.randint(0,3)
                nueva_posicion += nueva_posicion_boost
            if nueva_posicion == 0:
                nueva_posicion_boost = random.randint(1,3)
                nueva_posicion += nueva_posicion_boost
            competidor.pista.move(competidor.auto_imagen, nueva_posicion, 0)
            competidor.posicion_x += nueva_posicion
            print(f"{competidor.name}: {competidor.posicion_x}")
           
       
        def verificar_vuelta(competidores):
            for competidor in competidores:
                if competidor.vuelta == 3:
                    return competidor.name
                if competidor.posicion_x >= 1500:
                    competidor.vuelta += 1
                    competidor.posicion_x = 0+(competidor.posicion_x-1500)
                    competidor.pista.coords(competidor.auto_imagen, 
                    competidor.posicion_x, 50)
                    b1.config(text=f'Vuelta{competidor.vuelta}')
                
                
        #vueltas_completadas = verificar_vuelta()
        ganador = verificar_vuelta(competidores)

        if ganador:
            label_ganador = tk.Label(ventana_principal, text=f"{ganador} ganó!!", font=('Arial', 20), bg="white")
            label_ganador.pack(pady=5)
            b1.config(text='Volver a jugar', command=reiniciar)


l2 = tk.Label(ventana_principal, text='Para ganar el auto debe llegar 3 veces al final. El auto avanzara del 0 a 10 aleatoriamente cada 0,05segundo', font=('Arial', 20), bg='white')
l2.pack(pady=25)

b1 = tk.Button(ventana_principal, text='JUGAR!', font=('Arial', 20), height=2, width=15, command=empezar_juego)
b1.pack(pady=25)

ventana_principal.mainloop()
