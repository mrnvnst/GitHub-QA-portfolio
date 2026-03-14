import random
import requests
import time
import string

from faker import Faker
from helpers.endpoints import Url

faker = Faker()


class Generator:

    _run_prefix = str(int(time.time()))

    @staticmethod
    def email():
        # Создание уникального email для каждого прогона теста с регистрацией
        username = faker.user_name()
        return f"{username}_{Generator._run_prefix}@example.com"

    @staticmethod
    def password():
        return faker.password(length=10)

    @staticmethod
    def name():
        return faker.name()

    @staticmethod
    def user_data():
        return {
            "email": Generator.email(),
            "password": Generator.password(),
            "name": Generator.name()
        }

    @staticmethod
    # Рандомный выбор ингредиентов из списка с обязательным выбором одного из вида булочек
    def random_ingredients(min_count=2, max_count=3):
        ingredients_data = requests.get(Url.GET_INGREDIENTS).json()['data']
        buns = [item for item in ingredients_data if item['type'] == 'bun']
        filling = [item for item in ingredients_data if item['type'] != 'bun']
        # Рандомный выбор булочки
        chosen = [random.choice(buns)]
        # Рандомный выбор ингредиентов
        count = random.randint(min_count - 1, max_count - 1)
        chosen += random.sample(filling, count)
        return [ingredient['_id'] for ingredient in chosen]

    @staticmethod
    def random_invalid_id(length=24):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

