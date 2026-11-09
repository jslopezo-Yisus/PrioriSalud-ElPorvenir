# PrioriSalud El Porvenir
# Datos académicos simulados. No representan mediciones ni consultas reales.

MUNICIPAL_CONTEXT = {
    "population": 48600,
    "rural_share": 39,
    "rural_veredas": 18,
    "children_vaccination_incomplete": 21,
    "rural_households_without_safe_water": 29,
    "travel_min_minutes": 90,
    "travel_max_minutes": 180,
    "rural_posts": 4,
    "rural_posts_permanent": 2,
}

PROBLEMS = [
    {
        "id": "materno",
        "name": "Atención materno-infantil rural",
        "short_name": "Atención materno-infantil",
        "description": "Barreras para el inicio oportuno del control prenatal y la vacunación completa en menores de cinco años.",
        "evidence": "21% de menores de cinco años con esquema de vacunación incompleto, según la base municipal depurada del caso.",
        "status": "Prioridad identificada en fases anteriores",
        "data_gap": "Falta establecer la oportunidad del primer control prenatal y desagregar coberturas por vereda, edad y biológico.",
    },
    {
        "id": "agua",
        "name": "Acceso continuo a agua segura",
        "short_name": "Agua segura",
        "description": "Hogares rurales sin acceso continuo a agua segura y posible relación con eventos gastrointestinales.",
        "evidence": "29% de hogares rurales sin agua segura continua. La relación con enfermedad gastrointestinal es una hipótesis por validar.",
        "status": "Brecha territorial por profundizar",
        "data_gap": "Se requiere caracterizar continuidad, calidad del agua y eventos de salud relacionados.",
    },
    {
        "id": "acceso",
        "name": "Barreras geográficas y económicas de acceso",
        "short_name": "Barreras de acceso",
        "description": "Distancias, tiempos de desplazamiento y costos de transporte que dificultan el acceso a servicios.",
        "evidence": "Desplazamientos estimados de 90 minutos a 3 horas desde veredas dispersas.",
        "status": "Determinante transversal",
        "data_gap": "Falta desagregar tiempos, costos y barreras según vereda y grupo poblacional.",
    },
    {
        "id": "participacion",
        "name": "Participación y articulación comunitaria",
        "short_name": "Participación comunitaria",
        "description": "Necesidad de fortalecer la participación comunitaria y la coordinación territorial para identificar barreras.",
        "evidence": "Vacío de información sobre razones de inasistencia, diferencias entre veredas y necesidades diferenciales.",
        "status": "Vacío de información y gobernanza",
        "data_gap": "No se dispone de una consulta comunitaria sistemática ni de un registro de acuerdos territoriales.",
    },
]

# Matriz técnica multicriterio. Pesos propuestos para la simulación, suma 100%.
TECHNICAL_CRITERIA = [
    {"id": "magnitude", "name": "Magnitud", "weight": 25, "description": "Extensión del problema y población potencialmente afectada.", "guide": "1 = afectación muy limitada; 5 = afectación extensa o frecuente."},
    {"id": "severity", "name": "Severidad", "weight": 25, "description": "Consecuencias potenciales sobre salud, bienestar y continuidad del cuidado.", "guide": "1 = consecuencias leves; 5 = consecuencias graves o de alta trascendencia."},
    {"id": "equity", "name": "Inequidad", "weight": 20, "description": "Afectación de población rural, dispersa y grupos con barreras diferenciales.", "guide": "1 = baja concentración de inequidades; 5 = afecta especialmente a grupos con mayores barreras."},
    {"id": "feasibility", "name": "Viabilidad", "weight": 15, "description": "Posibilidad de organizar una respuesta desde la capacidad institucional y territorial disponible.", "guide": "1 = muy difícil de implementar; 5 = alta posibilidad de implementación."},
    {"id": "resources", "name": "Uso de recursos", "weight": 15, "description": "Disponibilidad y uso razonable de recursos humanos, logísticos y financieros.", "guide": "1 = requerimientos muy difíciles de cubrir; 5 = requerimientos relativamente manejables."},
]

# Puntajes simulados 1-5. Orden: magnitud, severidad, inequidad, viabilidad, recursos.
TECHNICAL_SCORES = {
    "materno": [5, 5, 5, 4, 3],
    "agua": [3, 4, 4, 3, 3],
    "acceso": [4, 4, 5, 3, 3],
    "participacion": [3, 3, 4, 4, 4],
}

TECHNICAL_RATIONALES = {
    "materno": [
        "La brecha de vacunación reportada sugiere una afectación relevante; falta precisar denominadores y distribución territorial.",
        "La atención prenatal y la vacunación se relacionan con prevención y continuidad de cuidados materno-infantiles.",
        "La dispersión rural puede profundizar barreras para gestantes, niños y cuidadores.",
        "Es posible organizar búsqueda activa y jornadas extramurales, sujeto a capacidad real de la red.",
        "Requiere talento humano, transporte, biológicos y cadena de frío; por ello no recibe la máxima calificación.",
    ],
    "agua": [
        "El 29% de hogares rurales sin continuidad de agua segura indica una brecha relevante, aunque falta caracterización.",
        "La falta de agua segura puede afectar condiciones de salud y bienestar; no se atribuyen aquí eventos específicos.",
        "Los hogares rurales dispersos pueden enfrentar mayor exposición y menor capacidad de respuesta.",
        "Las soluciones requieren coordinación intersectorial y acciones que exceden al sector salud.",
        "Puede requerir infraestructura e inversión sostenida, cuya disponibilidad no está documentada.",
    ],
    "acceso": [
        "Los tiempos estimados de 90 a 180 minutos muestran una barrera territorial importante.",
        "Las demoras y costos pueden afectar la oportunidad y continuidad de distintos servicios.",
        "La dispersión y las limitaciones de transporte afectan con mayor intensidad a hogares con menos recursos.",
        "Existen alternativas organizativas, pero dependen de transporte, coordinación y disponibilidad institucional.",
        "La operación extramural y los apoyos de transporte requieren recursos recurrentes.",
    ],
    "participacion": [
        "El vacío de información es transversal, pero no existe una medición de su magnitud poblacional.",
        "Una articulación débil puede limitar la pertinencia y continuidad de las respuestas.",
        "La participación inclusiva puede visibilizar necesidades de grupos que suelen quedar subrepresentados.",
        "Es viable proponer espacios de diálogo y mecanismos de registro con organización institucional.",
        "Puede iniciarse con recursos organizativos y logísticos moderados, según disponibilidad local.",
    ],
}

# Matriz participativa simulada. No corresponde a una consulta real.
COMMUNITY_CRITERIA = [
    {"id": "daily_impact", "name": "Impacto en la vida cotidiana", "weight": 30, "description": "Cuánto afecta las actividades, el bienestar y la vida familiar."},
    {"id": "urgency", "name": "Urgencia percibida", "weight": 30, "description": "Qué tan necesario se considera actuar pronto."},
    {"id": "access", "name": "Barreras de acceso y respuesta", "weight": 25, "description": "Dificultad para obtener atención o resolver la necesidad."},
    {"id": "community_action", "name": "Posibilidad de acción colectiva", "weight": 15, "description": "Oportunidad de participar en soluciones y seguimiento."},
]

COMMUNITY_SCORES = {
    "materno": [5, 5, 4, 4],
    "agua": [4, 4, 4, 3],
    "acceso": [5, 5, 5, 4],
    "participacion": [3, 3, 3, 5],
}

COMMUNITY_RATIONALES = {
    "materno": ["Afecta el cuidado de gestantes, niños y familias.", "Se considera importante evitar retrasos en controles y vacunación.", "La distancia y el transporte pueden dificultar la atención.", "Las familias pueden apoyar la búsqueda activa y el seguimiento."],
    "agua": ["La continuidad del agua condiciona tareas domésticas y bienestar.", "La necesidad es constante en hogares sin servicio continuo.", "La solución puede estar limitada por infraestructura y dispersión.", "La comunidad puede participar en vigilancia y cuidado del recurso."],
    "acceso": ["Los traslados consumen tiempo y recursos familiares.", "La barrera afecta la posibilidad de recibir atención oportunamente.", "El tiempo y costo de transporte son obstáculos directos.", "La comunidad puede ayudar a organizar rutas y reportar barreras."],
    "participacion": ["Su impacto es menos inmediato que otras necesidades materiales.", "Se percibe como una condición que debe fortalecerse progresivamente.", "La falta de espacios limita la comunicación con instituciones.", "Es el problema con mayor posibilidad directa de acción colectiva."],
}

# Integración ilustrativa: 60% resultado técnico + 40% comunitario.
INTEGRATION_WEIGHTS = {"technical": 60, "community": 40}

ACTORS = [
    {"name": "Gestantes, madres, padres y cuidadores", "role": "Experiencias de atención materno-infantil."},
    {"name": "Líderes y lideresas de las veredas", "role": "Necesidades y barreras del territorio."},
    {"name": "Autoridades étnicas y organizaciones diferenciales", "role": "Enfoque diferencial e inclusión."},
    {"name": "ESE, EPS, IPS y Secretaría de Salud", "role": "Capacidad institucional y articulación."},
    {"name": "Operadores de transporte y autoridades locales", "role": "Movilidad y condiciones de acceso."},
]

DELIBERATION_RULES = [
    ("Escucha activa", "Dar tiempo de intervención a todos los sectores, sin imponer una respuesta."),
    ("Lenguaje accesible", "Explicar criterios y alternativas sin tecnicismos innecesarios."),
    ("Inclusión", "Facilitar participación rural, diferencial y de personas con discapacidad."),
    ("Transparencia", "Registrar método, participantes por sector y resultados agregados."),
    ("Protección", "No publicar datos personales ni ubicaciones domiciliarias identificables."),
]


def _weighted_score(scores, criteria):
    return round(sum(score * criterion["weight"] for score, criterion in zip(scores, criteria)) / 100, 2)


def technical_results():
    results = []
    for problem in PROBLEMS:
        scores = TECHNICAL_SCORES[problem["id"]]
        results.append({
            **problem,
            "score": _weighted_score(scores, TECHNICAL_CRITERIA),
            "scores": scores,
            "rationales": TECHNICAL_RATIONALES[problem["id"]],
        })
    return sorted(results, key=lambda item: item["score"], reverse=True)


def community_results():
    results = []
    for problem in PROBLEMS:
        scores = COMMUNITY_SCORES[problem["id"]]
        results.append({
            **problem,
            "score": _weighted_score(scores, COMMUNITY_CRITERIA),
            "scores": scores,
            "rationales": COMMUNITY_RATIONALES[problem["id"]],
        })
    return sorted(results, key=lambda item: item["score"], reverse=True)


def integrated_results():
    technical = {item["id"]: item for item in technical_results()}
    community = {item["id"]: item for item in community_results()}
    results = []
    for problem in PROBLEMS:
        tech_score = technical[problem["id"]]["score"]
        community_score = community[problem["id"]]["score"]
        combined = (tech_score * INTEGRATION_WEIGHTS["technical"] + community_score * INTEGRATION_WEIGHTS["community"]) / 100
        difference = abs(tech_score - community_score)
        results.append({
            **problem,
            "technical_score": tech_score,
            "community_score": community_score,
            "score": round(combined, 2),
            "difference": round(difference, 2),
            "agreement": "Convergencia alta" if difference < 0.4 else ("Convergencia moderada" if difference < 0.8 else "Diferencia para deliberar"),
        })
    return sorted(results, key=lambda item: item["score"], reverse=True)


VERSION_HISTORY = [
    {"version": "V2.0", "name": "Integración metodológica y ruta de acción", "status": "Implementada para demostración", "summary": "Consolidación de matrices técnica, comunitaria e integrada; desarrollo de la ruta territorial de 12 meses, indicadores, recursos y controles de riesgo.", "changes": ["Matriz técnica ponderada con justificaciones por criterio.", "Matriz participativa simulada con actores, criterios y reglas de deliberación.", "Matriz integrada con ponderación 60% técnica y 40% comunitaria.", "Ruta de acción estructurada en cuatro fases y horizonte de 12 meses.", "Indicadores con definiciones, metas de proceso propuestas, líneas base pendientes y fuentes de verificación.", "Identificación de recursos, riesgos y controles."], "note": "Versión funcional demostrativa. Las matrices, valoraciones y metas propuestas requieren validación; no se han realizado pruebas piloto ni mediciones reales."},
    {"version": "V1.1", "name": "Ajustes de visualización adaptable", "status": "Implementada", "summary": "Corrección de la presentación del encabezado y la distribución de módulos en pantallas pequeñas.", "changes": ["Ajuste del encabezado para evitar desbordamientos.", "Reorganización de navegación lateral en móviles.", "Adaptación de márgenes, tarjetas y columnas."], "note": "Mejora visual verificada en el entorno de desarrollo; no equivale a prueba formal de usabilidad."},
    {"version": "V1.0", "name": "Estructura funcional inicial", "status": "Base implementada", "summary": "Construcción de la estructura principal del prototipo y sus módulos de priorización.", "changes": ["Navegación principal y panel de inicio.", "Módulos iniciales de evaluación técnica, participación y comparación.", "Sección de ruta de acción y registro de versiones.", "Incorporación de datos y puntuaciones demostrativas del caso El Porvenir."], "note": "Las puntuaciones son ilustrativas y requieren revisión."},
]

PILOT_CHECKS = [
    {"area": "Comprensión del propósito", "question": "¿La persona identifica para qué sirve PrioriSalud y qué decisión apoya?", "evidence": "Explicación del participante y dudas manifestadas."},
    {"area": "Comprensión de los datos", "question": "¿Distingue datos de contexto y cifras demostrativas?", "evidence": "Errores de interpretación y aclaraciones necesarias."},
    {"area": "Navegación", "question": "¿Encuentra los módulos y regresa al inicio sin ayuda?", "evidence": "Dificultades, pasos innecesarios y apoyos solicitados."},
    {"area": "Interpretación de resultados", "question": "¿Comprende criterios, ponderaciones, escalas y comparación?", "evidence": "Preguntas e interpretaciones incorrectas."},
    {"area": "Legibilidad y accesibilidad", "question": "¿Puede leer el contenido desde computador y celular?", "evidence": "Problemas de tamaño, contraste o distribución."},
]

NEXT_ITERATION = [
    "Realizar pruebas de recorrido y registrar tareas, fecha y dispositivo.",
    "Revisar los supuestos y las puntuaciones demostrativas antes de cualquier uso decisorio.",
    "Validar criterios, pesos y resultados con las fuentes y actores correspondientes.",
    "Completar metas, responsables y mecanismos de seguimiento de la ruta de acción.",
    "Documentar hallazgos, decisiones, cambios y evidencia de verificación.",
]


# Ruta de acción demostrativa de 12 meses. Metas de proceso propuestas, no resultados observados.
ACTION_PLAN = [
    {
        "phase": "01", "period": "Meses 1 y 2", "title": "Alistamiento y diagnóstico territorial",
        "objective": "Actualizar la información de gestantes y menores de cinco años, reconocer barreras por vereda y verificar la capacidad de respuesta.",
        "activities": [
            "Depurar y contrastar los registros disponibles de gestantes y menores de cinco años.",
            "Caracterizar tiempos, costos y medios de desplazamiento por vereda.",
            "Identificar oferta de la ESE, puestos de salud, EPS e IPS y disponibilidad de equipos extramurales.",
            "Establecer una línea base verificable para oportunidad prenatal y vacunación según edad.",
        ],
        "responsibles": "Secretaría de Salud municipal y ESE, con articulación de EPS/IPS y referentes comunitarios.",
        "deliverable": "Diagnóstico territorial actualizado y matriz de brechas por vereda.",
        "risks": "Registros incompletos, duplicados o desactualizados; baja disponibilidad de información desagregada.",
    },
    {
        "phase": "02", "period": "Meses 3 a 5", "title": "Búsqueda activa y atención extramural",
        "objective": "Acercar servicios preventivos a gestantes, niños y cuidadores de las zonas rurales priorizadas.",
        "activities": [
            "Diseñar un calendario concertado de jornadas extramurales por vereda.",
            "Realizar búsqueda activa y orientación para ingreso temprano al control prenatal.",
            "Verificar carnés y necesidades de vacunación de menores de cinco años, respetando lineamientos vigentes.",
            "Coordinar transporte, cadena de frío, talento humano, insumos y mecanismos de referencia.",
        ],
        "responsibles": "ESE y equipos de salud; Secretaría de Salud para coordinación y EPS/IPS para continuidad de la atención.",
        "deliverable": "Calendario de jornadas, registros agregados de atenciones y remisiones.",
        "risks": "Clima, vías, transporte, disponibilidad de biológicos o personal y dificultades de convocatoria.",
    },
    {
        "phase": "03", "period": "Meses 6 a 9", "title": "Seguimiento y continuidad del cuidado",
        "objective": "Reducir pérdidas de seguimiento y facilitar que las personas completen las atenciones requeridas.",
        "activities": [
            "Revisar listados de seguimiento con datos mínimos necesarios y acceso restringido.",
            "Coordinar recordatorios y búsqueda de personas con atenciones pendientes.",
            "Gestionar remisiones y apoyos de transporte según barreras identificadas.",
            "Revisar periódicamente diferencias de acceso entre veredas y grupos poblacionales.",
        ],
        "responsibles": "ESE, EPS/IPS y Secretaría de Salud, con apoyo de enlaces comunitarios bajo acuerdos de confidencialidad.",
        "deliverable": "Tablero de seguimiento agregado y registro de barreras resueltas o pendientes.",
        "risks": "Interrupción de la continuidad, rotación de personal y dificultades de contacto con hogares dispersos.",
    },
    {
        "phase": "04", "period": "Meses 10 a 12", "title": "Evaluación, rendición de cuentas y ajuste",
        "objective": "Valorar la ejecución, identificar brechas persistentes y acordar ajustes para el siguiente ciclo.",
        "activities": [
            "Comparar los indicadores con la línea base validada y explicar limitaciones de datos.",
            "Analizar cobertura, oportunidad y continuidad por vereda cuando el tamaño de los datos lo permita.",
            "Socializar resultados agregados con actores institucionales y comunitarios.",
            "Actualizar la ruta de acción con responsables, recursos y compromisos del siguiente periodo.",
        ],
        "responsibles": "Secretaría de Salud y ESE, con participación de EPS/IPS y representantes comunitarios.",
        "deliverable": "Informe de evaluación, acta de acuerdos y ruta de mejora actualizada.",
        "risks": "Ausencia de línea base comparable, subregistro o falta de acuerdos para sostener acciones.",
    },
]

ACTION_INDICATORS = [
    {"name": "Caracterización territorial", "definition": "Veredas con ficha de barreras y oferta actualizada / 18 veredas × 100.", "target": "Meta propuesta: caracterizar las 18 veredas.", "baseline": "Por levantar durante los meses 1 y 2.", "frequency": "Bimestral", "source": "Fichas territoriales y registro de validación."},
    {"name": "Ejecución de jornadas extramurales", "definition": "Jornadas realizadas / jornadas programadas × 100.", "target": "Meta propuesta: ejecutar al menos 90% de las jornadas programadas, con reprogramación documentada.", "baseline": "Por establecer al aprobar el calendario.", "frequency": "Mensual", "source": "Cronograma y actas de jornada."},
    {"name": "Seguimiento de esquemas pendientes", "definition": "Menores identificados con necesidad de seguimiento que cuentan con gestión documentada / total de menores identificados con necesidad × 100.", "target": "Meta propuesta: gestionar el seguimiento del 100% de los casos identificados, sin asumir que todos completan el esquema.", "baseline": "Por levantar con revisión de registros nominales.", "frequency": "Mensual", "source": "Registro institucional protegido y reporte agregado."},
    {"name": "Oportunidad del control prenatal", "definition": "Gestantes con primer control prenatal durante el primer trimestre / gestantes con información verificable × 100.", "target": "Definir después de establecer línea base y validar capacidad de respuesta.", "baseline": "No disponible; requiere medición inicial.", "frequency": "Trimestral", "source": "Registros de atención prenatal de EPS/IPS/ESE."},
    {"name": "Brechas territoriales de atención", "definition": "Comparación de cobertura y oportunidad entre veredas con datos suficientes y comparables.", "target": "Meta de proceso: producir análisis territorial y plan de mejora para brechas identificadas.", "baseline": "No disponible; requiere datos desagregados.", "frequency": "Trimestral", "source": "Consolidado agregado por vereda."},
]

RESOURCE_AREAS = [
    {"area": "Talento humano", "detail": "Medicina, enfermería, vacunación, auxiliares y apoyo administrativo según disponibilidad y competencias."},
    {"area": "Logística y transporte", "detail": "Vehículo, combustible, rutas, tiempos de desplazamiento y alternativas ante condiciones climáticas."},
    {"area": "Insumos y cadena de frío", "detail": "Biológicos, insumos, equipos y condiciones de conservación conforme a lineamientos aplicables."},
    {"area": "Información y seguimiento", "detail": "Registros depurados, conectividad cuando exista, formatos de contingencia y protección de datos."},
    {"area": "Articulación comunitaria", "detail": "Convocatoria accesible, horarios concertados, traducción o ajustes razonables cuando se requieran."},
]

RISK_CONTROLS = [
    {"risk": "Información incompleta o no comparable", "control": "Definir denominadores, fuentes, fecha de corte y reglas de calidad antes de calcular indicadores."},
    {"risk": "Baja asistencia a jornadas", "control": "Concertar fechas con referentes locales, comunicar con anticipación y revisar barreras de transporte."},
    {"risk": "Interrupción por clima o vías", "control": "Establecer rutas alternas, criterios de reprogramación y canales de comunicación."},
    {"risk": "Falta de continuidad entre prestadores", "control": "Acordar responsables de remisión, seguimiento y devolución de información agregada."},
    {"risk": "Exposición de datos personales", "control": "Aplicar acceso restringido, minimización de datos y reportes agregados sin identificadores."},
]
