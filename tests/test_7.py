# Os três testes extras pedidos na questão 7

from src.config import AppConfig, OrderBuilder
from src.channel import WebFactory, MobileFactory

# Teste de Singleton
def test_configuracao_inicializa_com_valores_padrao():
    AppConfig._instance = None # Reset forçado para simular primeira chamada isolada
    
    config = AppConfig()
    
    assert config.environment == "production"
    assert config.currency == "BRL"
    assert config.debug is False


# Teste de Builder
def test_builder_constroi_pedido_valido_sem_produtos_com_total_zero():
    pedido = (OrderBuilder()
              .com_cliente("Cliente Sem Compras")
              .build())
    
    assert len(pedido.produtos) == 0
    assert pedido.total() == 0


# Teste de Abstract Factory
def test_fabricas_diferentes_criam_classes_concretas_distintas():
    web_checkout = WebFactory().create_checkout()
    mobile_checkout = MobileFactory().create_checkout()
    
    assert type(web_checkout) is not type(mobile_checkout)
    assert web_checkout.__class__.__name__ == "WebCheckout"
    assert mobile_checkout.__class__.__name__ == "MobileCheckout"