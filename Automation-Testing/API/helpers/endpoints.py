class Url:
    MAIN_URL = 'https://stellarburgers.education-services.ru'
    # Ручка регистрации POST
    CREATE_USER = f"{MAIN_URL}/api/auth/register"
    # Ручка авторизации POST
    LOGIN_USER = f"{MAIN_URL}/api/auth/login"
    # Ручка создания заказа POST
    CREATE_ORDER = f"{MAIN_URL}/api/orders"
    # Ручка удаления пользователя DELETE
    DELETE_USER = f"{MAIN_URL}/api/auth/user"
    # Ручка получения данных об ингредиентах
    GET_INGREDIENTS = f"{MAIN_URL}/api/ingredients"
    # Получение данных о пользователе
    GET_USER_INFO = f"{MAIN_URL}/api/auth/user"
