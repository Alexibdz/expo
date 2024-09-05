from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="INVENTARIOS", bg="#dddddd", font="sans 30 bold", anchor=CENTER)
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, height=90)
        
        frame2 = tk.Frame(self, bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)

        lbl_frame = LabelFrame(frame2, text="Productos", bg="#C6D9E3", font="sans 22 bold")
        lbl_frame.place(x=20, y=30, width=400, height=500)

        lbl_nombre = Label(lbl_frame, text="Nombre: ", font="sans 14 bold", bg="#C6D9E3")
        lbl_nombre.place(x=10, y=20)
        self.entry_nombre = ttk.Entry(lbl_frame, font="sans 14 bold")
        self.entry_nombre.place(x=140, y=20, width=240, height=40)

        lbl_proveedor = Label(lbl_frame, text="Proveedor: ", font="sans 14 bold", bg="#C6D9E3")
        lbl_proveedor.place(x=10, y=80)
        self.entry_proveedor = ttk.Entry(lbl_frame, font="sans 14 bold")
        self.entry_proveedor.place(x=140, y=80, width=240, height=40)

        lbl_precio = Label(lbl_frame, text="Precio: ", font="sans 14 bold", bg="#C6D9E3")
        lbl_precio.place(x=10, y=140)
        self.entry_precio = ttk.Entry(lbl_frame, font="sans 14 bold")
        self.entry_precio.place(x=140, y=140, width=240, height=40)

        lbl_costo = Label(lbl_frame, text="Costo: ", font="sans 14 bold", bg="#C6D9E3")
        lbl_costo.place(x=10, y=200)
        self.entry_costo = ttk.Entry(lbl_frame, font="sans 14 bold")
        self.entry_costo.place(x=140, y=200, width=240, height=40)

        lbl_stock = Label(lbl_frame, text="Stock: ", font="sans 14 bold", bg="#C6D9E3")
        lbl_stock.place(x=10, y=260)
        self.entry_stock = ttk.Entry(lbl_frame, font="sans 14 bold")
        self.entry_stock.place(x=140, y=260, width=240, height=40)

        btn_agregar = tk.Button(lbl_frame, text="Agregar",  bg="#dddddd", font="sans 14 bold")        
        btn_agregar.place(x=80, y=340, width=240, height=40)

        btn_editar = tk.Button(lbl_frame, text="Editar",  bg="#dddddd", font="sans 14 bold")        
        btn_editar.place(x=80, y=400, width=240, height=40)

        #Tabla
        treeFrame = tk.Frame(frame2, bg="#C6D9E3")
        treeFrame.place(x=440, y=50, width=620, height=400)

        scroll_y = ttk.Scrollbar(treeFrame)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(treeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(treeFrame, columns=("ID", "PRODUCTO", "PROVEEDOR", "PRECIO", "COSTO", "STOCK"), show="headings", 
                                 height=40, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)

        self.tree.heading("ID", text="ID")
        self.tree.heading("PRODUCTO", text="Prodcuto")
        self.tree.heading("PROVEEDOR", text="Proveedor")
        self.tree.heading("PRECIO", text="Precio")
        self.tree.heading("COSTO", text="Costo")
        self.tree.heading("STOCK", text="Stock")

        self.tree.column("ID", width=70, anchor="center")
        self.tree.column("PRODUCTO", width=100, anchor="center")
        self.tree.column("PROVEEDOR", width=100, anchor="center")
        self.tree.column("PRECIO", width=100,anchor="center")
        self.tree.column("COSTO", width=100,anchor="center")
        self.tree.column("STOCK", width=70, anchor="center")
        
        self.tree.pack(expand=True, fill=BOTH)