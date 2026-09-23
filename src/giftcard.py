# Questão 8, forma de pagamento nova sem mexer no payment.py

from src.payment import Payment, PaymentProcessor, register_payment_processor


class GiftCardPayment(Payment):
    def pay(self, amount) -> None:
        print(f"Pagamento de {amount} em gift card realizado com sucesso!")


class GiftCardProcessor(PaymentProcessor):
    def create_payment(self) -> Payment:
        return GiftCardPayment()


register_payment_processor("GIFTCARD", GiftCardProcessor)
