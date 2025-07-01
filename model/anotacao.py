from sqlalchemy import Column, String, Integer, Date, ForeignKey
from datetime import datetime
from  model import Base


class Anotacao(Base):
    __tablename__ = 'anotacao'

    # Identificador único da anotação.
    id = Column("pk_anotacao", Integer, primary_key=True)
    # ID do exercício ao qual a anotação está associada.
    exercicio_id = Column(Integer, ForeignKey("exercicio.pk_exercicio"), nullable=False)
    # Data em que o exercício foi executado.
    data_execucao = Column(Date, nullable=False)
    # Número da série do exercício (geralmente varia de 1 a 4).
    serie = Column(Integer, nullable=False)
    # Número de repetições que foram executadas (geralmenete varia de 6 a 15).
    repeticoes = Column(Integer, nullable=False)
    # Carga utilizada nessa série (geralmente em kg).
    carga = Column(Integer, nullable=False)
    # Comentário sobre a execução dessa série.
    comentario = Column(String(200))

    def __init__(self, exercicio_id:int, serie:int, repeticoes:int, carga:int, comentario:str, data_execucao:Date):
        self.exercicio_id = exercicio_id
        self.data_execucao = data_execucao
        self.serie = serie
        self.repeticoes = repeticoes
        self.carga = carga
        self.comentario = comentario

