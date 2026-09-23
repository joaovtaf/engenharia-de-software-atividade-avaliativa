# Testes do Builder pedidos na questão 2

import pytest

from src.config import OrderBuilder, Produto


def test_builder_constroi_pedido_com_pelo_menos_dois_produtos():
    produto1 = Produto("Cama Elástica para Urso Polar", 2.00)
    produto2 = Produto("Anéis de Saturno", 142.00)

    pedido = (OrderBuilder()
              .com_cliente("Lady Gaga da Silva")
              .com_produto(produto1)
              .com_produto(produto2)
              .build())

    assert len(pedido.produtos) == 2
    assert pedido.total() == 144.00


def test_builder_aceita_pelo_menos_dois_atributos_opcionais():
    produto = Produto("Máscara dO Máscara", 1250.00)

    pedido = (OrderBuilder()
              .com_cliente("Lady Gaga da Silva")
              .com_produto(produto)
              .com_endereco("Rlyeh, apto 666")
              .com_pagamento("Escambo")
              .build())

    assert pedido.endereco == "Rlyeh, apto 666"
    assert pedido.pagamento == "Escambo"


def test_build_sem_cliente_gera_erro():
    produto = Produto("Cama Elástica para Urso Polar", 2.00)

    with pytest.raises(ValueError):
        (OrderBuilder()
         .com_produto(produto)
         .build())
