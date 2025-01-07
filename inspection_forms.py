from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, IntegerField, TextAreaField, FileField, RadioField, SelectField
from wtforms.validators import DataRequired, NumberRange

class InspectionForm(FlaskForm):
    fecha = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired(message="Por favor, ingrese una fecha válida.")])
    hora = TimeField('Hora', format='%H:%M', validators=[DataRequired(message="Por favor, ingrese una hora válida.")])
    nombre_usuario = StringField('Nombre del Usuario', validators=[DataRequired(message="Por favor, ingrese su nombre.")])
    proyecto_area = StringField('Proyecto/Área Asignada', validators=[DataRequired(message="Por favor, ingrese el proyecto o área asignada.")])
    numero_vehiculo = StringField('Número de Vehículo', validators=[DataRequired(message="Por favor, ingrese el número del vehículo.")])
    kilometraje_inicial = IntegerField('Kilometraje Inicial', validators=[DataRequired(message="Por favor, ingrese el kilometraje inicial."), NumberRange(min=0, message="El kilometraje debe ser un número positivo.")])
    kilometraje_final = IntegerField('Kilometraje Final', validators=[DataRequired(message="Por favor, ingrese el kilometraje final."), NumberRange(min=0, message="El kilometraje debe ser un número positivo.")])
    
    # Sección de inspección externa
    parachoques_delantero = RadioField('Parachoques delantero', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    parachoques_trasero = RadioField('Parachoques trasero', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    puerta_delantera_izquierda = RadioField('Puerta delantera izquierda', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    puerta_trasera_izquierda = RadioField('Puerta trasera izquierda', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    puerta_delantera_derecha = RadioField('Puerta delantera derecha', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    puerta_trasera_derecha = RadioField('Puerta trasera derecha', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    caja_trasera = RadioField('Caja trasera', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    techo = RadioField('Techo', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    
    # Sección de inspección interna
    asientos = RadioField('Asientos', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    tablero = RadioField('Tablero', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    ventanas = RadioField('Ventanas', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    equipamiento_adicional = RadioField('Equipamiento adicional', choices=[('con_danio', 'Con daño'), ('sin_danio', 'Sin daño')], default='sin_danio', validators=[DataRequired()])
    
    # Campo de opción múltiple para el nivel de combustible
    nivel_combustible = SelectField('Nivel de combustible con el que se entrega el vehículo', choices=[('1/4', '1/4'), ('2/4', '2/4'), ('3/4', '3/4'), ('tanque_lleno', 'Tanque lleno')], validators=[DataRequired()])
    
    observaciones = TextAreaField('Observaciones Generales', validators=[DataRequired(message="Por favor, ingrese las observaciones generales.")])
    firma_usuario = StringField('Usuario responsable del vehículo', validators=[DataRequired(message="Por favor, ingrese su firma.")])
    firma_encargado = StringField('Encargado de Flotilla', validators=[DataRequired(message="Por favor, ingrese la firma del encargado de flotilla.")])
    photos = FileField('Subir Fotos (máximo 15)', validators=[DataRequired(message="Por favor, suba las fotos.")])