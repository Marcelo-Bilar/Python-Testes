from ApiEmFlask.enums.TipoUsuario import TipoUsuario
from ApiEmFlask.model.Usuario import Usuario


class UsuarioService:

    def __init__(self):
        pass

    def consultarUsuario(self, nome_usuario):
        lista_usuario = [
            Usuario("Filipe","sdsadsadbnsad", TipoUsuario.ADMIM.value),
            Usuario("Daniel", "sdkhb23bh234hbf", TipoUsuario.COMUM.value),
            Usuario("Douglas", "fjnfej3onlwe", TipoUsuario.COMUM.value),
            Usuario("Rafael", "1fsdujhfsdfwhu", TipoUsuario.COMUM.value),
        ]

        for usuarioLista in lista_usuario:
            if(usuarioLista.nome == nome_usuario):
                return usuarioLista


        return None