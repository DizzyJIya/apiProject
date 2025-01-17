from utils import http_methods
from utils.http_methods import Http_method
"""Методы для тестирования GoogleMapsAPI"""
base_url = 'https://rahulshettyacademy.com' #Базовая url
key='?key=qaclick123'       #Параметры для всех запросов
class Google_maps_api():
    """Метод для создания новой локаций"""
    @staticmethod
    def create_new_place():
        json_for_create_new_place = {
            "location": {
            "lat": -38.383494,
            "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
            "shoe park",
            "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"}
        post_resourse='/maps/api/place/add/json' #ресурс метода POST
        post_url=base_url + post_resourse+key
        print(post_url)
        result_post=Http_method.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для Проверки новой локаций"""

    @staticmethod
    def get_new_place(place_id):
        get_resourse='/maps/api/place/get/json'  #ресурс метода GET
        get_url=base_url + get_resourse+key+'&place_id='+place_id
        print(get_url)
        get_result=Http_method.get(get_url)
        print(get_result.text)
        return get_result

    """Метод для изменения новой локаций"""

    @staticmethod
    def put_new_place(place_id):

        put_resourse='/maps/api/place/update/json'
        put_url=base_url + put_resourse+key
        print(put_url)
        json_for_put_new_place = {

            "place_id":place_id,

             "address":"100 Lenina street, RU",

            "key":"qaclick123"

            }
        result_put=Http_method.put(put_url, json_for_put_new_place)
        print(result_put.text)
        return result_put
    """Метод для удаления новой локаций"""
    @staticmethod
    def delete_new_place(place_id):
        delete_resourse = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        json_for_put_new_place = {

"place_id":place_id

}
        result_delete = Http_method.delete(delete_url, json_for_put_new_place)
        print(result_delete.text)
        return result_delete