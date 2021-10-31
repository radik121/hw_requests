from pprint import pprint
import requests

with open('ya.token.txt', 'r') as file_object:
    token = file_object.read().strip()

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {
            "path": file_path,
            "overwrite": "true"
        }
        link_upload = requests.get(url, headers=headers, params=params)
        # href = link_upload.json()
        upload_file = requests.put(url=link_upload.json().get('href', ''), data=open('file.txt', 'rb'), params=params, headers=headers)
        # if upload_file.status_code == 201:
        # print("Success")
        return 'Файл загружен успешно!'


if __name__ == '__main__':
    uploader = YaUploader(token)
    print(uploader.upload('netology/file.txt'))