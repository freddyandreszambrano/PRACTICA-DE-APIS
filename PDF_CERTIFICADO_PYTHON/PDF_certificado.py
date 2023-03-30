import pdfkit
import jinja2
from datetime import datetime

data={}
data['nombre'] = "freddy zambrano"
data['hora'] = '60'
data['fecha'] = datetime.now().date().strftime('%d-%m-%Y')
print(data)

context = {"data": data}
templade_Loader = jinja2.FileSystemLoader("T:\TECNICA DE PROGRAMACION\PDF_CERTIFICADO_PYTHON")
templade_env = jinja2.Environment(loader=templade_Loader)

html_template = "index.html"
templade = templade_env.get_template(html_template)
output_text = templade.render(context)

path_wkthmltopdf = b"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
output_pdf = "certificado.pdf"
pdfkit.from_string(output_text, output_pdf, configuration=config)
