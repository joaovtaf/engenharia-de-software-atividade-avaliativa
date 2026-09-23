# Testes da forma de pagamento nova, questão 8

from src.config import OrderBuilder, Produto
from src.payment import get_payment_processor, Payment
from src.channel import get_channel_factory
from src.service import OrderService, EventLogger
import src.giftcard  # só importar já registra a forma de pagamento nova


def monta_pedido(forma_pagamento):
    return (OrderBuilder()
            .com_cliente("Bruna Martins")
            .com_produto(Produto("Livro", 60.00))
            .com_pagamento(forma_pagamento)
            .build())


def test_giftcard_fica_registrado_so_com_o_import():
    processor = get_payment_processor("GIFTCARD")

    assert processor.__class__.__name__ == "GiftCardProcessor"


def test_giftcard_cria_um_payment_como_os_outros():
    payment = get_payment_processor("GIFTCARD").create_payment()

    assert isinstance(payment, Payment)
    assert payment.__class__.__name__ == "GiftCardPayment"


def test_fluxo_do_service_nao_muda_com_a_forma_de_pagamento_nova(capsys):
    pedido = monta_pedido("GIFTCARD")

    OrderService(get_payment_processor(pedido.pagamento),
                 get_channel_factory("WEB"),
                 EventLogger()).process(pedido)

    saida = capsys.readouterr().out
    assert "gift card" in saida
    assert "Checkout Web" in saida
