<div align="center">

# Práctica — Modelado con SQLAlchemy

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-D71F00?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-migraciones-6BA81E?logo=alembic&logoColor=white)](https://alembic.sqlalchemy.org/)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-yellow.svg)](LICENSE)

Práctica de modelado de datos con SQLAlchemy y migraciones de Alembic sobre Flask:
relaciones uno a muchos y muchos a muchos entre usuarios, canciones, álbumes y
medios.

</div>

---

## Descripción

Ejercicio de clase centrado en el diseño del modelo de datos y en el manejo de
migraciones. El dominio es un catálogo musical: un usuario tiene álbumes, un álbum
agrupa canciones y cada canción puede estar disponible en varios medios
(digital, CD, vinilo).

## Modelo de datos

```
usuarios ──< albumes ──< album_cancion >── canciones
                                              │
                                           medios
```

| Modelo | Tabla | Relación |
| :--- | :--- | :--- |
| `Usuario` | `usuarios` | uno a muchos con álbumes |
| `Album` | `albumes` | uno a muchos con canciones (vía tabla intermedia) |
| `Cancion` | `canciones` | muchos a muchos con álbumes y medios |
| `AlbumCancion` | `album_cancion` | tabla intermedia |
| `Medio` | `medios` | formato de publicación |

## Estructura

```
app/
├── config/settings.py        Configuración y cadena de conexión
├── database/database.py      Instancia de SQLAlchemy
└── models/                   Un archivo por entidad
migrations/                   Historial de migraciones de Alembic
run.py                        Punto de entrada
```

## Cómo ejecutarlo

```bash
python -m venv venv
venv\Scripts\activate         # Windows
pip install -r requirements.txt

flask db upgrade              # aplica las migraciones
python run.py
```

## Autor

**Sara Garzón** · [github.com/sara051106garzon-boop](https://github.com/sara051106garzon-boop)

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
