from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.utils import ImageReader
import io
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('CertificateFont', 'fonts\PinyonScript-Regular.ttf'))


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']

        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=landscape(A4))
        width, height = landscape(A4)

        # Add background image
        bg_image = ImageReader('static\certificateTemplate.png')
        c.drawImage(bg_image, 0, 0, width=width, height=height)

        # Add name text
        c.setFont("CertificateFont", 58)
        text_width = c.stringWidth(name, "CertificateFont", 58)
        c.setFillColorRGB(0.2, 0.3, 0.7)
        c.drawString((width - text_width) / 2, height / 2, name)

        c.save()
        buffer.seek(0)

        return send_file(
            buffer,
            as_attachment=True,
            download_name=f'{name}_certificate.pdf',
            mimetype='application/pdf'
        )

    return render_template('index.html')
app.run(port=8000)
