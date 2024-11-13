from flask import Blueprint, request, jsonify
from controllers.ControladorGastoComun import ControladorGastoComun
from datetime import datetime

gastos_comunes_blueprint = Blueprint('gastos_comunes_blueprint', __name__)

@gastos_comunes_blueprint.route('/gastos/generar', methods=['POST'])
def generar_gastos():
    data = request.get_json()
    mes = data.get('mes')
    anio = data.get('anio')
    monto_por_departamento = data.get('monto')
    
    gastos = ControladorGastoComun.generar_gastos(mes, anio, monto_por_departamento)
    return jsonify({"mensaje": "Gastos generados exitosamente", "gastos": [g.serializar() for g in gastos]}), 201

@gastos_comunes_blueprint.route('/gastos/marcar_pagado', methods=['PATCH'])
def marcar_como_pagado():
    data = request.get_json()
    departamento_id = data.get('departamento_id')
    periodo = data.get('periodo')
    fecha_pago = datetime.strptime(data.get('fecha_pago'), "%d-%m-%Y")

    resultado = ControladorGastoComun.marcar_como_pagado(departamento_id, periodo, fecha_pago)
    return jsonify(resultado[0]), resultado[1]

@gastos_comunes_blueprint.route('/gastos/pendientes', methods=['GET'])
def obtener_gastos_pendientes():
    hasta_mes = int(request.args.get('mes'))
    hasta_anio = int(request.args.get('anio'))

    resultado = ControladorGastoComun.obtener_gastos_pendientes(hasta_mes, hasta_anio)
    return jsonify({"gastos_pendientes": resultado[0]}), resultado[1]
