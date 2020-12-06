class Jogo:
    def __init__(self, nome: str, ano_lancamento: str, genero: str, horas_jogadas: int, total_trofeus: int, preco_jogo: float):
        self.__genero = genero
        self.__nome = nome
        self.__ano_lancamento = ano_lancamento
        self.__horas_jogadas = horas_jogadas
        self.__total_trofeus = total_trofeus
        self.__preco_jogo = preco_jogo
        self.__jogos = []

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        if isinstance(genero, str):
            self.__genero = genero

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def ano_lancamento(self):
        return self.__ano_lancamento

    @ano_lancamento.setter
    def ano_lancamento(self, ano_lancamento: int):
      if isinstance(ano_lancamento, int):
        self.__ano_lancamento = ano_lancamento

    @property
    def horas_jogadas(self):
        return self.__horas_jogadas

    @horas_jogadas.setter
    def horas_jogadas(self, horas_jogadas: int):
      if isinstance(horas_jogadas, int):
        self.__horas_jogadas = horas_jogadas

    @property
    def preco_jogo(self):
        return self.__preco_jogo

    @preco_jogo.setter
    def preco_jogo(self, preco_jogo: float):
        if preco_jogo is isinstance(preco_jogo, float):
            self.__preco_jogo = preco_jogo

    @property
    def total_trofeus(self):
        return self.__total_trofeus

    @total_trofeus.setter
    def total_trofeus(self, total_trofeus: int):
        if isinstance(total_trofeus, int):
            self.__total_trofeus = total_trofeus

    @property
    def jogos(self):
        return self.__jogos
