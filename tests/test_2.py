from src.config import Produto, OrderBuilder


produto1 = Produto("Cama Elástica para Urso Polar", 2.00)
produto2 = Produto("Anéis de Saturno", 142.00)
produto3 = Produto("Máscara dO Máscara", 1250.00)

# Construção de um pedido contendo pelo menos dois produtos e
# utilização de pelo menos dois atributos opcionais

pedido_valido = (OrderBuilder()
                 .com_cliente("Lady Gaga da Silva")
                 .com_produto(produto1)
                 .com_produto(produto2)
                 .com_produto(produto3)
                 .com_endereco("Rlyeh, apto 666")
                 .com_pagamento("Escambo")
                 .build())

print(f"Cliente: {pedido_valido.cliente}")
print(f"Endereço: {pedido_valido.endereco}")
print(f"Forma de Pagamento: {pedido_valido.pagamento}")
print(f"Total a pagar: R$ {pedido_valido.total()}")


# Tentativa de construir um pedido sem cliente
try:
    pedido_invalido = (OrderBuilder()
                       .com_produto(produto1)
                       .build())
except ValueError as erro:
    print(f"Falha na construção. Motivo: {erro}")