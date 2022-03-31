import requests

TOKEN = ''

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def make_folder(self, name_folder):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": name_folder}
        response = requests.put(upload_url, headers=headers, params=params)
        return response.status_code




if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    ya.make_folder('new_folder31_03')