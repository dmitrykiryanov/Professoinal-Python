from settings import TOKEN_U
import datetime
import vk_api
from pprint import pprint

from random import randrange

token_u = TOKEN_U
vk = vk_api.VkApi(token=token_u)

# получаем данные о пользователе, для которого подбираем пару
def get_user_data(user_id):
    user_data = vk.method("users.get", {"user_ids": user_id, "fields": "bdate,sex,city,relation"})[0]
    return user_data
# подбираем кандидатов на основании данных о пользователе (возраст, пол, город, семейное положение)
def search_couple(user_id):
    search_param = {}
    if get_user_data(user_id)['sex'] == 2:
        search_param['sex'] = 1
    else:
        search_param['sex'] = 2
    user_age = int(datetime.datetime.now().strftime('%Y')) - int(get_user_data(user_id)['bdate'].split('.')[-1])
    search_param['age_from'] = user_age - 1
    search_param['age_to'] = user_age + 1
    search_param['city'] = get_user_data(user_id)['city']['id']
    search_param['status'] = 6
    search_param['has_foto'] = 1
    search_param['count'] = 10
    search_param['offset'] = randrange(0, 50, 5)  # интуитивно понимаю, что офсет должен меняться, но каким образом?
    search_param['fields'] = 'city'
    couple_for_user = vk.method("users.search", search_param)['items']
    for i, couple in enumerate(couple_for_user, 0):  # отбираем кандидатов с открытым профилем
        if couple['is_closed'] == True:
            couple_for_user.pop(i)
    return couple_for_user
# получаем список отсортированных по популярности фотографий кандидата
def get_best_photo(id):
    couples_photo = vk.method('photos.get', {'owner_id': id, 'album_id': 'profile', 'extended': 1})
    photo_dict = {}
    for photo in couples_photo['items']:
        photo_grade = int(photo['likes']['count']) + int(photo['comments']['count'])
        photo_id = photo['id']
        owner_id = photo['owner_id']
        # print(photo_url)
        photo_dict.setdefault(photo_grade, f'photo{owner_id}_{photo_id}')
    best_photo_list = sorted(photo_dict.items(), reverse=True)

    return best_photo_list
def get_final_info_from_couple(user_id):
    final_info = {}
    couples = search_couple(user_id)
    list_ids = []  # список id кандидатов, чтобы убрать повторяющиеся id
    for couple in couples:
        id_couple = couple['id']
        if id_couple not in list_ids:
            list_ids.append(id_couple)
            if len(get_best_photo(id_couple)) < 3:
                continue
            final_info[id_couple] = [get_best_photo(id_couple)[0][1], get_best_photo(id_couple)[1][1],
                                     get_best_photo(id_couple)[2][1]]

    return final_info
