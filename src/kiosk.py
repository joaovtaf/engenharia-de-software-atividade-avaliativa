# Questão 5, extensão do canal KIOSK sem mexer em channel.py

from src.channel import Checkout, Notification, ChannelFactory, register_channel_factory
from src.config import AppConfig


class KioskCheckout(Checkout):
    def show(self, order):
        config = AppConfig()
        print(f"[Totem] {order.cliente}, confira seu pedido na tela")
        for produto in order.produtos:
            print(f"  {produto.nome}: {config.currency} {produto.preco}")
        print(f"Total: {config.currency} {order.total()}")


class KioskNotification(Notification):
    def send(self, order):
        print(f"[Totem] comprovante do pedido de {order.cliente} liberado pra impressão")


class KioskFactory(ChannelFactory):
    def create_checkout(self):
        return KioskCheckout()

    def create_notification(self):
        return KioskNotification()


register_channel_factory("KIOSK", KioskFactory)
