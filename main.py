from flask import Flask, render_template, request, redirect
from fuente.getTipo import getTipoCategoria
from fuente.cargar import cargarTransaccion
from fuente.funciones import sacarMes
from fuente.mostrarGastos import getGastosMensuales

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def funcion1():
  if request.method == 'POST':
    if request.form['opcion'] == 'Cargar movimiento':
      return redirect('/cargarMovimiento')
    elif request.form['opcion'] == 'Mostrar gastos por mes':
      return redirect('/elegirMes')
  elif request.method == 'GET':
    return render_template("index.html")

@app.route("/cargarMovimiento", methods=['GET', 'POST'])
def funcion2():
  if request.method == 'POST':
    if request.form['cargar'] == 'Aceptar':
      cargarTransaccion(request.form)
    return redirect("/")
  elif request.method == 'GET':
    return render_template("cargarMovimiento.html", returning = getTipoCategoria())

@app.route("/elegirMes", methods=['GET', 'POST'])
def funcion3():
  if request.method == 'POST':
    if request.form['cargar'] == 'Mostrar gastos':
      return redirect("/gastosMes/{0}".format(sacarMes(request.form)))
    elif request.form['cargar'] == 'Volver a inicio':
      return redirect('/')
  elif request.method == 'GET':
    return render_template("elegirMes.html")

@app.route("/gastosMes/<int:elMes>", methods=['GET', 'POST'])
def funcion4(elMes):
  if request.method == 'POST':
    if request.form['opcion'] == 'Volver a Inicio':
      return redirect("/")
  elif request.method == 'GET':
    return render_template("gastosPorMes.html", returning = getGastosMensuales(elMes))

if __name__=='__main__':
  app.run(host='0.0.0.0')

