from view.tela import Tela
import PySimpleGUI as sg


class TelaUsuario(Tela):
    def __init__(self, controlador_usuario):
        self.__controlador_usuario = controlador_usuario
        self.__window_cadastro = None
        self.__window_menu = None
        self.__window_exclusao = None

    def init_components(self):
        sg.ChangeLookAndFeel('SandyBeach')
        layout_cadastro_usuario = [
                                    [sg.Text('Cadastro de um novo usuário')],
                                    [sg.InputText('Nome do usuario', key='nome')],
                                    [sg.InputText('Email', key='email')],
                                    [sg.InputText('ID_Usuário(apenas numeros)', key='id_usuario')],
                                    [sg.Submit()]
                                  ]

        layout_menu_usuario =     [
                                    [sg.Text('----- USUÁRIOS -----')],
                                    [sg.Text('Clique em uma opção do menu abaixo:')],
                                    [sg.Button('Adicionar usuário')],
                                    [sg.Button('Remover usuário')],
                                    [sg.Button('Listar usuários')],
                                    [sg.Button('Voltar ao menu principal')],
                                  ]

        layout_exclusao_usuario = [
                                    [sg.Text('Exclusão de um novo usuário')],
                                    [sg.InputText('Digite o nome do usuário', key='nome_exclusao')],
                                    [sg.Submit()]
                                  ]

        self.__window_cadastro = sg.Window('Cadastro de Usuários').Layout(layout_cadastro_usuario)
        self.__window_exclusao = sg.Window('Remoção de Usuários').Layout(layout_exclusao_usuario)
        self.__window_menu = sg.Window('Menu de Usuários').Layout(layout_menu_usuario)

    def open_menu(self):
        self.init_components()
        button, values = self.__window_menu.Read()
        if button == 'Adicionar usuário':
            button2, values = self.__window_cadastro.Read()
        elif button == 'Remover usuário':
            button2, values = self.__window_exclusao()
        self.close()
        return button, values

    def close(self):
        self.__window_menu.Close()
        self.__window_cadastro.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

"""
     esse método recebe uma lista como parametro, percorre ela e exibe os elementos da mesma
    def exibir_menu_opcoes(self, lista: []):
       for elem in lista:
            print(elem)

    def verifica_opcao(self, msg: str = "", opcoes_validas: [] = None):
        while True:
            valor_lido = input(msg)
            try:
               inteiro = int(valor_lido)
               if opcoes_validas and inteiro not in opcoes_validas:
                   raise ValueError
               return inteiro
           except ValueError:
               print("Digite uma opção válida.")

    def tratar_int_str(self, msg=""):
        while True:
            try:
                resposta = int(input(msg))
                return resposta
            except ValueError:
"""