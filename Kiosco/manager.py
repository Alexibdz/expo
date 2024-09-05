from tkinter import Tk, Frame
from container import Container
from ttkthemes import ThemedStyle

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Caja registradora v1.0')
        self.resizable(False, False)
        self.config(bg="#C6D9E3")
        self.geometry("800x400+120+20")

        self.container = Frame(self, bg="#C6D9E3")
        self.container.pack(fill="both", expand=True)

        self.frames = {Container: None}

        self.cargar_frames()

        self.mostar_frames(Container)
        
        self.set_theme()

    def cargar_frames(self):
        for item in self.frames.keys():
            frame = item(self.container, self)
            self.frames[item] = frame
    
    def mostar_frames(self, item):
        frame = self.frames[item]
        frame.tkraise()
    
    def set_theme(self):
        estilo = ThemedStyle(self)
        estilo.set_theme("breeze")

def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()