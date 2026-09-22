from src.config import OrderBuilder, Produto
from src.payment import PixProcessor, BoletoProcessor, PixPayment


def monta_pedido(forma_pagamento):
    produto = Produto("Fone de ouvido", 89.90)
    return (OrderBuilder()
            .com_cliente("Rafael Souza")
            .com_produto(produto)
            .com_pagamento(forma_pagamento)
            .build())


def test_processa_pedido_com_pix(capsys):
    pedido = monta_pedido("pix")

    PixProcessor().process_order(pedido)

    saida = capsys.readouterr().out
    assert "Pix" in saida


def test_processa_pedido_com_boleto(capsys):
    pedido = monta_pedido("boleto")

    BoletoProcessor().process_order(pedido)

    saida = capsys.readouterr().out
    assert "boleto" in saida


def test_forma_de_pagamento_do_pedido_corresponde_ao_processor_usado():
    pedido = monta_pedido("pix")

    payment = PixProcessor().create_payment()

    assert pedido.pagamento == "pix"
    assert isinstance(payment, PixPayment)
