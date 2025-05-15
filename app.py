from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io

# Register the custom font
pdfmetrics.registerFont(TTFont('CertificateFont', 'fonts/PinyonScript-Regular.ttf'))

app = Flask(__name__)

# Fixed date for the certificate
# FIXED_DATE = "May 15, 2025"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        #Name Adjustment
        # y_offset = int(request.form.get('y_offset', 265)) #for regular workshop
        y_offset = int(request.form.get('y_offset', 285))  #for AIBAITCLUB
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=landscape(A4))
        width, height = landscape(A4)

        # Background image

        # bg_image = ImageReader('static/certificateTemplate.png')
        bg_image = ImageReader('static\CertificateAIBAITCLUB.png')
        c.drawImage(bg_image, 0, 0, width=width, height=height)

        # Name Text
        c.setFont("CertificateFont", 58)
        text_width = c.stringWidth(name, "CertificateFont", 58)
        c.setFillColorRGB(0.2, 0.3, 0.7)
        c.drawString((width - text_width) / 2, y_offset, name)

        # # Fixed Date Text (bottom-right corner)
        # c.setFont("Helvetica", 18)
        # c.setFillColorRGB(0.3, 0.3, 0.3)
        # c.drawRightString(width - 80, 80, FIXED_DATE)

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
