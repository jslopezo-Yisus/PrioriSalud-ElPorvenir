from flask import Blueprint, render_template
from .data import (
    PROBLEMS, TECHNICAL_CRITERIA, COMMUNITY_CRITERIA,
    technical_results, community_results, integrated_results,
    VERSION_HISTORY, PILOT_CHECKS, NEXT_ITERATION, ACTORS,
    DELIBERATION_RULES, INTEGRATION_WEIGHTS, MUNICIPAL_CONTEXT,
    ACTION_PLAN, ACTION_INDICATORS, RESOURCE_AREAS, RISK_CONTROLS,
)

main = Blueprint("main", __name__)


@main.route("/")
def dashboard():
    return render_template(
        "dashboard.html", problems=PROBLEMS,
        technical=technical_results(), integrated=integrated_results(),
        context=MUNICIPAL_CONTEXT,
    )


@main.route("/evaluacion-tecnica")
def evaluacion_tecnica():
    return render_template(
        "evaluacion_tecnica.html", problems=PROBLEMS,
        criteria=TECHNICAL_CRITERIA, results=technical_results(),
    )


@main.route("/participacion")
def participacion():
    return render_template(
        "participacion.html", criteria=COMMUNITY_CRITERIA,
        results=community_results(), actors=ACTORS,
        rules=DELIBERATION_RULES,
    )


@main.route("/resultados")
def resultados():
    return render_template(
        "resultados.html", technical=technical_results(),
        community=community_results(), integrated=integrated_results(),
        weights=INTEGRATION_WEIGHTS,
    )


@main.route("/ruta-accion")
def ruta_accion():
    priority = integrated_results()[0]
    return render_template(
        "ruta_accion.html", priority=priority, phases=ACTION_PLAN,
        indicators=ACTION_INDICATORS, resources=RESOURCE_AREAS,
        risks=RISK_CONTROLS,
    )


@main.route("/versiones")
def versiones():
    return render_template(
        "versiones.html", versions=VERSION_HISTORY,
        pilot_checks=PILOT_CHECKS, next_iteration=NEXT_ITERATION,
    )
