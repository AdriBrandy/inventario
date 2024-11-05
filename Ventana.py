
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from inventario import *

class Ventana(Frame):
    data=inventario()

    def __init__(self, master=None):
        super().__init__(master,width=1100, height=730)
        self.master=master
        self.pack()
        self.create_widgets()
        self.llenaDatos()
        self.habilitarCajasTexto("disabled")
        self.habilitarBotonesOperaciones("normal")
        self.habilitarBotonesSave("disabled")
        self.ID=-1

    def habilitarBotonesOperaciones(self,estado):
        self.btnNew.configure(state=estado)
        self.btnModify.configure(state=estado)
        self.btnDelete.configure(state=estado)

    def habilitarBotonesSave(self,estado):
        self.btnSave.configure(state=estado)
        self.btnCancel.configure(state=estado)

    def habilitarBotonesCancel(self,estado):
        self.btnSave.configure(state=estado)
        self.btnCancel.configure(state=estado)

    def habilitarCajasTexto(self,estado):
        self.txtPRODUCT.configure(state=estado)
        self.txtCATEGORY.configure(state=estado)
        self.txtQUANTITY.configure(state=estado)
        self.txtPRICE.configure(state=estado)
        self.txtCOLOR.configure(state=estado)
        self.txtCOST.configure(state=estado)
        self.txtBRAND.configure(state=estado)

    def limpiarCajas(self):
        self.txtPRODUCT.delete(0,END)
        self.txtCATEGORY.delete(0,END)
        self.txtQUANTITY.delete(0,END)
        self.txtPRICE.delete(0,END)
        self.txtCOLOR.delete(0,END)
        self.txtCOST.delete(0,END)
        self.txtBRAND.delete(0,END)
        self.txtPRODUCT2.delete(0,END)
        self.txtPRODUCT3.delete(0,END)
        self.txtMARCA.delete(0,END)

    def llenaDatos(self):
        datos = self.data.consulta_productos()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7]))

        if len(self.grid.get_children())>0: 
            self.grid.selection_set(self.grid.get_children()[0]) #SELECCIONAR EL PRIMER REGISTRO

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
    
    def fAtras(self):
        self.limpiaGrid()
        self.llenaDatos()
        self.limpiarCajas()
        self.habilitarBotonesSave("disabled")
        self.habilitarBotonesOperaciones("normal")
        self.limpiarCajas()
        self.habilitarCajasTexto("disabled")
    
    def fSearch(self):
        buscar = self.txtPRODUCT2.get()
        if buscar:
            s = 'WHERE PRODUCTO = "{}"'.format(buscar)
            datos = self.data.buscar_productos(s)
            self.limpiaGrid()
            self.limpiarCajas()
            for row in datos:
                self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                
            if not datos:
                messagebox.showinfo("Buscar", "No se encontraron productos con ese nombre.")
        else:
            messagebox.showwarning("Buscar", "Por favor ingresa un producto para buscar.")
    
    def fSearchLabel(self):
        producto = self.txtPRODUCT3.get()
        marca=self.txtMARCA.get()
        if True:
            s = 'WHERE PRODUCTO = "{}" and MARCA="{}"'.format(producto,marca)
            datos = self.data.buscar_productoymarca(s)
            self.limpiaGrid()
            self.limpiarCajas()
            for row in datos:
                self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                
                if not datos:
                    messagebox.showinfo("Buscar", "No se encontraron productos con ese nombre.")
    
    def fNew(self):
        self.habilitarCajasTexto("normal")
        self.habilitarBotonesCancel("normal")
        self.limpiarCajas()
        self.txtPRODUCT.focus()

    def fSave(self):
        if self.ID==-1:
            self.data.inserta_producto(self.txtPRODUCT.get(),self.txtCATEGORY.get(),self.txtQUANTITY.get(),self.txtPRICE.get(),self.txtCOLOR.get(),self.txtCOST.get(),self.txtBRAND.get())
            messagebox.showinfo("Guardar", "Registro guardado correctamente")
        else:
            self.data.modifica_producto(self.ID,self.txtPRODUCT.get(),self.txtCATEGORY.get(),self.txtQUANTITY.get(),self.txtPRICE.get(),self.txtCOLOR.get(),self.txtCOST.get(),self.txtBRAND.get())
            messagebox.showinfo("Modificar", "Registro modificado correctamente")
            self.ID=-1
        
        self.limpiaGrid()
        self.llenaDatos()
        self.limpiarCajas()
        self.habilitarBotonesSave("disabled")
        self.habilitarBotonesOperaciones("normal")
        self.limpiarCajas()
        self.habilitarCajasTexto("disabled")

    def fModify(self):
        selected=self.grid.focus()
        clave=self.grid.item(selected,'text')
        if clave=="":
            messagebox.showwarning("Modificar","Selecciona elemento a eliminar")
        else:
            self.ID=clave
            self.habilitarCajasTexto("normal")
            valores=self.grid.item(selected,'values')
            self.limpiarCajas()
            self.txtPRODUCT.insert(0,valores[0])
            self.txtCATEGORY.insert(0,valores[1])
            self.txtQUANTITY.insert(0,valores[2])
            self.txtPRICE.insert(0,valores[3])
            self.txtCOLOR.insert(0,valores[4])
            self.txtCOST.insert(0,valores[5])
            self.txtBRAND.insert(0,valores[6])
            self.habilitarBotonesOperaciones("disabled")
            self.habilitarBotonesCancel("normal")
            self.txtPRODUCT.focus()
    
    def fDelete(self):
        selected=self.grid.focus()
        clave=self.grid.item(selected,'text')
        if clave=="":
            messagebox.showwarning("Eliminar","Selecciona elemento a eliminar")
        else:
            valores=self.grid.item(selected,'values')
            campo=str(clave)+"  " + valores[0] +"  "+valores[6] #ID PRODUCTO Y MARCA
            respuesta=messagebox.askquestion("Eliminar","¿Desea eliminar registro seleccionado?\n" + campo)
            if respuesta==messagebox.YES:
                r=self.data.elimina_producto(clave)
                if r==1:
                    messagebox.showinfo("Eliminar", "Registro eliminado correctamente")
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", "No fue posible eliminar registro")    
    
    def fCancel(self):
        respuesta=messagebox.askquestion("Cancelar","¿Estas seguro que desea cancelar?")
        if respuesta==messagebox.YES:
            self.limpiarCajas()
            self.habilitarBotonesSave("disabled")
            self.habilitarBotonesOperaciones("normal")
            self.habilitarCajasTexto("disabled")
    
    def create_widgets(self):
        # -----------------------------------------POSICIONES Y COLORES DE FRAMES---------------------------------------------
        # --------------------------------------------------------------------------------------------------------------------

        frame1=Frame(self, bg="#A3EDAF") #CUADRADO SUPERIOR IZQUIERDO BOTONES
        frame1.place(x=0, y=0, width=200, height=150)
        frame2=Frame(self, bg="#BAF8C7") #SUPERIOR LOGO
        frame2.place(x=200, y=0, width=900, height=150)
        frame3=Frame(self, bg="#BAF8C7") #IZQUIERDA DATOS
        frame3.place(x=0,y=150,width=200,height=580)
        frame4=Frame(self, bg="#E1FCE9") #BODY CONSULTAS
        frame4.place(x=200,y=150,width=900,height=580)

        # --------------------------------------------BOTON BUSCAR PRODUCTO----------------------------------------------------
        # ------------------------------CONSTRUCCION Y POSICION----------------------------------------------------------------

        label9=Label(frame2,text="PRODUCTO: ",font=("Comic Sans",12))
        label9.place(x=10,y=50)
        self.txtPRODUCT2=Entry(frame2)
        self.txtPRODUCT2.place(x=10,y=80,width=180, height=20)

        # --------------------BOTONES BUSCAR Y ATRAS  PARA BUSCAR POR PRODUCTO-----------------------------------------------
        # --------------------CONSTRUCCION Y POSICION------------------------------------------------------------------------

        self.btnSearch=Button(frame2,text="Buscar",command=self.fSearch, bg="#E1FCE9", fg="black", font=10)
        self.btnSearch.place(x=200,y=75,width=100,height=30)
        self.btnBack=Button(frame2,text="Atrás",command=self.fAtras, bg="#E1FCE9", fg="black",font=10)
        self.btnBack.place(x=310,y=75,width=100,height=30)

        # --------------------------------------------BOTON BUSCAR PRODUCTO por marca------------------------------------------
        # ------------------------------CONSTRUCCION Y POSICION----------------------------------------------------------------

        label10=Label(frame2,text="PRODUCTO: ",font=("Comic Sans",12))
        label10.place(x=450,y=50)
        label11=Label(frame2,text="MARCA: ",font=("Comic Sans",12))
        label11.place(x=480,y=80)

        self.txtPRODUCT3=Entry(frame2)
        self.txtPRODUCT3.place(x=570,y=50,width=180, height=20)
        self.txtMARCA=Entry(frame2)
        self.txtMARCA.place(x=570,y=80,width=180, height=20)

        # --------------------BOTONES BUSCAR Y ATRAS  PARA FILTRAR POR PRODUCTO Y POR MARCA----------------------------------
        # --------------------CONSTRUCCION Y POSICION------------------------------------------------------------------------

        self.btnSearchLabel=Button(frame2,text="Buscar",command=self.fSearchLabel, bg="#E1FCE9", fg="black", font=10)
        self.btnSearchLabel.place(x=775,y=40,width=100,height=30)
        self.btnBack=Button(frame2,text="Atrás",command=self.fAtras, bg="#E1FCE9", fg="black",font=10)
        self.btnBack.place(x=775,y=80,width=100,height=30)


        # -------------------------------------------------BOTONES NUEVO, CAMBIAR, BORRAR-------------------------------------
        # --------------------CONSTRUCCION Y POSICION-------------------------------------------------------------------------

        self.btnNew=Button(frame1,text="NUEVO",command=self.fNew, bg="#E1FCE9", fg="black", font=10)
        self.btnNew.place(x=50,y=20,width=100,height=30)

        self.btnModify=Button(frame1,text="CAMBIAR",command=self.fModify, bg="#E1FCE9", fg="black", font=10)
        self.btnModify.place(x=50,y=60,width=100,height=30)

        self.btnDelete=Button(frame1,text="BORRAR",command=self.fDelete, bg="#E1FCE9", fg="black", font=10)
        self.btnDelete.place(x=50,y=100,width=100,height=30)

        # -----------------------------------------------LABELS Y HOLDERS INPUT------------------------------------------------------
        # -------------------CONSTRUCCION Y POSICIONAMIENTO--------------------------------------------------------------------------

        label2=Label(frame3,text="PRODUCTO: ",font=("Comic Sans",12))
        label2.place(x=10,y=50)
        self.txtPRODUCT=Entry(frame3)
        self.txtPRODUCT.place(x=10,y=80,width=180, height=20)

        label3=Label(frame3,text="LÍNEA: ",font=("Comic Sans",12))
        label3.place(x=10,y=110)
        self.txtCATEGORY=Entry(frame3)
        self.txtCATEGORY.place(x=10,y=140,width=180, height=20)

        label4=Label(frame3,text="CANTIDAD: ",font=("Comic Sans",12))
        label4.place(x=10,y=170)
        self.txtQUANTITY=Entry(frame3)
        self.txtQUANTITY.place(x=10,y=200,width=180, height=20)

        label5=Label(frame3,text="PRECIO: ",font=("Comic Sans",12))
        label5.place(x=10,y=230)
        self.txtPRICE=Entry(frame3)
        self.txtPRICE.place(x=10,y=260,width=180, height=20)

        label6=Label(frame3,text="COLOR: ",font=("Comic Sans",12))
        label6.place(x=10,y=290)
        self.txtCOLOR=Entry(frame3)
        self.txtCOLOR.place(x=10,y=320,width=180, height=20)

        label7=Label(frame3,text="COSTO: ",font=("Comic Sans",12))
        label7.place(x=10,y=350)
        self.txtCOST=Entry(frame3)
        self.txtCOST.place(x=10,y=380,width=180, height=20)

        label8=Label(frame3,text="MARCA: ",font=("Comic Sans",12))
        label8.place(x=10,y=410)
        self.txtBRAND=Entry(frame3)
        self.txtBRAND.place(x=10,y=440,width=180, height=20)
        
        # ------------------------------------------------------BOTONES GUARDAR Y CANCELAR-------------------------------------------------
        #--------- ------------------------------------------------------PARA LOS REGISTROS------------------------------------------------

        self.btnSave=Button(frame3,text="GUARDAR",command=self.fSave, bg="#E1FCE9", fg="black", font=10)
        self.btnSave.place(x=40,y=480,width=120,height=30)
        self.btnCancel=Button(frame3,text="CANCELAR",command=self.fCancel, bg="#E1FCE9", fg="black", font=10)
        self.btnCancel.place(x=40,y=520,width=120,height=30)

        # --------------------------------------------------------------VISUALIZACION GRILLA------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------

        self.grid=ttk.Treeview(frame4, columns=("col1","col2","col3","col4","col5","col6","col7"))

        # -------------------------------------------------------DEFINICION DE LA GRILLA (COLUMNAS)-----------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------

        self.grid.column("#0",width=50)
        self.grid.column("col1", width=140,anchor=CENTER)
        self.grid.column("col2", width=120,anchor=CENTER)
        self.grid.column("col3", width=120,anchor=CENTER)
        self.grid.column("col4", width=120,anchor=CENTER)
        self.grid.column("col5", width=120,anchor=CENTER)
        self.grid.column("col6", width=120,anchor=CENTER)
        self.grid.column("col7", width=90,anchor=CENTER)

        #--------------- DEFINICION DE LOS NOMBRES DE LAS COLUMNAS---------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------------------------------------

        self.grid.heading("#0", text="ID",anchor=CENTER)
        self.grid.heading("col1", text="PRODUCTO",anchor=CENTER)
        self.grid.heading("col2", text="LINEA",anchor=CENTER)
        self.grid.heading("col3", text="CANTIDAD",anchor=CENTER)
        self.grid.heading("col4", text="PRECIO_UNITARIO",anchor=CENTER)
        self.grid.heading("col5", text="COLOR",anchor=CENTER)
        self.grid.heading("col6", text="COSTO_UNITARIO",anchor=CENTER)
        self.grid.heading("col7", text="MARCA",anchor=CENTER)

        # ---------------DEFINICION DE SCROLLBAR-----------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------------------------------
        
        self.grid.pack(side=LEFT, fill=Y)
        sb=Scrollbar(frame4, orient=VERTICAL)
        sb.pack(side=RIGHT,fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'