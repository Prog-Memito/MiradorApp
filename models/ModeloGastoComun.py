from app import db
from sqlalchemy.orm import relationship
from datetime import datetime

class GastoComun(db.Model):
    __tablename__ = 'gastos_comunes'

    id = db.Column(db.Integer, primary_key=True)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamentos.id'), nullable=False)
    periodo = db.Column(db.String(7), nullable=False)  # formato: "MM-YYYY"
    monto = db.Column(db.Float, nullable=False)
    pagado = db.Column(db.Boolean, default=False)
    fecha_pago = db.Column(db.Date, nullable=True)

    departamento = relationship("Departamento", back_populates="gastos_comunes")

    def serializar(self):
        return {
            'id': self.id,
            'departamento_id': self.departamento_id,
            'periodo': self.periodo,
            'monto': self.monto,
            'pagado': self.pagado,
            'fecha_pago': self.fecha_pago.strftime("%d-%m-%Y") if self.fecha_pago else None
        }
