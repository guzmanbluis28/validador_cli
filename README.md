# Validador CLI

Herramienta de línea de comandos escrita en Python para validar direcciones de **email** y **URLs**.
Construida con una arquitectura limpia, modular y testeada, ideal como base para proyectos CLI más complejos.

---

## Instalación

### Requisitos previos

- Python 3.10 o superior
- `pip` instalado
- Se recomienda entorno virtual (`venv`)

### Instalación local (modo editable)

```
git clone https://github.com/tu_usuario/validador_cli.git
cd validador_cli
pip install -e
```

> Esto te permitirá usar el comando validador directamente mientras desarrollas.

## Uso

```
validador --email test@example.com
validador --url https://google.com
validador --email test@x --url http://mal
```

## Testing

Este proyecto usa pytest y pytest-cov para pruebas y cobertura. Puedes ejecutarlas con:
`make test`

También puedes lanzar los tests manualmente: `pytest`

## Estilo de código

Usamos ruff como linter y formateador.

    - Verificar estilo: make lint
    - Corregir estilo: make format

## Pre-commit hooks

Antes de cada commit, se ejecutan validaciones automáticas de código con pre-commit.
Instálalos con: `make install`

## Estructura del proyecto

```
validador_cli/
├── validador/         ← Código fuente principal
├── tests/             ← Pruebas unitarias
├── .pre-commit-config.yaml
├── .coveragerc
├── pyproject.toml     ← Configuración central
├── Makefile           ← Comandos automatizados
├── README.md
└── run.py             ← Ejecución manual (opcional)
```

## Posibles mejoras futuras

    - Soporte para validación masiva desde archivo .csv
    - Soporte para stdin / pipes en la terminal
    - Integración con logging a archivo
    - Empaquetado con poetry o publicación en PyPI

## Autor

Luis Guzmán.

Security Automation Developer & Python Backend

📍 Cantabria, España
