
from flask import Flask, render_template, request
from core.formatter import format_code
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os
import re

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

ALLOWED_EXTENSIONS = {'cpp', 'c', 'h', 'hpp', 'py', 'js', 'html', 'htm', 'json', 'cs', 'css', 'sql', 'css', 'go', 'rust'}

def allowed_file(filename: str) -> bool:
    """
    Verifica si la extensión de un archivo es válida.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(e):
    """
    Manejador de error cuando el archivo o texto excede el límite de tamaño.
    """
    return render_template('index.html', error="El archivo o texto enviado es demasiado grande (Máximo 2MB)."), 413

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Maneja las peticiones GET y POST para la página principal.
    """
    error = None
    formatted_html = None
    raw_code = '' 

    language = request.form.get('language', 'cpp')
    theme = request.form.get('theme', 'dracula')
    linenos = request.form.get('linenos', True)
    
    if request.method == 'POST':
        code = request.form.get('code')
        file = request.files.get('file')
        raw_code = code
        linenos = request.form.get('linenos') == 'on'
        if code and len(code) > 100000:
            error = "El código excede el límite de 100,000 caracteres."
        elif file and file.filename:
            if allowed_file(file.filename):
                sec_filename = secure_filename(file.filename)
                try:
                    raw_code = file.read().decode('utf-8')
                except UnicodeDecodeError:
                    error = "El archivo no es de texto válido o está corrupto."
            else:
                error = "Error: Extensión de archivo no permitida. Suba un archivo de código válido."
        elif code:
            resultado = format_code(code, language, theme, linenos)
            formatted_html = resultado.html

    return render_template('index.html', 
                        formatted_html=formatted_html, 
                        error=error, 
                        raw_code=raw_code,
                        language=language,
                        theme=theme,
                        linenos=linenos)

if __name__ == '__main__':
    app.run(debug=True)
