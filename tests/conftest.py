import pytest

@pytest.fixture
def numeros_enteros():
    return 3,4

@pytest.fixture
def numeros_decimales():
    return .1, .2