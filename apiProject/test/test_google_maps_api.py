import json
import allure
from itertools import count

from requests import Response

from utils import cheking
from utils.api import Google_maps_api
from utils.cheking import Cheking
"""Создание, изменение и удаление новой локаций"""
@allure.epic("Test create place")
class Test_create_place():

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("Метод POST")
        result_post = Google_maps_api.create_new_place()
        check_post=result_post.json()
        place_id = check_post.get("place_id")
        Cheking.check_status_code(result_post,200)
        Cheking.check_json_token(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод Get после POST")
        result_get=Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'address', '29, side layout, cohen 09')


        print('Метод PUT')
        result_put=Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put, ['msg'])
        Cheking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод Get после PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Cheking.check_json_value(result_get, 'address', '100 Lenina street, RU')


        print('Метод Delete')
        result_delete = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete, ['status'])
        Cheking.check_json_value(result_delete, 'status', 'OK')

        print('Метод GET после DELETE')
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_token(result_get, ['msg'])
        Cheking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print("Тестирование Создание, изменения и удаление новой локаций прошло успешно!!!")


