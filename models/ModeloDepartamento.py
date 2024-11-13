from app import db
from sqlalchemy.orm import relationship

class Departamento(db.Model):
    __tablename__ = 'departamentos'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), nullable=False, unique=True)
    gastos_comunes = relationship("GastoComun", back_populates="departamento")

    def serializar(self):
        return {
            'id': self.id,
            'numero': self.numero
        }
