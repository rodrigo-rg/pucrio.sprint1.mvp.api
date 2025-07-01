from pydantic import BaseModel
from typing import List
from model.exercicio import Exercicio
from schemas import AnotacaoSchema


class ExercicioNewSchema(BaseModel):
    """ Novo Exercício a ser inserido na base.
    """
    nome: str = "Supino reto"


class ExercicioViewSchema(BaseModel):
    """ Exercício retornado.
    """
    id: int = 1
    nome: str = "Supino reto"
    anotacoes: List[AnotacaoSchema]


class ExerciciosViewSchema(BaseModel):
    """ Listagem de Exercícios.
    """
    exercicios:List[ExercicioViewSchema]


class ExercicioComAnotacaoSchema(BaseModel):
    """ Anotação completa incluindo o nome do exercício.
    """
    id: int = 1
    nome: str = "Supino reto"
    anotacao: AnotacaoSchema


class ExercicioDelSchema(BaseModel):
    """ Exercício a ser excluído.
    """
    id: int = 1


class ExercicioDelViewSchema(BaseModel):
    """ Exercício que foi excluído.
    """
    mensagem: str
    id: int


def apresenta_exercicio(exercicio: Exercicio):
    """ Retorna o JSON de um Exercício contendo todas as suas Anotações.
    """
    return {
        "exercicio_id": exercicio.id,
        "exercicio_nome": exercicio.nome,
        "anotacoes": [{"anotacao_id": a.id,
                      "data_execucao": a.data_execucao.strftime("%d/%m/%Y"),
                      "serie": a.serie,
                      "repeticoes": a.repeticoes,
                      "carga": a.carga,
                      "comentario": a.comentario}
                      for a in exercicio.anotacoes]
    }


def apresenta_exercicios(exercicios: List[Exercicio]):
    """ Retorna o JSON de todos os Exercícios contendo todas as suas respectivas Anotações.
    """
    return {
        "exercicios": [apresenta_exercicio(e) for e in exercicios]
    }
