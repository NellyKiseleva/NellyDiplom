import sender_stand_request
import data


# Тест 1. Тест который берет ответ на создание нового заказа

def test_create_order_get_success_response():
    data_user_body = sender_stand_request.post_create_order().json



# Тест 2. Выполнить запрос на получения заказа по треку заказа
def test_order_info_get_track_number():
    track_number = sender_stand_request.get_order_info(data.user_body).json
