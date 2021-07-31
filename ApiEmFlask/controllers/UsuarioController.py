import json

from flask import Blueprint, Response, request

from ApiEmFlask.enums.TipoUsuario import TipoUsuario
from ApiEmFlask.model.Usuario import Usuario
from ApiEmFlask.service.UsuarioService import UsuarioService

usuario_controller = Blueprint('usuario_controller', __name__)

usuarioService = UsuarioService()

@usuario_controller.route('/login', methods=["POST"])
def login():
    parametros = request.get_json()
    resposta = {
        "mensagem": ""
    }
    usuario = Usuario(parametros["usuario"], parametros["senha"], TipoUsuario.COMUM.value)

    if (usuario.nome == "Felipoe" and usuario.senha == "12345"):
        usuario.token = "SDAFJND234JKREJKSDJJ3234JN!@$DSJOSAKDÇ"

        return Response(json.dumps(usuario.__dict__), status=200, mimetype="/application/app")

    else:
        resposta["mensagem"] = "Usuario ou Senha incorretos"

        return Response(json.dumps(resposta), status=401, mimetype="/application/app")


@usuario_controller.route('/consultar', methods=["GET"])
def consultar_usuario():
    nome_usuario = request.args.get("nome_usuario")

    resposta_consulta = usuarioService.consultarUsuario(nome_usuario)

    if(resposta_consulta):
        return Response(json.dumps(resposta_consulta.__dict__), status=200, mimetype="/application/app")
    else:
        resposta = {
            "mensagem": "usuario nao encontrado!"
        }
        return Response(json.dumps(resposta), status=404, mimetype="/application/app")