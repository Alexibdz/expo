from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

class Ventas(tk.Frame):
    def __init__(self, parametro):
        super().__init__(parametro)  # 1100, 650
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
        self.entry_nro_factura = ttk.Entry(lbl_frame, textvariable=self.numero_factura, state="readonly", font="sans 12 bold")
        self.entry_nro_factura.place(x=100, y=10, width=50)

        lbl_nombre = tk.Label(lbl_frame, text="Productos:", bg="#C6D9E3", font="sans 12 bold")
        lbl_nombre.place(x=200, y=12)
        self.entry_nombre = ttk.Combobox(lbl_frame, font="sans 12 bold", state="readonly")
        self.entry_nombre.place(x=280, y=10, width=180)

        self.cargar_productos()

        label_valor = tk.Label(lbl_frame, text="Precio: ", bg="#C6D9E3", font="sans 12 bold")
        label_valor.place(x=470, y=12)
        self.entry_valor = ttk.Entry(lbl_frame, font="sans 12 bold", state="readonly")
        self.entry_valor.place(x=540, y=10, width=180)

        self.entry_nombre.bind("<<ComboboxSelected>>", self.actualizar_precio)

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

        btn_agregar = tk.Button(lbl_frame1, text="Agregar articulo", bg="#dddddd", font="sans 12 bold")
        btn_agregar.place(x=50, y=10, width=240, height=50)

        btn_pagar = tk.Button(lbl_frame1, text="Pagar", bg="#dddddd", font="sans 12 bold")
        btn_pagar.place(x=400, y=10, width=240, height=50)

        btn_ver_facturas = tk.Button(lbl_frame1, text="Ver facturas", bg="#dddddd", font="sans 12 bold")
        btn_ver_facturas.place(x=750, y=10, width=240, height=50)

        self.lbl_suma_total = tk.Label(frame2, text="Total a pagar: ARS 0", bg="#C6D9E3", font="sans 25 bold")
        self.lbl_suma_total.place(x=360, y=335)

    def crear_conexion(self):
        """Crear y devolver la conexión a la base de datos MySQL."""
        try:
            conexion = mysql.connector.connect(
                host='localhost',  # Host
                user='root',  # Usuario de MySQL
                password='',  # Contraseña de MySQL
                database='kiosco_db'  # Base de datos en MySQL
            )
            return conexion
        except Error as e:
            messagebox.showerror("Error de conexión", f"Error al conectar con la base de datos: {e}")
            return None

    def cargar_productos(self):
        """Cargar los productos desde la base de datos y asignarlos al combobox."""
        conexion = self.crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT nombre FROM inventario")
                productos = cursor.fetchall()
                self.entry_nombre["values"] = [producto[0] for producto in productos]
                if not productos:
                    print("No se encontraron productos en la base de datos.")
                cursor.close()
            except Error as e:
                print("Error al cargar productos desde la base de datos: ", e)
            finally:
                conexion.close()

    def actualizar_precio(self, event):
        """Actualizar el precio del producto seleccionado en el combobox."""
        nombre_producto = self.entry_nombre.get()
        conexion = self.crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT precio FROM inventario WHERE nombre = %s", (nombre_producto,))
                precio = cursor.fetchone()
                if precio:
                    self.entry_valor.config(state="normal")
                    self.entry_valor.delete(0, tk.END)
                    self.entry_valor.insert(0, precio[0])
                    self.entry_valor.config(state="readonly")
                else:
                    self.entry_valor.config(state="normal")
                    self.entry_valor.delete(0, tk.END)
                    self.entry_valor.insert(0, "Precio no disponible")
                    self.entry_valor.config(state="readonly")
                cursor.close()
            except Error as e:
                messagebox.showerror("Error", f"Error al obtener el precio: {e}")
            finally:
                conexion.close()

    def actualizar_total(self):
        total = 0.0
        for child in self.tree.get_children():
            subtotal = float(self.tree.item(child, "values") [3])
            total += subtotal
        self.lbl_suma_total.config(text=f"Total a pagar: ARS {total:.0f}")

    def registrar(self):
        producto = self.entry_nombre.get()
        precio = self.entry_valor.get()
        cantidad = self.entry_cantidad.get()

        if producto and precio and cantidad:
            try:
                cantidad = int(cantidad)
                if not self.verificar_stock(producto, cantidad):
                    messagebox.showerror("Error", "Stock insuficiente para el producto seleccionado")
                    return
                precio = float(precio)
                subtotal = cantidad * precio
                
                self.tree.insert("", "end", values=(producto, f"{precio:.0f}", cantidad, f"subtotal:.0f"))
                
                self.entry_nombre.set("")
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.config(state="readonly")
                self.entry_cantidad.delete(0, tk.END)

                self.actualizar_total()
            except ValueError:
                messagebox.showerror("Error", "Cantidad o precio no validos")
        else:
            messagebox.showerror("Error", "Debe Completar todos los campos")

    def verificar_stock(self, nombre_producto, cantidad):
        conexion = self.crear_conexion()
        if conexion:
            try:
                c = conexion.cursor()
                c.execute("SELECT stock FROM inventario WHERE nombre = %s", (nombre_producto,))
                stock = c.fetchone
                if stock and stock[0] >= cantidad:
                    return True
                return False
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error al verificar el stock: {e}")
            finally:
                conexion.close()     