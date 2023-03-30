import pdfkit
import jinja2

data={}
data['nombres'] = "Freddy Andres"
data['apellidos'] = "Zambrano Quilambaqui"
data['cedula'] = '0943029505'
data['sexo'] = 'Masculino'
data['fecha_nacimiento'] = '06/06/2003'
data['correo'] = 'fzambranoq2@unemi.edu.ec'
data['estado_civil'] = 'Soltero'
data['direccion'] = 'Nueva naranjal'
data['canton'] = 'Naranjal'
data['provincia'] = 'Guayas'
data['primaria'] = 'escuela fiscal mixta "Mariano Unda"'
data['secundaria'] = 'Unidad educativa "Siete de Noviembre"'
data['titulo'] = 'Bachiller: sistemas computacionales'
data['curso1'] = 'Egg-corporation  curso programacion desde cero desde julio 18 hasta el 26 de agosto '
data['curso2'] = 'Ministerio de educacion y cultura  curso de computacion desde el 5 de febrero hasta el 20 de febrero'
data['firma'] = 'Freddy Zambrano'
print(data)

context = {"data": data}
templade_Loader = jinja2.FileSystemLoader("T:\TECNICA DE PROGRAMACION\PDF__CURRICULUM_PYTHON")
templade_env = jinja2.Environment(loader=templade_Loader)

html_template = "index.html"
templade = templade_env.get_template(html_template)
output_text = templade.render(context)

path_wkthmltopdf = b"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
output_pdf = "curriculum.pdf"
pdfkit.from_string(output_text, output_pdf, configuration=config)
