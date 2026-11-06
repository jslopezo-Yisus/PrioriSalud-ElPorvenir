# PrioriSalud El Porvenir

Prototipo académico para apoyar la priorización territorial de problemas de salud en el municipio simulado de El Porvenir.

## Requisitos
- Python 3.10 o superior
- Visual Studio Code (recomendado)

## Instalación en Windows PowerShell

1. Abre esta carpeta en Visual Studio Code.
2. Comprueba si Python está disponible:

   ```powershell
   py --version
   ```

   Si funciona, crea el entorno:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   Si `py` tampoco funciona, instala Python desde https://www.python.org/downloads/ y durante la instalación marca **Add Python to PATH**. Después cierra y vuelve a abrir VS Code.

3. Instala las dependencias:

   ```powershell
   python -m pip install -r requirements.txt
   ```

   Si `python` no funciona pero `py` sí, usa:

   ```powershell
   py -m pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:

   ```powershell
   python run.py
   ```

   O, si usas el lanzador:

   ```powershell
   py run.py
   ```

5. Abre en el navegador: http://127.0.0.1:5000

## Estructura

```text
PrioriSalud-ElPorvenir/
├── app/
│   ├── __init__.py
│   ├── data.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── evaluacion_tecnica.html
│   │   ├── participacion.html
│   │   ├── resultados.html
│   │   ├── ruta_accion.html
│   │   └── versiones.html
│   └── static/
│       ├── css/style.css
│       └── js/main.js
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Nota académica
El Porvenir y sus datos corresponden a un caso simulado. Los valores de puntuación y participación incluidos en esta primera versión son demostrativos, no resultados reales ni acuerdos comunitarios validados. Las ponderaciones y valoraciones deben revisarse con los aportes del equipo antes de presentar conclusiones.
