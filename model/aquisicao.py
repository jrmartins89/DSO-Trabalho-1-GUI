from model.usuario import Usuario
from model.jogo import Jogo


class Aquisicao:
    def __init__(self, usuario: Usuario, jogo: Jogo, data_aquisicao: str, forma_pagamento: str, preco_compra: float):
        self.__usuario = usuario
        self.__jogo = jogo
        self.__data_aquisicao = data_aquisicao
        self.__metodo_pagamento = forma_pagamento
        self.__preco_compra = preco_compra

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def jogo(self, jogo):
        self.__jogo = jogo

    @property
    def data_aquisicao(self):
        return self.__data_aquisicao

    @data_aquisicao.setter
    def data_aquisicao(self, data_aquisicao: str):
        if isinstance(data_aquisicao, str):
            self.__data_aquisicao = data_aquisicao

    @property
    def metodo_pagamento(self):
        return self.__metodo_pagamento

    @metodo_pagamento.setter
    def metodo_pagamento(self, metodo_pagamento: str):
        if isinstance(metodo_pagamento, str):
            self.__metodo_pagamento = metodo_pagamento

    @property
    def preco_compra(self):
        return self.__preco_compra

    @preco_compra.setter
    def preco_compra(self, preco_compra: str):
        if isinstance(preco_compra, str):
            self.__preco_compra = preco_compra
