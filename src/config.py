# Configuração compartilhada da aplicação e o pedido com o builder dele

# Questão 1

class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'environment'):
            self.environment = 'production'
        if not hasattr(self, 'currency'):
            self.currency = 'BRL'
        if not hasattr(self, 'debug'):
            self.debug = False

# Questão 2

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Order:

    def __init__(self, cliente, produtos, endereco=None, cupom=None, pagamento=None, observacao=None):
        self.cliente = cliente
        self.produtos = produtos
        self.endereco = endereco
        self.cupom = cupom
        self.pagamento = pagamento
        self.observacao = observacao

    def total(self):

        total = 0
        for produto in self.produtos:
            total += produto.preco
            
        return total

class OrderBuilder:

    def __init__(self):

        self._cliente = None
        self._produtos = []
        self._endereco = None
        self._cupom = None
        self._pagamento = None
        self._observacao = None

    def com_cliente(self, nome):
        self._cliente = nome
        return self

    def com_produto(self, produto):
        self._produtos.append(produto)
        return self
        
    def com_endereco(self, endereco):
        self._endereco = endereco
        return self

    def com_cupom(self, cupom):
        self._cupom = cupom
        return self
    
    def com_pagamento(self, pagamento):
        self._pagamento = pagamento
        return self

    def com_observacao(self, observacao):
        self._observacao = observacao
        return self

    def build(self):

        if self._cliente is None:
            raise ValueError("Precisa de cliente")
        
        return Order(self._cliente, 
                     self._produtos, 
                     self._endereco, 
                     self._cupom, 
                     self._pagamento, 
                     self._observacao)




