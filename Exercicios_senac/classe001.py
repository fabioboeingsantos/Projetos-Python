class Produto():
    def __unit__(self, nome: str, preco: float, qtd: int):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def exibir(self):
        print(f'produto {self.nome}, preco{self.preco}, qtd{self.qtd}')

produto_01 = Produto("arroz", 10.0, 15)

produto_02 = Produto(nome="feijao", preco=9.0, qtd=9)



produto_01.exibir()