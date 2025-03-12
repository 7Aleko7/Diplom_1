from unittest.mock import Mock
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.burger import Burger



class TestBurger:

    def test_burger_set_buns(self):
        bun_mock = Mock(spec= Bun)
        burger = Burger()
        burger.set_buns(bun_mock)

        assert burger.bun == bun_mock

    def test_burger_add_ingredient(self):
        ingredient_mock = Mock(spec= Ingredient)
        burger = Burger()
        burger.add_ingredient(ingredient_mock)

        assert ingredient_mock in burger.ingredients

    def test_burger_remove_ingredient(self):
        ingredient_mock = Mock(spec= Ingredient)
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)

        assert ingredient_mock not in burger.ingredients

    def test_burger_move_ingredient(self):
        first_ingredient_mock = Mock(spec=Ingredient)
        second_ingredient_mock = Mock(spec=Ingredient)
        burger = Burger()
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [second_ingredient_mock, first_ingredient_mock]

    def test_burger_get_price(self):
        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = 10

        first_ingredient_mock = Mock(spec=Ingredient)
        first_ingredient_mock.get_price.return_value = 5.8
        second_ingredient_mock = Mock(spec=Ingredient)
        second_ingredient_mock.get_price.return_value = 1.9

        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)

        assert burger.get_price() == 27.7

    def test_burger_get_receipt(self):
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = 'С кунжутом'
        bun_mock.get_price.return_value = 30

        first_ingredient_mock = Mock(spec=Ingredient)
        first_ingredient_mock.get_type.return_value = 'SAUCE'
        first_ingredient_mock.get_name.return_value = 'Кисло-сладкий'
        first_ingredient_mock.get_price.return_value = 5

        second_ingredient_mock = Mock(spec=Ingredient)
        second_ingredient_mock.get_type.return_value = 'FILLING'
        second_ingredient_mock.get_name.return_value = 'Сыр'
        second_ingredient_mock.get_price.return_value = 10.5

        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)

        expected_receipt = ("(==== С кунжутом ====)\n"
            "= sauce Кисло-сладкий =\n"
            "= filling Сыр =\n"
            "(==== С кунжутом ====)\n\n"
            "Price: 75.5")

        assert burger.get_receipt() == expected_receipt
