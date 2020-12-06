from model.jogo import Jogo
from view.tela_jogo import TelaJogo


class ControladorJogo:
    def __init__(self, controlador_biblioteca):
        self.__controlador_biblioteca = controlador_biblioteca
        self.__tela = TelaJogo(self)
        self.__jogos = []

    # evocaco do método do menu criado na classe de tela

    def abre_tela(self):
        button, values = self.__tela.open()

        if button == 'Adicionar Jogo':
            self.incluir_jogo(values['nome'], values['ano'], values['genero'], values['horas_jogadas'],
                              values['trofeus'], values['preco_jogo'])
        elif button == 'Remover Jogo':
            self.excluir_jogo(values['nome_exclusao'])
        elif button == 'Listar Jogos':
            self.listar_jogos()
        elif button == 'Voltar ao menu Principal':
            self.__controlador_biblioteca.abre_tela()

    def incluir_jogo(self, nome: str, ano_lancamento: str, genero: str, horas_jogadas: int, total_trofeus: int,
                     preco_jogo: float):
        try:
            for jogo in self.__jogos:
              if jogo.nome == nome:
                raise Exception()
        except Exception:
            self.__tela.show_message("JOGOS", "Jogo já existente no sistema")
        else:
            self.__jogos.append(Jogo(nome, ano_lancamento, genero, horas_jogadas, total_trofeus, preco_jogo))
            self.__tela.show_message("CADASTRO DE JOGOS", "Jogo cadastrado com sucesso!")

# essa funçao percorre toda a lista de jogo para localizar o registro com o nome que foi passado como parametro.
# quando acha esse registro, o objeto é removido

    def excluir_jogo(self, nome: str):
        if isinstance(nome, str):
            for jogo in self.__jogos:
                if jogo.nome == nome:
                    self.__jogos.remove(jogo)
                    self.__tela.show_message("Jogos", "Jogo excluído com sucesso!")

    # essa funcao retorna a lista de jogos
    # invocação do método próprio da tela para exibição da lista ao invés do print.
    # O método recebe uma lista de strings. Ela incia vazia e a cada iteração é adicionado o jogo.nome

    def listar_jogos(self):
        lista_jogos = ''
        for jogo in self.__jogos:
            lista_jogos += "Nome: " + jogo.nome + '\n' + "Ano de Lançamento: " + jogo.ano_lancamento + '\n' + \
                           "Gênero do Jogo: " + jogo.genero + '\n' + "Horas Jogadas: " + jogo.horas_jogadas + '\n' +\
                           "Total de Trofeus: " + jogo.total_trofeus + '\n' + "Preço do Jogo: " + jogo.preco_jogo
            self.__tela.show_message('Jogos', lista_jogos)

# percorrer a lista e retornar o objeto de jogo cujo parametro nome seja igual ao parametro nome da funcao de listagem
