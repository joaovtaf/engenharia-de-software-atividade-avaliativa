from src.channel import WebFactory, MobileFactory, Checkout, Notification
from src.config import OrderBuilder, Produto


def monta_pedido():
    produto = Produto("Fone de ouvido", 89.90)
    return (OrderBuilder()
            .com_cliente("Ana Paula")
            .com_produto(produto)
            .build())


def test_web_factory_cria_objetos_compativeis_com_as_abstracoes():
    web = WebFactory()

    assert isinstance(web.create_checkout(), Checkout)
    assert isinstance(web.create_notification(), Notification)


def test_mobile_factory_cria_objetos_compativeis_com_as_abstracoes():
    mobile = MobileFactory()

    assert isinstance(mobile.create_checkout(), Checkout)
    assert isinstance(mobile.create_notification(), Notification)


def test_checkout_e_notificacao_mostram_dados_do_pedido(capsys):
    pedido = monta_pedido()
    web = WebFactory()

    web.create_checkout().show(pedido)
    web.create_notification().send(pedido)

    saida = capsys.readouterr().out
    assert pedido.cliente in saida


def test_fabrica_do_canal_nao_cria_pagamento():
    web = WebFactory()
    assert not hasattr(web, "create_payment")
