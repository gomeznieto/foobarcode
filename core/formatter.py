import re
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from dataclasses import dataclass

@dataclass
class FormatterResult:
    html: str

# Función para darle formato al código
def format_code(code_string: str, language: str, theme: str, show_linenos: bool) -> FormatterResult:
    try:
        lexer = get_lexer_by_name(language, stripall=True)
    except:
        lexer = get_lexer_by_name("text", stripall=True)
    
    formatter = HtmlFormatter(
            style=theme,
            linenos=False,
            full=False,
            noclasses=True,
            cssstyles=f"width: 100%;  overflow-x: auto;",
            prestyles='padding: .5em 1em; white-space: pre; margin: 0; line-height: 1.5;'
        )
   
    # EStilos de Pygments
    formatted_html = highlight(code_string, lexer, formatter)
    
    # Estilo de números
    if show_linenos:
        formatted_html = insert_line_numbers(formatted_html)
    
    # Párrafos previo y posterior del bloque de código para facilitar escritura en Moodle
    formatted_html = formatted_html.replace('<div class="highlight"', '<p></p><!--Creado en https://foobarcode.vercel.app/--><div class="highlight"')
    formatted_html = formatted_html.replace('</table></div>', '</table></div><p></p>')
    
    return FormatterResult(html=formatted_html)

# Función para insertar y darle estilos a los números
def insert_line_numbers(html):
    match = re.search('(<pre[^>]*>)(.*)(</pre>)', html, re.DOTALL)
    if not match: 
        return html

    pre_open = match.group(1)
    pre_open_number = match.group(1).replace('style="', 'style="color: #f1fa8c;')
    pre_content = match.group(2)
    pre_close = match.group(3)

    num_lines = pre_content.count('\n') + 1
    numbers = range(1, num_lines + 1)

    format_str = '%' + str(len(str(numbers[-1]))) + 'i'
    lines = '\n'.join(format_str % i for i in numbers)

    start, end = match.span()

    table_html = (
        f'<table style="border-collapse: collapse; margin: 0; padding: 0; width: 100%;"><tr>'
        f'<td style="border-radius: 5px 0px 0px 5px; background-color: #46495a; padding: 0; margin: 0; vertical-align: top; width: 1%; line-height: 1.5;">'
        f'{pre_open_number}{lines}{pre_close}'
        f'</td>'
        f'<td style="padding: 0; margin: 0; vertical-align: top;">'
        f'{pre_open}{pre_content}{pre_close}'
        f'</td>'
        f'</tr></table>'
    )

    return html[:start] + table_html + html[end:]
