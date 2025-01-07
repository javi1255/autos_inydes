from flask import Flask, render_template, redirect, url_for, request, flash, make_response
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from weasyprint import HTML
import os
import uuid
from werkzeug.utils import secure_filename
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'reports/uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Limitar el tamaño del archivo a 50 MB

# Crear las carpetas necesarias si no existen
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'INYDES1255' and password == '1255':
            user = User(id=username)
            login_user(user)
            return redirect(url_for('generate_report'))
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/generate_report', methods=['GET', 'POST'])
@login_required
def generate_report():
    if request.method == 'POST':
        # Obtener los datos del formulario
        fecha = request.form.get('fecha')
        hora = request.form.get('hora')
        nombre_usuario = request.form.get('nombre_usuario')
        proyecto_area = request.form.get('proyecto_area')
        numero_vehiculo = request.form.get('numero_vehiculo')
        kilometraje_inicial = request.form.get('kilometraje_inicial')
        kilometraje_final = request.form.get('kilometraje_final')
        revision_interna = request.form.get('revision_interna')
        revision_externa = request.form.get('revision_externa')
        nivel_combustible = request.form.get('nivel_combustible')
        responsable_vehiculo = request.form.get('responsable_vehiculo')
        responsable_flotilla = request.form.get('responsable_flotilla')
        signature = request.form.get('signature')

        # Manejar la carga de fotos (hasta 15 fotos)
        fotos = []
        for file in request.files.getlist('fotos'):
            if file:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                fotos.append(filepath)

        # Guardar la firma digital
        signature_path = None
        if signature:
            signature_data = base64.b64decode(signature.split(',')[1])
            signature_filename = f'signature_{uuid.uuid4().hex}.png'
            signature_path = os.path.join(app.config['UPLOAD_FOLDER'], signature_filename)
            with open(signature_path, 'wb') as f:
                f.write(signature_data)

        # Generar número de folio único de 10 dígitos
        folio = str(uuid.uuid4().int)[:10]

        # Crear carpeta para el reporte
        report_dir = os.path.join('reports', folio)
        os.makedirs(report_dir, exist_ok=True)

        # Generar PDF
        html = render_template(
            'report_template.html',
            fecha=fecha,
            hora=hora,
            nombre_usuario=nombre_usuario,
            proyecto_area=proyecto_area,
            numero_vehiculo=numero_vehiculo,
            kilometraje_inicial=kilometraje_inicial,
            kilometraje_final=kilometraje_final,
            revision_interna=revision_interna,
            revision_externa=revision_externa,
            nivel_combustible=nivel_combustible,
            responsable_vehiculo=responsable_vehiculo,
            responsable_flotilla=responsable_flotilla,
            fotos=fotos,
            signature_path=signature_path
        )
        pdf_path = os.path.join(report_dir, f"{folio}.pdf")
        HTML(string=html, base_url=request.base_url).write_pdf(pdf_path)

        response = make_response()
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'inline; filename={folio}.pdf'
        response.data = open(pdf_path, "rb").read()
        return response
    return render_template('report_form.html')

if __name__ == '__main__':
    app.run(debug=True)