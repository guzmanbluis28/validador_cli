from validador.utils import is_valid_email, is_valid_url

def test_email_valido():
    assert is_valid_email("test@example.com") is True

def test_email_invalido():
    assert is_valid_email("test@.com") is False

def test_url_valido():
    assert is_valid_url("https://www.example.com") is True

def test_url_invalido():
    assert is_valid_url("htp://invalid-url") is False
