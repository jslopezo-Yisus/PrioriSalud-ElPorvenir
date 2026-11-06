# Datos académicos simulados del caso El Porvenir.
# Las puntuaciones de ejemplo son demostrativas y deben ser validadas por el equipo.

PROBLEMS = [
    {
        "id": "materno",
        "name": "Atención materno-infantil rural",
        "description": "Barreras para el inicio oportuno del control prenatal y la vacunación completa en menores de cinco años.",
        "evidence": "21% de menores de cinco años con esquema de vacunación incompleto, según la base municipal depurada del caso.",
        "status": "Prioridad identificada en fases anteriores"
    },
    {
        "id": "agua",
        "name": "Acceso continuo a agua segura",
        "description": "Hogares rurales sin acceso continuo a agua segura y posible relación con eventos gastrointestinales.",
        "evidence": "29% de hogares rurales sin agua segura continua. La relación con enfermedad gastrointestinal es una hipótesis por validar.",
        "status": "Brecha territorial por profundizar"
    },
    {
        "id": "acceso",
        "name": "Barreras geográficas y económicas de acceso",
        "description": "Distancias, tiempos de desplazamiento y costos de transporte que dificultan el acceso a servicios.",
        "evidence": "Desplazamientos estimados de 90 minutos a 3 horas desde veredas dispersas.",
        "status": "Determinante transversal"
    },
    {
        "id": "participacion",
        "name": "Participación y articulación comunitaria",
        "description": "Necesidad de fortalecer la participación comunitaria y la coordinación territorial para identificar barreras.",
        "evidence": "Vacío de información sobre razones de inasistencia, diferencias entre veredas y necesidades diferenciales.",
        "status": "Vacío de información y gobernanza"
    }
]

TECHNICAL_CRITERIA = [
    {"id": "magnitude", "name": "Magnitud", "weight": 25, "description": "Tamaño o extensión del problema."},
    {"id": "severity", "name": "Trascendencia / severidad", "weight": 25, "description": "Consecuencias sobre la salud y el bienestar."},
    {"id": "equity", "name": "Vulnerabilidad e inequidad", "weight": 20, "description": "Afectación diferencial de población rural y grupos con barreras."},
    {"id": "feasibility", "name": "Viabilidad técnica y política", "weight": 15, "description": "Posibilidad institucional y operativa de intervenir."},
    {"id": "resources", "name": "Recursos y costo-efectividad", "weight": 15, "description": "Disponibilidad y uso razonable de recursos."}
]

# Calificaciones de demostración en escala 1-5. Sustituir por la matriz aprobada por el equipo.
TECHNICAL_SCORES = {
    "materno": [5, 5, 5, 4, 3],
    "agua": [3, 4, 4, 3, 3],
    "acceso": [4, 4, 5, 3, 3],
    "participacion": [3, 3, 4, 4, 4]
}

COMMUNITY_SCORES = {
    "materno": 4.5,
    "agua": 4.0,
    "acceso": 4.7,
    "participacion": 3.8
}

def technical_results():
    results = []
    for problem in PROBLEMS:
        scores = TECHNICAL_SCORES[problem["id"]]
        total = sum(score * criterion["weight"] for score, criterion in zip(scores, TECHNICAL_CRITERIA)) / 100
        results.append({**problem, "score": round(total, 2)})
    return sorted(results, key=lambda item: item["score"], reverse=True)

def community_results():
    return sorted(
        [{**p, "score": COMMUNITY_SCORES.get(p["id"], 0)} for p in PROBLEMS],
        key=lambda item: item["score"],
        reverse=True
    )
