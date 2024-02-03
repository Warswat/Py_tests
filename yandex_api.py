import requests


token = " token "

headers = {'Authorization': token}

folder_path = "testovichok/"


def check_disk_for_folder(headers,path):
    response = requests.get('https://cloud-api.yandex.net/v1/disk/resources', params={'path': path}, headers=headers)
    return response


def create_folder(headers,path):
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params={'path': path}, headers=headers)
    return response
