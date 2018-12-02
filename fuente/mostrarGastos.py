import sqlite3 
from configW import __database

def getGastosMensuales(mes):

  tipoCategoria = []
  miDB = sqlite3.connect(__database)
  c = miDB.cursor()

  for row in c.execute('select * from Tipo_Categoria'):
    identificador = int(row[0])
    descripcion = str(row[1])

    tuplear = [identificador, descripcion]
    tipoCategoria.append(tuplear)

  if mes == 12:
    ano = 8
  else:
    ano = 9

  sentencia1 = 'select ID, Descripcion, Importe, Fecha, ID_TipoCategoria from Movimiento where fecha between "201{0}-{1}-01" and "201{0}-{1}-31" and ID_TipoCategoria !=0 order by ID_TipoCategoria'.format(ano, mes)

  losGastos = []

  for row in c.execute(sentencia1):
    identificador = str(row[0])
    descripcion = str(row[1])
    importe = float(row[2])
    fecha = str(row[3])
    idTipoCategoria = int(row[4])
    
    lista = [identificador, descripcion, importe, fecha, idTipoCategoria]
    losGastos.append(lista)
        


  sentencia2 = 'select sum(Importe) from Movimiento where fecha between "201{0}-{1}-01" and "201{0}-{1}-31" group by ID_Categoria'.format(ano, mes)


  sumaGastos = []
  for row in c.execute(sentencia2):
    sumaGastosMios = float(row[0])

    sumaGastos.append(sumaGastosMios)

   
  sentencia3 = 'select sum(Importe) from Movimiento group by ID_Categoria'

  sumaGastosTotales = []
  for row in c.execute(sentencia3):
    sumaGastosMiosTotales = float(row[0])

    sumaGastosTotales.append(sumaGastosMiosTotales)








 
  gastosYCategorias = [mes, tipoCategoria, losGastos, sumaGastos, sumaGastosTotales]

#  print gastosYCategorias[1][0] se muestran todos los ides de categoria 
#  print gastosYCategorias[1][1] se muestran todos los tipoCategoria
#  print gastosYCategorias[1][1][1] se muestra ropa invierno
#  print gastosYCategorias[0] se muestra mes
#  print gastosYCategorias[2][1] se muestra la primera fila de los gastos
#  print gastosYCategorias[2][2] se muestra la segunda fila de los gastos
#  print gastosYCategorias[2][1][0] se muestra el id de la primera fila

  
  return gastosYCategorias


