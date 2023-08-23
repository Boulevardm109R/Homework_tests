import requests
import unittest


class TestYandexDiskAPI(unittest.TestCase):
    base_url = 'https://cloud-api.yandex.net/v1/disk'
    headers = {
        'Authorization': 'YANDEX TOKEN',
    }

    def test_create_folder_success(self):
        folder_name = 'TestFolder'
        folder_info_url = f'{self.base_url}/resources?path=/{folder_name}'
        response = requests.get(folder_info_url, headers=self.headers)
        if response.status_code == 200:
            self.assertEqual(response.status_code, 200)
        else:
            folder_url = f'{self.base_url}/resources?path=/{folder_name}'
            response = requests.put(folder_url, headers=self.headers)
            self.assertEqual(response.status_code, 201)

        response = requests.get(folder_info_url, headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_create_folder_error(self):
        folder_name = 'TestFolder'
        folder_url = f'{self.base_url}/resources?path=/{folder_name}'
        response = requests.put(folder_url, headers=self.headers)
        self.assertEqual(response.status_code, 409)

    def test_invalid_authorization(self):
        invalid_headers = {
            'Authorization': 'InvalidToken',
        }
        folder_name = 'InvalidTestFolder'
        folder_url = f'{self.base_url}/resources?path=/{folder_name}'
        response = requests.put(folder_url, headers=invalid_headers)
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
