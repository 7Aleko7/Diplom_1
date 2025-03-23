import pytest
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.tests.data import IngredientData

class TestIngredient:
    ingredients = IngredientData()

    @pytest.mark.parametrize('type, name, price', ingredients.parametrize_ingredient_data)
    def test_ingredient_get_type(self,type, name, price):
        ingredient=Ingredient(type, name, price)
        assert ingredient.get_type() == type

    @pytest.mark.parametrize('type, name, price', ingredients.parametrize_ingredient_data)
    def test_ingredient_get_name(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('type, name, price', ingredients.parametrize_ingredient_data)
    def test_ingredient_get_price(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price