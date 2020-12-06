from view.tela import Tela
import PySimpleGUI as sg


class TelaJogo(Tela):

    def __init__(self, controlador_jogo):
        self.__controlador_jogo = controlador_jogo
        self.__window_cadastro = None
        self.__window_menu = None
        self.__window_exclusao = None

    def init_components(self):
        sg.ChangeLookAndFeel('SandyBeach')
        layout_cadastro_jogo = [
                                [sg.Text('Cadastro de um novo jogo')],
                                [sg.InputText('Nome do Jogo', key='nome')],
                                [sg.InputText('Ano de lançamento', key='ano')],
                                [sg.InputText('Genero', key='genero')],
                                [sg.InputText('Total de horas jogadas', key='horas_jogadas')],
                                [sg.InputText('Total de trofeus do jogo', key='trofeus')],
                                [sg.InputText('Preço do jogo', key='preco_jogo')],
                                [sg.Submit()]
                               ]

        layout_menu_jogo =     [
                                [sg.Text('----- JOGOS -----')],
                                [sg.Text('Clique em uma opção do menu abaixo:', size=(45, 1))],
                                [sg.Button('Adicionar Jogo')],
                                [sg.Button('Remover Jogo')],
                                [sg.Button('Listar Jogos')],
                                [sg.Button('Voltar ao menu Principal')]
                               ]

        layout_exclusao_jogo = [
                                [sg.Text('Insira o nome do jogo')],
                                [sg.InputText('Nome do jogo', key='nome_exclusao')],
                                [sg.Submit()]
                               ]

        self.__window_menu = sg.Window('Menu de Jogos').Layout(layout_menu_jogo)
        self.__window_cadastro = sg.Window('Cadastrar Jogo').Layout(layout_cadastro_jogo)
        self.__window_exclusao = sg.Window('Remover Jogo').Layout(layout_exclusao_jogo)

    def open(self):
        self.init_components()
        button, values = self.__window_menu.Read()
        if button == 'Adicionar Jogo':
            button2, values = self.__window_cadastro.Read()
        elif button == 'Remover Jogo':
            button2, values = self.__window_exclusao.Read()
        self.close()
        return button, values

    def close(self):
        self.__window_menu.Close()
        self.__window_cadastro.Close()
        self.__window_exclusao.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
