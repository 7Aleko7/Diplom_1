from Diplom_1.praktikum.database import Database
from Diplom_1.tests.data import BunData, IngredientData

class TestDatabase:

    def test_database_available_buns(self):
        db=Database()
        bun = BunData()
        buns=db.available_buns()

        assert len(buns) == 3
        assert buns[0].get_name() == bun.appends_db_first_bun['name']
        assert buns[0].get_price() == bun.appends_db_first_bun['price']
        assert buns[1].get_name() == bun.appends_db_second_bun['name']
        assert buns[1].get_price() == bun.appends_db_second_bun['price']
        assert buns[2].get_name() == bun.appends_db_third_bun['name']
        assert buns[2].get_price() == bun.appends_db_third_bun['price']


    def test_database_available_ingredients(self):
        db = Database()
        ingredient = IngredientData()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6

        assert ingredients[0].get_type() == ingredient.appends_db_first_sauce_ingredient['type']
        assert ingredients[0].get_name() == ingredient.appends_db_first_sauce_ingredient['name']
        assert ingredients[0].get_price() == ingredient.appends_db_first_sauce_ingredient['price']
        assert ingredients[1].get_type() == ingredient.appends_db_second_sauce_ingredient['type']
        assert ingredients[1].get_name() == ingredient.appends_db_second_sauce_ingredient['name']
        assert ingredients[1].get_price() == ingredient.appends_db_second_sauce_ingredient['price']
        assert ingredients[2].get_type() == ingredient.appends_db_third_sauce_ingredient['type']
        assert ingredients[2].get_name() == ingredient.appends_db_third_sauce_ingredient['name']
        assert ingredients[2].get_price() == ingredient.appends_db_third_sauce_ingredient['price']

        assert ingredients[3].get_type() == ingredient.appends_db_first_filling_ingredient['type']
        assert ingredients[3].get_name() == ingredient.appends_db_first_filling_ingredient['name']
        assert ingredients[3].get_price() == ingredient.appends_db_first_filling_ingredient['price']
        assert ingredients[4].get_type() == ingredient.appends_db_second_filling_ingredient['type']
        assert ingredients[4].get_name() == ingredient.appends_db_second_filling_ingredient['name']
        assert ingredients[4].get_price() == ingredient.appends_db_second_filling_ingredient['price']
        assert ingredients[5].get_type() == ingredient.appends_db_third_filling_ingredient['type']
        assert ingredients[5].get_name() == ingredient.appends_db_third_filling_ingredient['name']
        assert ingredients[5].get_price() == ingredient.appends_db_third_filling_ingredient['price']




