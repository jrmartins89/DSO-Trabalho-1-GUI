from view.tela_aquisicao import TelaAquisicao
from model.aquisicao import Aquisicao


class ControladorAquisicao:

    def __init__(self, controlador_biblioteca):
        self.__controlador_biblioteca = controlador_biblioteca
        self.__tela = TelaAquisicao(self)
        self.__aquisicoes = []

    def abre_tela(self):
        button, values = self.__tela.open()
        if button == 'Realizar uma aquisição':
            self.efetuar_aquisicao(values['id_usuario'], values['nome'], values['data_aquisicao'],
                                   values['data_aquisicao'], values['forma_pagamento'])
        elif button == 'Listar aquisições':
            self.listar_aquisicoes()
        elif button == 'Voltar ao Menu Principal':
            self.__controlador_biblioteca.abre_tela()

# o controlador biblioteca sao privados porque nessa classe de controlador de aquisiçao não há getter,
# entao o acesso tem que ser de forma privada
    
    def efetuar_aquisicao(self, id_usuario: str, jogo: str, data_aquisicao: str, forma_pagamento: str,
                          preco_compra: float):
        try:
            usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
            jogo = self.__controlador_biblioteca.controlador_jogo.listar_jogo_por_nome(jogo)
        except Exception:
            print("Usuário ou jogo não existente")
        else:
            self.__aquisicoes.append(Aquisicao(usuario, jogo, data_aquisicao, forma_pagamento, preco_compra))
            print("Jogo adquirido!")

    def listar_aquisicoes(self):
        lista_aquisicoes = []
        for aquisicao in self.__aquisicoes:
            lista_aquisicoes.append(aquisicao.jogo.nome)
        self.__tela.mostra_lista_str(lista_aquisicoes)
