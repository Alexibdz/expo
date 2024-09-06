from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

            
class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        def crear_conexion():
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
        self.pack()
        self.conexion = crear_conexion()
        self.cursor = self.conexion.cursor()
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

        btn_agregar = tk.Button(lbl_frame, text="Agregar",  bg="#dddddd", font="sans 14 bold", command=self.registrar)        
        btn_agregar.place(x=80, y=340, width=240, height=40)

        btn_editar = tk.Button(lbl_frame, text="Editar",  bg="#dddddd", font="sans 14 bold", command=self.editar_producto)        
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
        self.tree.heading("PRODUCTO", text="Producto")
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

        self.mostrar()

        btn_actualizar = Button(frame2, text="Actualizar Inventario", font="sans 14 bold", command=self.actualizar_inventario)
        btn_actualizar.place(x=440, y=480, width=260, height=50)

        btn_borrar = Button(frame2, text="Borrar Item", font="sans 14 bold", command=self.borrar_seleccion)
        btn_borrar.place(x=740, y=480, width=260, height=50)


    def eje_consulta(self, consulta, parametros=()):
        if self.conexion is not None:
            try:
                cursor = self.conexion.cursor()  # Crear el cursor de la conexión MySQL
                cursor.execute(consulta, parametros)  # Ejecutar la consulta con parámetros
                resultado = cursor.fetchall()  # Leer todos los resultados
                self.conexion.commit()  # Confirmar los cambios en la base de datos
                return resultado  # Devolver los resultados si los hay
            except Error as e:
                messagebox.showerror("Error en la consulta", f"Error al ejecutar la consulta: {e}")
            finally:
                cursor.close()  # Cerrar el cursor después de la operación
        else:
            messagebox.showerror("Error de conexión", "No hay conexión a la base de datos.")
            return None

        
    def validacion(self, nombre, proveedor, precio, costo, stock):
        if not (nombre and proveedor and precio and costo and stock):
            return False
        try:
            float(precio)
            float(costo)
            int(stock)
        except ValueError:
            return False
        return True
    
    def mostrar(self):
        consulta = "SELECT * FROM inventario ORDER BY id DESC"
        resultado = self.eje_consulta(consulta)
        for elemento in resultado:
            try:
                precio_arg = "{:,.0f} ARG ".format(float(elemento[3])) if elemento[3] else ""
                costo_arg =  "{:,.0f} ARG".format(float(elemento[4])) if elemento[4] else ""
            except ValueError:
                precio_arg = elemento[3]
                costo_arg = elemento[4]
            self.tree.insert("", 0, text=elemento[0], values=(elemento[0], elemento[1], elemento[2],
                                                              precio_arg, costo_arg, elemento[5]))

    def actualizar_inventario(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.mostrar()

        messagebox.showinfo("Actualizacion", "El inventario se actualizo correctamente.")

    def registrar(self):
        # Limpiar el árbol de datos actual
        result = self.tree.get_children()
        for pos in result:
            self.tree.delete(pos)
        
        # Obtener los datos de las entradas
        nombre = self.entry_nombre.get()
        prov = self.entry_proveedor.get()
        precio = self.entry_precio.get()
        costo = self.entry_costo.get()
        stock = self.entry_stock.get()

        # Validar los campos antes de intentar registrar
        if self.validacion(nombre, prov, precio, costo, stock):
            try:
                # Crear la consulta SQL con marcadores de posición para MySQL (%s)
                consulta = "INSERT INTO inventario (id, nombre, proveedor, precio, costo, stock) VALUES (%s, %s, %s, %s, %s, %s)"
                parametros = (None, nombre, prov, precio, costo, stock)

                # Ejecutar la consulta
                self.eje_consulta(consulta, parametros)
                
                # Limpiar los campos de entrada
                self.entry_nombre.delete(0, END)
                self.entry_proveedor.delete(0, END)
                self.entry_precio.delete(0, END)
                self.entry_costo.delete(0, END)
                self.entry_stock.delete(0, END)
                
                # Mostrar el contenido actualizado en el árbol
                self.mostrar()
            except Exception as e:
                messagebox.showwarning(title="Error", message=f"Error al registrar el producto: {e}")
        else:
            # Si la validación falla, muestra un mensaje de advertencia
            messagebox.showwarning(title="Error", message="Rellene todos los campos correctamente")
            self.mostrar()
    
    def editar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Editar Producto", "Seleccione un producto para editar.")
            return

        item_id = self.tree.item(seleccion)["text"]
        item_values = self.tree.item(seleccion)["values"]

        ventana_editar = Toplevel(self)
        ventana_editar.title("Editar producto")
        ventana_editar.geometry("400x400")
        ventana_editar.config(bg="#C6D9E3")

        lbl_nombre = Label(ventana_editar, text="Nombre", font="sans 14 bold", bg="#C6D9E3")
        lbl_nombre.grid(row=0, column=0, padx=10, pady=10)
        entry_nombre = Entry(ventana_editar, font="sans 14 bold")
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        entry_nombre.insert(0, item_values[1])

        lbl_proveedor = Label(ventana_editar, text="Proveedor:", font="sans 14 bold", bg="#C6D9E3")
        lbl_proveedor.grid(row=1, column=0, padx=10, pady=10)
        entry_proveedor = Entry(ventana_editar, font="sans 14 bold")
        entry_proveedor.grid(row=1, column=1, padx=10, pady=10)
        entry_proveedor.insert(0, item_values[2])
        
        lbl_precio = Label(ventana_editar, text="Precio:", font="sans 14 bold", bg="#C6D9E3")
        lbl_precio.grid(row=2, column=0, padx=10, pady=10)
        entry_precio = Entry(ventana_editar, font="sans 14 bold")
        entry_precio.grid(row=2, column=1, padx=10, pady=10)
        entry_precio.insert(0, item_values[3].split()[0].replace(",", ""))

        lbl_costo = Label(ventana_editar, text="Costo:", font="sans 14 bold", bg="#C6D9E3")
        lbl_costo.grid(row=3, column=0, padx=10, pady=10)
        entry_costo = Entry(ventana_editar, font="sans 14 bold")
        entry_costo.grid(row=3, column=1, padx=10, pady=10)
        entry_costo.insert(0, item_values[4].split()[0].replace(",", ""))

        lbl_stock = Label(ventana_editar, text="Stock:", font="sans 14 bold", bg="#C6D9E3")
        lbl_stock.grid(row=4, column=0, padx=10, pady=10)
        entry_stock = Entry(ventana_editar, font="sans 14 bold")
        entry_stock.grid(row=4, column=1, padx=10, pady=10)
        entry_stock.insert(0, item_values[5])
        
        def guardar_cambios():
            nombre = entry_nombre.get()
            proveedor = entry_proveedor.get()
            precio = entry_precio.get()
            costo = entry_costo.get()
            stock = entry_stock.get()

            if not (nombre and proveedor and precio and costo and stock):
                messagebox.showwarning("Guardar cambios", "Rellene todos los campos.")
                return
            
            try:
                precio = float(precio.replace(",",""))
                costo =  float(costo.replace(",",""))
            except ValueError:
                messagebox.showwarning("Guardar cambios", "Ingrese valores numericos validos para precio y/o costo.")
                return
            
            consulta = """UPDATE inventario
              SET nombre=%s, proveedor=%s, precio=%s, costo=%s, stock=%s
              WHERE id=%s"""
            parametros = (nombre, proveedor, precio, costo, stock, item_id)

            self.eje_consulta(consulta, parametros)
            self.actualizar_inventario()

            ventana_editar.destroy()

            
        
        btn_guardar = Button(ventana_editar, text="Guardar cambios", font="sans 14 bold", command=guardar_cambios)
        btn_guardar.place(x=80, y=250, width=240, height=40)

    def borrar_seleccion(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Borrar Producto", "Seleccione un producto para borrar.")
            return

        item_id = self.tree.item(seleccion)["text"]
        
        confirmacion = messagebox.askyesno("Confirmar Borrado", "¿Está seguro de que desea borrar este producto?")
        if not confirmacion:
            return

        # Consulta SQL para eliminar el ítem seleccionado
        consulta = "DELETE FROM inventario WHERE id=%s"
        parametros = (item_id,)

        try:
            self.eje_consulta(consulta, parametros)
            self.actualizar_inventario()
            messagebox.showinfo("Borrado exitoso", "El producto ha sido borrado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al borrar el producto: {e}")



