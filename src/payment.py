from abc import ABC, abstractmethod

class Order:
    pass

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
    def create_payment() -> Payment:
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
