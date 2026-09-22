from src.config import AppConfig


def test_duas_instancias_sao_o_mesmo_objeto():
    config1 = AppConfig()
    config2 = AppConfig()
    assert config1 is config2


def test_alteracao_em_uma_referencia_aparece_na_outra():
    config1 = AppConfig()
    config2 = AppConfig()

    config1.environment = "development"

    assert config2.environment == "development"


def test_valor_alterado_nao_e_restaurado_numa_nova_chamada():
    config1 = AppConfig()
    config1.debug = True

    config2 = AppConfig()

    assert config2.debug is True
