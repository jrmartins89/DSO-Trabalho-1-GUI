from abc import ABC, abstractmethod

class Tela(ABC):
  @abstractmethod
  def __init__(self, controlador):
    self.__controlador = controlador

  @abstractmethod
  ##def tela_opcoes(self):
  ##  pass

  def mostra_lista_str(self, lista: []):
    for elem in lista:
      print(elem)