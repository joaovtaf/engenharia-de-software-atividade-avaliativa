# Exemplo executável da integração, roda o fluxo completo nos três canais

from src.config import AppConfig, OrderBuilder, Produto
from src.channel import get_channel_factory
from src.payment import get_payment_processor
from src.service import OrderService, EventLogger

# inicialização da aplicação, importar esses dois já registra o canal e o pagamento novos
import src.kiosk
import src.giftcard


def monta_pedido(cliente, forma_pagamento):
    return (OrderBuilder()
            .com_cliente(cliente)
            .com_produto(Produto("Teclado mecânico", 350.00))
            .com_produto(Produto("Mouse gamer", 120.00))
            .com_endereco("Rua das Acácias, 120")
            .com_pagamento(forma_pagamento)
            .build())


def roda_fluxo(canal, pedido):
    print(f"===== canal {canal}, pagamento {pedido.pagamento} =====")

    servico = OrderService(get_payment_processor(pedido.pagamento),
                           get_channel_factory(canal),
                           EventLogger())
    servico.process(pedido)
    print()


config = AppConfig()
print(f"Ambiente: {config.environment}, moeda: {config.currency}, debug: {config.debug}")
print()

roda_fluxo("WEB", monta_pedido("Rafael Souza", "PIX"))
roda_fluxo("MOBILE", monta_pedido("Ana Paula", "CARTAO"))
roda_fluxo("KIOSK", monta_pedido("Carlos Lima", "GIFTCARD"))
