import pymysql
# import pandas as pd

class inventario:

    # def __init__(self):
    #   self.cnn = pymysql.connect(host="localhost", user="root", passwd="greenday22", database="tp_laboratorio_bdd") #LOCAL ADRI
   
    def __init__(self):
       self.cnn = pymysql.connect(host="localhost", user="root", passwd="Root123?", database="TP_LABORATORIO_BDD") #LOCAL ARA
   
    def __str__(self):
        datos=self.consulta_productos()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_productos(self):
        cur = self.cnn.cursor()
        sql="SELECT ID, PRODUCTO, Descripcion_linea_productos, CANTIDAD, PRECIO_UNITARIO, COLOR, COSTO_UNITARIO, Descripcion_Marcas FROM productos P LEFT JOIN linea_productos L on P.ID_LINEA_PRODUCTO_FK=L.ID_linea_productos_PK left join marcas M on P.ID_MARCAS_FK=M.ID_Marcas_PK;"
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_productos(self, WHERE=""):
        cur = self.cnn.cursor()
        sql="SELECT ID, PRODUCTO, Descripcion_linea_productos, CANTIDAD, PRECIO_UNITARIO, COLOR, COSTO_UNITARIO, Descripcion_Marcas FROM productos P LEFT JOIN linea_productos L on P.ID_LINEA_PRODUCTO_FK=L.ID_linea_productos_PK left join marcas M on P.ID_MARCAS_FK=M.ID_Marcas_PK {}".format((WHERE)).upper()
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def buscar_productoymarca(self, WHERE=""):
        cur = self.cnn.cursor()
        sql="SELECT ID, PRODUCTO, Descripcion_linea_productos, CANTIDAD, PRECIO_UNITARIO, COLOR, COSTO_UNITARIO, Descripcion_Marcas FROM productos P LEFT JOIN linea_productos L on P.ID_LINEA_PRODUCTO_FK=L.ID_linea_productos_PK left join marcas M on P.ID_MARCAS_FK=M.ID_Marcas_PK {}".format((WHERE)).upper()
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def inserta_producto(self,PRODUCT,CATEGORY,QUANTITY,PRICE,COLOR,COST,BRAND): #------------REVISAR
        cur = self.cnn.cursor()
        sql='''INSERT INTO productos (PRODUCTO,LINEA,CANTIDAD,PRECIO_UNITARIO,COLOR,COSTO_UNITARIO,MARCA) 
        VALUES('{}','{}','{}','{}', '{}', '{}', '{}')'''.format(PRODUCT.upper(),CATEGORY.upper(),QUANTITY,PRICE,COLOR.upper(),COST,BRAND.upper())
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_producto(self,ID): #------------REVISAR
        cur = self.cnn.cursor()
        sql='''DELETE FROM productos WHERE ID = {}'''.format(ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_producto(self,ID,PRODUCTO,LINEA,CANTIDAD,PRECIO_UNITARIO,COLOR,COSTO_UNITARIO,MARCA): #------------REVISAR
        cur = self.cnn.cursor()
        sql='''UPDATE productos SET PRODUCTO='{}', LINEA='{}', CANTIDAD='{}',
        PRECIO_UNITARIO='{}', COLOR='{}', COSTO_UNITARIO='{}', MARCA='{}' WHERE ID={}'''.format(PRODUCTO.upper(),LINEA.upper(),CANTIDAD,PRECIO_UNITARIO,COLOR.upper(),COSTO_UNITARIO,MARCA.upper(), ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n

    # def consulta_productos_combinados(self):
    #     try:
    #         cur = self.cnn.cursor()
    #         query = """
    #         SELECT 
    #             p.ID, 
    #             p.PRODUCTO, 
    #             l.Descripcion_linea_productos,
    #             p.CANTIDAD, 
    #             p.PRECIO_UNITARIO, 
    #             p.COSTO_UNITARIO, 
    #             p.COLOR, 
    #             m.Descripcion_Marcas 
    #         FROM 
    #             productos p
    #         JOIN 
    #             marcas m ON p.ID_MARCAS_FK = m.ID_Marcas_PK
    #         JOIN 
    #             linea_productos l ON p.ID_LINEA_PRODUCTO_FK = l.ID_linea_productos_PK;
    #         """
    #         cur.execute(query)
    #         datos = cur.fetchall()
    #         cur.close()
    #         return datos
    #     except pymysql.MySQLError as e:
    #         print(f"Error al consultar productos combinados: {e}")
    #         return []