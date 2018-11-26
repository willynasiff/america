import sqlite3 
from configW import __database

def getTipoCategoria(): 

  tipoCategoria = [] 
  

  miDB = sqlite3.connect(__database)
  c = miDB.cursor()

  for row in c.execute('select * from Tipo_Categoria'):
    iden = str(row[0])
    desc = str(row[1])

    idDesc = iden + '-  ' + desc 

    tipoCategoria.append(idDesc)
 

  miDB.commit()
  miDB.close()


  return tipoCategoria 

