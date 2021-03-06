from webapp import db
from models.table_unidades import Unidades
from models.table_atividades import Atividades
from models.table_diretores import Diretores

class Eventos(db.Model):
    __tablename__:'eventos'

    id = db.Column(db.Integer, primary_key=True)
    id_atividades = db.Column(db.Integer,db.ForeignKey(Atividades.id))
    id_unidades = db.Column(db.Integer,db.ForeignKey(Unidades.id))
    _data = db.Column(db.Date())
    hora = db.Column(db.Time())
    id_diretor = db.Column(db.Integer, db.ForeignKey(Diretores.id))
    situacao = db.Column(db.Boolean)


    def __init__(self,id_atividades,id_unidades,_data,hora, id_diretor, situacao):
        self.id_atividades = id_atividades
        self.id_unidades = id_unidades
        self._data = _data
        self.hora = hora
        self.id_diretor = id_diretor
        self.situacao = situacao