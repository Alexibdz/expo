from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Ventas(tk.Frame):
    def __init__(self, parametro):
        super().__init__(parametro) #1100, 650
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="VENTAS", bg="#dddddd", font="sans 30 bold", anchor=CENTER)
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, height=90)

        frame2 = tk.Frame(self, bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)

        lbl_frame = LabelFrame(frame2, text="Informacion de ventas", bg="#C6D9E3", font="sans 16 bold")
        lbl_frame.place(x=10, y=10, width=1060, height=80)

        lbl_nro_factura = tk.Label(lbl_frame, text="Numero de \n factura", bg="#C6D9E3", font="sans 12 bold")
        lbl_nro_factura.place(x=10, y=5)
        self.numero_factura = tk.StringVar()
        self.entry_nro_faactura = ttk.Entry(lbl_frame, textvariable=self.numero_factura, state="readonly", font="sans 12 bold")
        self.entry_nro_faactura.place(x=100, y=10, width=50)

        lbl_nombre = tk.Label(lbl_frame, text="Productos:", bg="#C6D9E3", font="sans 12 bold")
        lbl_nombre.place(x=200, y=12)
        self.entry_nombre = tk.Entry(lbl_frame, font="sans 12 bold")
        self.entry_nombre.place(x=280, y=10, width=180)

        label_valor = tk.Label(lbl_frame, text="Precio: ", bg="#C6D9E3", font="sans 12 bold")
        label_valor.place(x=470, y=12)
        self.entry_valor = ttk.Entry(lbl_frame, font="sans 12 bold")
        self.entry_valor.place(x=540, y=10, width=180)

        label_cantidad = tk.Label(lbl_frame, text="Cantidad: ", bg="#C6D9E3", font="sans 12 bold")
        label_cantidad.place(x=730, y=12)
        self.entry_cantidad = ttk.Entry(lbl_frame, font="sans 12 bold")
        self.entry_cantidad.place(x=820, y=10, width=180)

        treeFrame = tk.Frame(frame2, bg="#C6D9E3")
        treeFrame.place(x=150, y=120, width=800, height=200)

        scroll_y = ttk.Scrollbar(treeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(treeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(treeFrame, columns=("Producto", "Precio", "Cantidad", "Subtotal"), show="headings", 
                                 height=10, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)
        
        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Precio")
        self.tree.heading("#3", text="Cantidad")
        self.tree.heading("#4", text="Subtotal")

        self.tree.column("Producto", anchor="center")
        self.tree.column("Precio", anchor="center")
        self.tree.column("Cantidad", anchor="center")
        self.tree.column("Subtotal", anchor="center")
        
        self.tree.pack(expand=True, fill=BOTH)

        lbl_frame1 = LabelFrame(frame2, text="Opciones", bg="#C6D9E3", font="sans 12 bold")
        lbl_frame1.place(x=10, y=380, width=1060, height=100)

        btn_agregar = tk.Button(lbl_frame1, text="Agregar articulo",  bg="#dddddd", font="sans 12 bold")        
        btn_agregar.place(x=50, y=10, width=240, height=50)

        btn_pagar = tk.Button(lbl_frame1, text="Pagar",  bg="#dddddd", font="sans 12 bold")        
        btn_pagar.place(x=400, y=10, width=240, height=50)

        btn_agregar = tk.Button(lbl_frame1, text="Agregar articulo",  bg="#dddddd", font="sans 12 bold")        
        btn_agregar.place(x=750, y=10, width=240, height=50)