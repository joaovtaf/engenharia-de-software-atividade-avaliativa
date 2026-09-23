# Questão 3, formas de pagamento e os processors que criam elas (Factory Method)

from abc import ABC, abstractmethod

from src.config import Order

class Payment(ABC):
    @abstractmethod
    def pay(self, amount) -> None:
        pass

class PixPayment(Payment):
    def pay(self, amount) -> None:
        print(f"Pagamento de {amount} com Pix realizado com sucesso!")

class CreditCardPayment(Payment):
    def pay(self, amount) -> None:
        print(f"Pagamento de {amount} com cartão de crédito realizado com sucesso!")

class BoletoPayment(Payment):
    def pay(self, amount) -> None:
        print(f"Pagamento de {amount} com boleto realizado com sucesso!")

class PaymentProcessor(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        pass

    def process_order(self, order : Order) -> None:
        self.create_payment().pay(order.total())

class PixProcessor(PaymentProcessor):
    def create_payment(self):
        return PixPayment()
    
class CreditCardProcessor(PaymentProcessor):
    def create_payment(self):
        return CreditCardPayment()

class BoletoProcessor(PaymentProcessor):
    def create_payment(self):
        return BoletoPayment()


_processors = {
    "PIX": PixProcessor,
    "CARTAO": CreditCardProcessor,
    "BOLETO": BoletoProcessor,
}


def register_payment_processor(forma, processor_cls):
    _processors[forma] = processor_cls


def get_payment_processor(forma):
    processor_cls = _processors.get(forma)
    if processor_cls is None:
        raise ValueError(f"Forma de pagamento desconhecida: {forma}")
    return processor_cls()
