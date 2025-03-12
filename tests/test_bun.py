import pytest
from Diplom_1.praktikum.bun import Bun
from Diplom_1.tests.data import BunData

class TestBun:

    buns=BunData

    @pytest.mark.parametrize('name, price' , buns.parametrize_bun_data)
    def test_bun_get_name(self, name, price):
        bun=Bun(name, price)
        assert  bun.get_name() == name

    @pytest.mark.parametrize('name, price' , buns.parametrize_bun_data)
    def test_bun_get_price(self, name, price):
        bun=Bun(name, price)
        assert  bun.get_price() == price


