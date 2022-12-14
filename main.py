#orientação a objetos estoque
class Estoque:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
    def baixa(self, quantidade):
        if self.quantidade < quantidade:
            print('Quantidade insuficiente em estoque')
            return
        self.quantidade -= quantidade
    def repor(self, quantidade):
        self.quantidade += quantidade
    def mostra(self):
        print('Produto: ', self.nome)
        print('Quantidade: ', self.quantidade)
#orientação a objetos venda
class Venda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
    def registra_venda(self):
        self.produto.baixa(self.quantidade)
    def cancela_venda(self):
        self.produto.repor(self.quantidade)
#orientação a objetos produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def mostra(self):
        print('Produto: ', self.nome)
        print('Preço: ', self.preco)

#orientação a objetos preço
class Preco:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco
    def altera_preco(self, novo_preco):
        self.preco = novo_preco
    def mostra(self):
        print('Produto: ', self.produto.nome)
        print('Preço: ', self.preco)

#orientação a objetos item venda
class ItemVenda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
    def mostra(self):
        print('Produto: ', self.produto.nome)
        print('Quantidade: ', self.quantidade)
        print('Preço: ', self.produto.preco)
        print('Total: ', self.produto.preco * self.quantidade)



#funcionamento
def main():
    while True:
        print('1 - Estoque')
        print('2 - Venda')
        print('3 - Preço')
        print('4 - Item Venda')
        print('5 - Sair')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            print('1 - Mostrar')
            print('2 - Baixa')
            print('3 - Repor')
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1:
                estoque.mostra()
            elif opcao == 2:
                quantidade = int(input('Digite a quantidade: '))
                estoque.baixa(quantidade)
            elif opcao == 3:
                quantidade = int(input('Digite a quantidade: '))
                estoque.repor(quantidade)
        elif opcao == 2:
            print('1 - Registrar Venda')
            print('2 - Cancelar Venda')
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1:
                venda.registra_venda()
            elif opcao == 2:
                venda.cancela_venda()
        elif opcao == 3:
            print('1 - Mostrar')
            print('2 - Alterar Preço')
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1:
                preco.mostra()
            elif opcao == 2:
                novo_preco = float(input('Digite o novo preço: '))
                preco.altera_preco(novo_preco)
        elif opcao == 4:
            item_venda.mostra()
        elif opcao == 5:
            break
        else:
            print('Opção inválida')

#instanciando objetos
estoque = Estoque('Camiseta', 10)
produto = Produto('Camiseta', 50)
preco = Preco(produto, 50)
venda = Venda(estoque, 5)
item_venda = ItemVenda(produto, 5)

#executando
main()