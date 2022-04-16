import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randrange
from settings import TOKEN_GROUP
from functions import get_final_info_from_couple
token_group = TOKEN_GROUP

vk = vk_api.VkApi(token=token_group)
longpoll = VkLongPoll(vk)

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7)})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        # user = vk.method("users.get", {"user_ids": event.user_id})
        # fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
        # print(fullname)
        if event.to_me:
            request = event.text
            if request.lower() == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}, напиши старт для поиска пары")
            elif request.lower() == "старт":
                write_msg(event.user_id, f"Высылаю подходящих кандидатов для тебя: {get_final_info_from_couple(event.user_id)}")

            elif request.lower() == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")

