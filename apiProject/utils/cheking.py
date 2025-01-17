
import json

from requests import Response
"""Методы для проверки ответов наших запросов"""

class Cheking():

    """Метод для проверки статус-кода ответа"""
    @staticmethod
    def check_status_code(result, status_code):
        """Проверяет, совпадает ли статус-код ответа с ожидаемым."""
        assert status_code == result.status_code
        if result.status_code ==status_code:
            print(f"Успешно! Cтатус-код = {result.status_code}")
        else:
            print(f"Провал! Ожидаемый статус-код = {status_code}, получен = {result.status_code}")

    """Метод для проверки наличия обязательных полей в JSON ответе"""
    @staticmethod
    def check_json_token(result,expected_value):
        """Проверяет, что все обязательные ключи присутствуют в JSON ответе."""
        token = json.loads(result.text)
        assert list(token)==expected_value
        print("Все обязательные поля присутствуют.")

    """Метод для проверки значения конкретного поля в JSON ответе"""

    @staticmethod
    def check_json_value(result,field_name,expected_value):
        """Проверяет, что значение указанного поля совпадает с ожидаемым."""
        check=result.json()
        check_info=check.get(field_name)
        assert check_info==expected_value
        print(f"Поле '{field_name}' корректно!")

    """Метод для поиска определенного слова в значении поля JSON ответа"""

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово " + search_word + f" присутствует в поле {field_name}!")
        else:
            print(f"Слово '{search_word}' не найдено в поле '{field_name}'.")
