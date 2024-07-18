
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

#metodo referenciado a classe e no a um objeto ou instancia - precisa indicar @classmethod
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        #para cada restaurante na lista - Restaurante.restaurantes para localizar melhor
        #Restaurante.restaurantes ou cls.restaurantes não precisa da instancia de objetos daquela classe, com a classe ja consegue acessar aqueles metodos
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
    #vai retornar caso ele for verdadeiro, se não vai retornar falso
        return '☑' if self._ativo else '☐'
    
    #metodo para os objetos
    def alternar_estado(self):
        self._ativo = not self._ativo 

#self= objeto que vai receber essa avaliação
    def receber_avaliacao(self,cliente, nota):
        if 0< nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao) #coloca dentro da lista essa avaliacao nova

    @property #não é um método comum, entao com o property se torna capaz de ler essas informações
    def media_avaliacoes(self):
        #se o restaurante não tiver avalicao retornar
        if not self._avaliacao:
            return '-'
        #pega todas as avaliacoes e para cada avaliacao a unica informacao que eu quero é a nota -> soma elas
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media