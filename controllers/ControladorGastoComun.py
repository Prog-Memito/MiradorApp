from services.ServicioGastoComun import ServicioGastoComun

class ControladorGastoComun:
    @staticmethod
    def generar_gastos(mes, anio, monto_por_departamento):
        return ServicioGastoComun.generar_gastos_comunes(mes, anio, monto_por_departamento)

    @staticmethod
    def marcar_como_pagado(departamento_id, periodo, fecha_pago):
        return ServicioGastoComun.marcar_como_pagado(departamento_id, periodo, fecha_pago)

    @staticmethod
    def obtener_gastos_pendientes(hasta_mes, hasta_anio):
        return ServicioGastoComun.obtener_gastos_pendientes(hasta_mes, hasta_anio)
