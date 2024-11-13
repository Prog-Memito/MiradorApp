from models.ModeloGastoComun import db, GastoComun
from models.ModeloDepartamento import Departamento
from datetime import datetime

class ServicioGastoComun:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ServicioGastoComun, cls).__new__(cls)
        return cls._instancia

    @staticmethod
    def generar_gastos_comunes(mes, anio, monto_por_departamento):
        periodo = f"{mes:02d}-{anio}"
        departamentos = Departamento.query.all()
        gastos_creados = []

        for departamento in departamentos:
            gasto = GastoComun(departamento_id=departamento.id, periodo=periodo, monto=monto_por_departamento)
            db.session.add(gasto)
            gastos_creados.append(gasto)

        db.session.commit()
        return gastos_creados

    @staticmethod
    def marcar_como_pagado(departamento_id, periodo, fecha_pago):
        gasto = GastoComun.query.filter_by(departamento_id=departamento_id, periodo=periodo).first()
        
        if not gasto:
            return {"mensaje": "No existe el gasto para este periodo"}, 404
        if gasto.pagado:
            return {"mensaje": "Pago duplicado"}, 400

        pago_dentro_plazo = fecha_pago <= datetime.strptime(f"10-{periodo}", "%d-%m-%Y")
        estado_transaccion = "Pago exitoso dentro del plazo" if pago_dentro_plazo else "Pago exitoso fuera de plazo"
        
        gasto.pagado = True
        gasto.fecha_pago = fecha_pago
        db.session.commit()

        return {"mensaje": estado_transaccion, "departamento": gasto.departamento_id, "periodo": gasto.periodo}, 200

    @staticmethod
    def obtener_gastos_pendientes(hasta_mes, hasta_anio):
        periodo_max = f"{hasta_mes:02d}-{hasta_anio}"
        pendientes = GastoComun.query.filter(
            GastoComun.periodo <= periodo_max,
            GastoComun.pagado == False
        ).order_by(GastoComun.periodo.asc()).all()

        if not pendientes:
            return {"mensaje": "Sin montos pendientes"}, 404

        return [gasto.serializar() for gasto in pendientes], 200
