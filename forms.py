from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import os
import logging

def generate_report(data, photo_paths):
    logging.debug("Generando reporte PDF...")

    # Cargar la plantilla HTML
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('reporte.html')

    # Renderizar el HTML con los datos
    html_out = template.render(
        fecha=data['fecha'],
        hora=data['hora'],
        nombre_usuario=data['nombre_usuario'],
        proyecto_area=data['proyecto_area'],
        numero_vehiculo=data['numero_vehiculo'],
        kilometraje_inicial=data['kilometraje_inicial'],
        kilometraje_final=data['kilometraje_final'],
        parachoques_delantero=data['parachoques_delantero'],
        parachoques_trasero=data['parachoques_trasero'],
        puerta_delantera_izquierda=data['puerta_delantera_izquierda'],
        puerta_trasera_izquierda=data['puerta_trasera_izquierda'],
        puerta_delantera_derecha=data['puerta_delantera_derecha'],
        puerta_trasera_derecha=data['puerta_trasera_derecha'],
        caja_trasera=data['caja_trasera'],
        techo=data['techo'],
        asientos=data['asientos'],
        tablero=data['tablero'],
        ventanas=data['ventanas'],
        equipamiento_adicional=data['equipamiento_adicional'],
        nivel_inicial=data['nivel_inicial'],
        nivel_final=data['nivel_final'],
        observaciones=data['observaciones'],
        firma_usuario=data['firma_usuario'],
        firma_encargado=data['firma_encargado'],
        photos=photo_paths
    )

    # Generar el PDF
    report_path = os.path.join('reports', 'reporte_inspeccion.pdf')
    HTML(string=html_out, base_url=os.getcwd()).write_pdf(report_path)
    logging.debug(f"Reporte PDF generado en: {report_path}")
    return report_path