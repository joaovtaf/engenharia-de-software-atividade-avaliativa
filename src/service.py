# Questão 6, coordenação do fluxo do pedido e o registro de eventos

class EventLogger:
    def log(self, order):
        print(f"[log] pedido de {order.cliente} processado, total {order.total()}")


class OrderService:
    def __init__(self, payment_processor, channel_factory, logger):
        self.payment_processor = payment_processor
        self.channel_factory = channel_factory
        self.logger = logger

    def process(self, order):
        checkout = self.channel_factory.create_checkout()
        notification = self.channel_factory.create_notification()

        checkout.show(order)
        self.payment_processor.process_order(order)
        notification.send(order)
        self.logger.log(order)
