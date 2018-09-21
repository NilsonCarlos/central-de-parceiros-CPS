from webapp import db

class Adm(db.Model):
    __tablename__ = 'adm'

    id = db.Column(db.Integer, primary_key = True)
    id_parceiros = db.Column(db.Integer, db.ForeignKey('parceiros.id_geral'))

    
    
    def __init__(self, id_parceiros):
        self.id_parceiros = id_parceiros
        