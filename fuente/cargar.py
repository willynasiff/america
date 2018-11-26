import sqlite3 
from configW import __database
from funciones import sacarNumero, sacarFecha

def cargarTransaccion(requestCompra):

  idTipoCategoria = sacarNumero(requestCompra['tipoGasto'])
  categoria = int(requestCompra['categoria'])
  importe = float(requestCompra['importe'])
  descripcion = requestCompra['descripcion']
  fecha = sacarFecha()
  
  if categoria == 4 or categoria == 1 or categoria == 2:
    idTipoCategoria = 0
 


  escribir = [importe, descripcion, categoria, idTipoCategoria, fecha]
  


  miDB = sqlite3.connect(__database)
  c = miDB.cursor()
  c.execute("insert into Movimiento (Importe, Descripcion, ID_Categoria, ID_TipoCategoria, Fecha) values (?,?,?,?,?)", escribir)
  miDB.commit()
  miDB.close()
  





