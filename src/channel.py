# Questão 4 e 5

from abc import ABC, abstractmethod

from src.config import AppConfig


class Checkout(ABC):
    @abstractmethod
    def show(self, order):
        pass


class Notification(ABC):
    @abstractmethod
    def send(self, order):
        pass


class ChannelFactory(ABC):
    @abstractmethod
    def create_checkout(self) -> Checkout:
        pass

    @abstractmethod
    def create_notification(self) -> Notification:
        pass


class WebCheckout(Checkout):
    def show(self, order):
        config = AppConfig()
        print(f"[Checkout Web] pedido de {order.cliente}")
        for produto in order.produtos:
            print(f"  {produto.nome}: {config.currency} {produto.preco}")
        print(f"Total: {config.currency} {order.total()}")


class WebNotification(Notification):
    def send(self, order):
        config = AppConfig()
        print(f"[E-mail] {order.cliente}, seu pedido de {config.currency} {order.total()} foi confirmado")


class MobileCheckout(Checkout):
    def show(self, order):
        config = AppConfig()
        print(f"[Checkout Mobile] {len(order.produtos)} item(ns), total {config.currency} {order.total()}")


class MobileNotification(Notification):
    def send(self, order):
        config = AppConfig()
        print(f"[Push] {order.cliente}, pedido de {config.currency} {order.total()} confirmado")


class WebFactory(ChannelFactory):
    def create_checkout(self):
        return WebCheckout()

    def create_notification(self):
        return WebNotification()


class MobileFactory(ChannelFactory):
    def create_checkout(self):
        return MobileCheckout()

    def create_notification(self):
        return MobileNotification()


_factories = {
    "WEB": WebFactory,
    "MOBILE": MobileFactory,
}


def register_channel_factory(channel, factory_cls):
    _factories[channel] = factory_cls


def get_channel_factory(channel):
    factory_cls = _factories.get(channel)
    if factory_cls is None:
        raise ValueError(f"Canal desconhecido: {channel}")
    return factory_cls()
