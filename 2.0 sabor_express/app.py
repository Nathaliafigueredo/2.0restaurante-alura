from modelos.restaurante import Restaurante 


restaurante_praca = Restaurante ('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui',24)
restaurante_praca.receber_avaliacao('nati',5)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()