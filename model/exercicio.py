from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from  model import Base, Anotacao


class Exercicio(Base):
    __tablename__ = 'exercicio'

    id = Column("pk_exercicio", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    # Relacionamento com a tabela Anotacao
    # Um exercício pode ter várias anotações associadas a ele.
    anotacoes = relationship("Anotacao")

    def __init__(self, nome:str):
        self.nome = nome

    def adiciona_anotacao(self, anotacao:Anotacao):
        """ Adiciona uma nova anotação ao Exercicio
        """
        self.anotacoes.append(anotacao)

