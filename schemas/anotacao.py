from pydantic import BaseModel
from typing import Optional
from model.anotacao import Anotacao
from datetime import date


class AnotacaoSchema(BaseModel):
    """ Anotação retornada.
    """
    anotacao_id: int = 1
    data_execucao: Optional[str] = date.today().isoformat()  # Data no formato ISO 8601, ex: "2023-10-01"
    serie: int = 1
    repeticoes: int = 1
    carga: int = 60
    comentario: Optional[str] = "Boa disposição hoje"


class AnotacaoNewSchema(BaseModel):
    """ Anotação a ser inserida.
    """
    exercicio_nome: str = "Supino reto"
    data_execucao: str = date.today().strftime("%d/%m/%Y")  # Data no formato dd/mm/aaaa
    serie: int = 1
    repeticoes: int = 8
    carga: int = 60
    comentario: Optional[str] = "Boa disposição hoje"


class AnotacaoViewSchema(BaseModel):
    """ Anotacão existente na base.
    """
    id: int = 1


class AnotacaoDelSchema(BaseModel):
    """ Anotação a ser excluída.
    """
    id: str


class AnotacaoDelViewSchema(BaseModel):
    """ Anotação que foi excluída.
    """
    mensagem: str
    id: int


def apresenta_anotacao(anotacao: Anotacao):
    """ Retorna o JSON contendo o ID da Anotação criada.
    """
    return {
        "anotacao_id": anotacao.id,
    }

def apresenta_anotacao_completa(anotacao: Anotacao, exercicio_nome: str):
    """ Retorna o JSON de uma Anotação incluindo o nome do Exercício.
    """
    return {
        "exercicio_id": anotacao.exercicio_id,
        "exercicio_nome": exercicio_nome,
        "anotacao_id": anotacao.id,
        "data_execucao": anotacao.data_execucao.strftime("%d/%m/%Y"),
        "serie": anotacao.serie,
        "repeticoes": anotacao.repeticoes,
        "carga": anotacao.carga,
        "comentario": anotacao.comentario
    }