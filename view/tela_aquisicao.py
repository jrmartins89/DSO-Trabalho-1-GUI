from view.tela import Tela
import PySimpleGUI as sg


class TelaAquisicao(Tela):
    def __init__(self, controlador_aquisicao):
        self.__controlador_aquisicao = controlador_aquisicao
        self.__window_cadastro = None
        self.__window_menu = None

    def init_components(self):
        sg.ChangeLookAndFeel('SandyBeach')
        layout_cadastro_aquisicao = [
                                      [sg.Text('Cadastro de uma nova aquisição')],
                                      [sg.InputText('Digite o ID do usuario', key='id_usuario')],
                                      [sg.InputText('Digite o nome do jogo', key='jogo')],
                                      [sg.InputText('Digite a data de compra', key='data_compra')],
                                      [sg.Text('Selecione a forma de pagamento')],
                                      [sg.Listbox(values=('Cartão de Crédito', 'Cartão de Débito', 'PayPal', 'Vale-Presente'), size=(15, 5))],
                                      [sg.InputText('Digite o valor da compra', key='valor_compra')],
                                      [sg.Submit()]
                                    ]

        layout_menu_aquisicao =    [
                                      [sg.Text('Menu de Aquisições')],
                                      [sg.Text('Selecione a opção desejada')],
                                      [sg.Button('Realizar uma aquisição')],
                                      [sg.Button('Listar aquisições')],
                                      [sg.Button('Voltar ao Menu Principal')],
                                      [sg.Submit()]
                                    ]

        self.__window_cadastro = sg.Window('Cadastro de Aquisição').Layout(layout_cadastro_aquisicao)
        self.__window_menu = sg.Window('Menu de Aquisição').Layout(layout_menu_aquisicao)

    def open(self):
        self.init_components()
        button, values = self.__window_menu.Read()
        if button == 'Realizar uma aquisição':
            button, values = self.__window_cadastro.Read()
            self.Close()
            return button, values
