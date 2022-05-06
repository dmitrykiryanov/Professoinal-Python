import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randrange
from settings import TOKEN_GROUP
from functions import get_final_info_from_couple
import db_work

token_group = TOKEN_GROUP

vk = vk_api.VkApi(token=token_group)
longpoll = VkLongPoll(vk)

person_db = db_work.SqlDataPersons()

def write_msg(user_id, message, attachment=None):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), 'attachment': attachment})
def create_msg(user_id):
    person_db = db_work.SqlDataPersons()
    person_db.create_table()
    # кривая логика, чтобы не выводить повторных кандитатов
    candidates = get_final_info_from_couple(user_id)
    current_couples = person_db.select_data() # т.к. здесь выводятся кортежи, пришлось создавать доп список
    new_current_couples = []
    for ids in current_couples:
        ids = str(ids)
        ids = ids[1:-2]
        new_current_couples.append(ids)
    for key, values in candidates.items():
        if key in new_current_couples:
            continue
        write_msg(event.user_id, "https://vk.com/id" + str(key))
        person_db.insert_info('person', 'ids_couple', key)
        for i in range(len(candidates[key])):
            write_msg(event.user_id, f'Фото {i+1}:', attachment=values[i])

if __name__ == '__main__':
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = event.text
                    if request.lower() == "привет":
                        write_msg(event.user_id, f"Хай, {event.user_id}, напиши старт для поиска пары")
                    elif request.lower() == "старт":
                        create_msg(event.user_id)

                    elif request.lower() == "пока":
                        write_msg(event.user_id, "Пока((")
                    else:
                        write_msg(event.user_id, "Не поняла вашего ответа...")

