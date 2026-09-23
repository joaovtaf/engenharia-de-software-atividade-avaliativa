# Testes do fluxo completo coordenado pelo OrderService, questão 6

from src.config import OrderBuilder, Produto
from src.channel import get_channel_factory
from src.payment import PixProcessor, CreditCardProcessor
from src.service import OrderService, EventLogger
import src.kiosk  # registra o KIOSK antes do fluxo usar esse canal


def monta_pedido():
    produto1 = Produto("Teclado mecânico", 350.00)
    produto2 = Produto("Mouse gamer", 120.00)
    return (OrderBuilder()
            .com_cliente("Rafael Souza")
            .com_produto(produto1)
            .com_produto(produto2)
            .build())


def test_fluxo_completo_pelo_canal_web(capsys):
    logger = EventLogger()
    pedido = monta_pedido()

    OrderService(PixProcessor(), get_channel_factory("WEB"), logger).process(pedido)

    saida = capsys.readouterr().out
    assert "Checkout Web" in saida
    assert "Pix" in saida
    assert "E-mail" in saida
    assert "log" in saida


def test_fluxo_completo_pelo_canal_kiosk(capsys):
    logger = EventLogger()
    pedido = monta_pedido()

    OrderService(CreditCardProcessor(), get_channel_factory("KIOSK"), logger).process(pedido)

    saida = capsys.readouterr().out
    assert "Totem" in saida
    assert "cartão de crédito" in saida
    assert "log" in saida
