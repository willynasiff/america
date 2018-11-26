import time

def sacarNumero(lista):
  numero = ''
  lista = lista[0:2]
  for index in lista:
    if index.isdigit():
      numero = numero + index

  return int(numero)

def sacarFecha():
  year = str(time.localtime()[0])
  month = str(time.localtime()[1])
  day = str(time.localtime()[2])

  if (len(month) == 1):
    month = "0" + month
  if (len(day) == 1):
    day = '0' + day

  return '{}-{}-{}'.format(year, month, day)

def sacarMes(requestMes):
  mes = int(sacarNumero(requestMes['meses']))

  return mes
