from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from model import Session, Exercicio, Anotacao
from schemas import *
from flask_cors import CORS
from datetime import datetime

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Tags para organizar as rotas da API na documentação OpenAPI
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
minhasrotas_tag = Tag(name="Minhas Rotas", description="Rotas da aplicação para manipulação de Anotações de Exercícios")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/anotacoes', tags=[minhasrotas_tag],
         responses={"200": ExerciciosViewSchema, "404": ErrorSchema})
def get_anotacoes():
    """Obtém todas as Anotações cadastradas.

    Retorna a listagem de Exercícios com suas respectivas Anotações.
    """

    session = Session()
    exercicios = session.query(Exercicio).order_by(Exercicio.nome.asc()).all()

    return apresenta_exercicios(exercicios), 200


@app.get('/anotacao', tags=[minhasrotas_tag],
         responses={"200": ExercicioComAnotacaoSchema, "404": ErrorSchema})
def get_anotacao(query: AnotacaoViewSchema):
    """Faz a busca por uma Anotação específica, a partir do ID da Anotação informado.

    Retorna todos os detalhes da Anotação.
    """
    session = Session()
    anotacao = session.query(Anotacao).filter(Anotacao.id == query.id).first()
    if (anotacao is None):
        # Se a anotação não foi encontrada, retorna um erro 404.
        error_msg = "Anotação não encontrada na base."
        return {"mensagem": error_msg}, 404
    # A partir da anotação encontrada, busca o exercício relacionado.
    # O objetivo é obter também o nome do exercício associado à anotação.
    exercicio = session.query(Exercicio).filter(Exercicio.id == anotacao.exercicio_id).first()
    return apresenta_anotacao_completa(anotacao, exercicio.nome), 200


@app.post('/anotacao', tags=[minhasrotas_tag],
          responses={"200": AnotacaoViewSchema, "400": ErrorSchema})
def add_anotacao(form: AnotacaoNewSchema):
    """Adiciona uma nova Anotação na base.

    Retorna o ID da Anotação que foi inserida.
    """

    try:
        # Validação dos valores digitados.
        serie = int(form.serie)
        repeticoes = int(form.repeticoes)
        carga = int(form.carga)
        comentario = str(form.comentario)
        # Data tem que estar no formato 'dd/mm/aaaa'
        data_execucao = datetime.strptime(form.data_execucao, "%d/%m/%Y").date()

        session = Session()
        # Verifica se o exercício já existe na base de dados
        exercicio_nome = form.exercicio_nome
        exercicio = session.query(Exercicio).filter(Exercicio.nome == exercicio_nome).first()
        # Se não existir, cria um novo exercício com o nome fornecido.
        if not exercicio:
            exercicio_id = add_exercicio(exercicio_nome)
            if exercicio_id == -1:
                error_msg = "Não foi possível adicionar anotação, erro ao adicionar exercício."
                return {"mensagem": error_msg}, 400
            exercicio = session.query(Exercicio).filter(Exercicio.id == exercicio_id).first()
        # Cria a nova anotação com os dados fornecidos.
        anotacao = Anotacao(
            exercicio_id = exercicio.id,
            serie = serie,
            repeticoes = repeticoes,
            carga = carga,
            comentario = comentario,
            data_execucao = data_execucao
        )
        exercicio.adiciona_anotacao(anotacao)
        session.commit()
        return apresenta_anotacao(anotacao), 200

    except (ValueError, TypeError) as e:
        # Captura erros de conversão de tipos, como quando o usuário digita um texto
        error_msg = "Dados inválidos. Verifique os campos digitados."
        return {"mensagem": error_msg}, 400

    except Exception as e:
        error_msg = "Não foi possível salvar nova anotação."
        return {"mensagem": error_msg}, 400


def add_exercicio(exercicio_nome: str) -> int:
    """Adiciona um novo Exercicio à base de dados, na tabela de Exercicios.

    Retorna o ID do Exercício que foi adicionado.
    """
    exercicio = Exercicio(nome=exercicio_nome)
    try:
        session = Session()
        session.add(exercicio)
        session.commit()
        return exercicio.id
    except Exception as e:
        error_msg = "Não foi possível salvar novo exercício."
        raise Exception(error_msg)


@app.delete('/anotacao', tags=[minhasrotas_tag],
            responses={"200": AnotacaoDelViewSchema, "400": ErrorSchema, "404": ErrorSchema})
def del_anotacao(query: AnotacaoDelSchema):
    """Exclui uma Anotação a partir do ID informado.

    Retorna uma mensagem de confirmação da exclusão.
    """
    try:
        anotacao_id = query.id
        session = Session()
        count = session.query(Anotacao).filter(Anotacao.id == anotacao_id).delete()
        session.commit()
        if count == 0:
            # Se a anotação não foi encontrada
            error_msg = "Anotação não encontrada na base."
            return {"mensagem": error_msg}, 404
        return {"mensagem": "Anotação excluída.", "id": anotacao_id}
    
    except Exception as e:
        error_msg = "Não foi possível excluir a anotação."
        return {"mensagem": error_msg}, 400
