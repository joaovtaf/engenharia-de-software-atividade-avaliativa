# Testes do Factory Method do pagamento, questão 3

from src.config import OrderBuilder, Produto
from src.payment import get_payment_processor, PixPayment, BoletoPayment


def monta_pedido(forma_pagamento):
    produto = Produto("Fone de ouvido", 89.90)
    return (OrderBuilder()
            .com_cliente("Rafael Souza")
            .com_produto(produto)
            .com_pagamento(forma_pagamento)
            .build())


def test_processa_pedido_com_pix(capsys):
    pedido = monta_pedido("PIX")

    get_payment_processor(pedido.pagamento).process_order(pedido)

    saida = capsys.readouterr().out
    assert "Pix" in saida
    assert "89.9" in saida


def test_processa_pedido_com_boleto(capsys):
    pedido = monta_pedido("BOLETO")

    get_payment_processor(pedido.pagamento).process_order(pedido)

    saida = capsys.readouterr().out
    assert "boleto" in saida


def test_mecanismo_criado_corresponde_a_forma_registrada_no_pedido():
    pedido_pix = monta_pedido("PIX")
    pedido_boleto = monta_pedido("BOLETO")

    pagamento_pix = get_payment_processor(pedido_pix.pagamento).create_payment()
    pagamento_boleto = get_payment_processor(pedido_boleto.pagamento).create_payment()

    assert isinstance(pagamento_pix, PixPayment)
    assert isinstance(pagamento_boleto, BoletoPayment)
