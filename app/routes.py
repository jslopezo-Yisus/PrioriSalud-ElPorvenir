from flask import Blueprint, render_template
from .data import PROBLEMS, TECHNICAL_CRITERIA, technical_results, community_results

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    return render_template("dashboard.html", problems=PROBLEMS, technical=technical_results())

@main.route("/evaluacion-tecnica")
def evaluacion_tecnica():
    return render_template("evaluacion_tecnica.html", problems=PROBLEMS, criteria=TECHNICAL_CRITERIA, results=technical_results())

@main.route("/participacion")
def participacion():
    return render_template("participacion.html", problems=PROBLEMS, results=community_results())

@main.route("/resultados")
def resultados():
    return render_template("resultados.html", technical=technical_results(), community=community_results())

@main.route("/ruta-accion")
def ruta_accion():
    return render_template("ruta_accion.html")

@main.route("/versiones")
def versiones():
    return render_template("versiones.html")
