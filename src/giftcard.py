# Questão 8

from src.payment import Payment, PaymentProcessor

class GiftCardPayment(Payment):
    def pay(self, amount) -> None:
        print(f"Pagamento de {amount} em GiftCard realizado com sucesso.")

class GiftCardProcessor(PaymentProcessor):
    def create_payment(self) -> Payment:
        return GiftCardPayment()