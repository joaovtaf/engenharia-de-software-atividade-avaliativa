import pytest

from src.channel import get_channel_factory
import src.kiosk  # só importar já registra o KIOSK, não mexe em channel.py


def test_get_channel_factory_retorna_a_fabrica_registrada():
    assert get_channel_factory("WEB").__class__.__name__ == "WebFactory"
    assert get_channel_factory("MOBILE").__class__.__name__ == "MobileFactory"


def test_canal_desconhecido_gera_erro_claro():
    with pytest.raises(ValueError):
        get_channel_factory("TOTEM_INEXISTENTE")


def test_kiosk_fica_disponivel_so_com_o_import_do_modulo():
    fabrica = get_channel_factory("KIOSK")

    assert fabrica.__class__.__name__ == "KioskFactory"
    assert fabrica.create_checkout().__class__.__name__ == "KioskCheckout"
    assert fabrica.create_notification().__class__.__name__ == "KioskNotification"
