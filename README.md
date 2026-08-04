# FooBar Code 🚀

Convierte tu código a HTML con resaltado de sintaxis y estilos inline. Ideal para pegar en Aulas Virtuales (Moodle, Goole ClassRoom), foros, y editores TinyMCE sin perder los colores.

![Python](https://img.shields.io/badge/Python-3.14+-3776AB?logo=python&style=flat)
![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?logo=flask&style=flat)
![License](https://img.shields.io/badge/License-MIT-green)

## Características

- 🎨 **Múltiples temas**: Monokai, Dracula, GitHub Dark, Nord, One Dark, Material, y más
- 📋 **Más de 10 lenguajes**: C++, C#, SQL, JavaScript, Python, HTML, JSON, Java, Rust, Go
- 📎 **Entrada dual**: Pegá código o subí archivos
- 🔢 **Números de línea**: Opcionales
- 🌙 **Tema oscuro/claro**: Toggle para la interfaz
- 📱 **HTML con estilos inline**: Listo para copiar y pegar en cualquier lado

## Instalación

### Requisitos

- Python 3.10+

### Paso a paso

```bash
# 1. Clonar el repositorio
git clone https://github.com/gomeznieto/foobarcode.git
cd foobarcode

# 2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 3. Instalar dependencias
pip install flask pygments

# 4. Ejecutar
python app.py
```

La app va a correr en `http://localhost:5000` 🎉

## Uso

1. **Pegá tu código** en el editor o subí un archivo
2. **Elegí el lenguaje** del dropdown
3. **Seleccioná el tema** que más te guste
4. **Activá números de línea** si los necesitás
5. **Hacé clic en "Convertir"**
6. **Copiá el HTML** resultante y pegalo donde necesites

## Tecnologías

| Herramienta | Uso |
|-------------|-----|
| **Flask** | Servidor web |
| **Pygments** | Resaltado de sintaxis |
| **CodeMirror** | Editor de código en el browser |
| **Tailwind CSS** | Estilos de la interfaz |

## Límites

- Máximo 2MB por archivo
- Máximo 100,000 caracteres por texto

## Estructura del Proyecto

```
format/
├── app.py                 # Aplicación Flask
├── core/
│   └── formatter.py       # Lógica de formateo con Pygments
├── templates/
│   └── index.html         # Interfaz de usuario
├── static/
│   ├── css/               # Estilos
│   ├── js/                # Scripts
│   └── img/               # Imágenes
└── README.md
```

## Deploy en Vercel

El proyecto incluye `vercel.json` para deploy automático en Vercel:

```bash
npm i -g vercel
vercel
```

## Licencia

MIT © Alejandro Gomez Nieto

---

Hecho con ❤️ y [Pygments](https://pygments.org/)
