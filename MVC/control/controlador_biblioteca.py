from view.tela_biblioteca import TelaBiblioteca
from control.controlador_jogo import ControladorJogo
from control.controlador_usuario import ControladorUsuario
from control.controlador_aquisicao import ControladorAquisicao


class ControladorBiblioteca:
    def __init__(self):
        self.__tela = TelaBiblioteca(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_jogo = ControladorJogo(self)
        self.__controlador_aquisicao = ControladorAquisicao(self)
# para chamar a tela de usuarios é necessário pensar que o controlador da biblioteca conhece o controlador de usuários.

# criando um laço de repeticao

    def abre_tela(self):
        while True:
            button, values = self.__tela.open()
            if button == 'Menu de Usuários':
                self.__controlador_usuario.abre_tela()
            elif button == 'Menu de Jogos':
                self.__controlador_jogo.abre_tela()
            elif button == 'Menu de Aquisições':
                self.__controlador_aquisicao.abre_tela()
# os getters sao necessários nessa classe do controlador da biblioteca porque o controlador de aquisicoes precisa
    # acessar os outros controladores, no caso o controlador de usuarios e controlador de jogos.

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario

    @property
    def controlador_jogo(self):
        return self.__controlador_jogo

    @property
    def controlador_aquisicao(self):
        return self.__controlador_aquisicao
