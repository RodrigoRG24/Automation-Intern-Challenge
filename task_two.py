import os
import time

import requests

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.countrylayer.com/v2/'


def request_with_retries(url, method='GET', json=None, max_retries=3, backoff_factor=5):
    retries = 0
    while retries < max_retries:
        if method == 'POST':
            response = requests.post(url, json=json)
        else:
            response = requests.get(url)

        if response.status_code == 200:
            return response
        elif response.status_code == 429:
            wait_time = backoff_factor * (2 ** retries)
            print(f"Demasiadas solicitudes. Esperando {wait_time} segundos...")
            time.sleep(wait_time)
            retries += 1
        else:
            return response
    raise Exception(f"Failed to get a valid response after {max_retries} retries")


def get_country(code):
    url = f'{BASE_URL}alpha/{code}?access_key={API_KEY}'
    response = request_with_retries(url)
    if response.status_code == 200:
        data = response.json()
        print(f"País: {data['name']}, Código Alpha2: {data['alpha2Code']}, Código Alpha3: {data['alpha3Code']}")
    else:
        print(f"Error al obtener el país: {response.status_code}")


def invalid_country(code):
    url = f'{BASE_URL}alpha/{code}?access_key={API_KEY}'
    response = request_with_retries(url)
    if response.status_code in [400, 404]:
        print(f"Respuesta esperada para país inexistente: {response.json()}")
    else:
        print(f"Error inesperado: {response.status_code}")


def post_country():
    url = f'{BASE_URL}all?access_key={API_KEY}'
    json_data = {
        "name": "Test Country",
        "alpha2_code": "TC",
        "alpha3_code": "TCY"
    }
    response = request_with_retries(url, method='POST', json=json_data)
    assert response.status_code in [405, 500], f"Error inesperado: {response.status_code}"
    print("Prueba de POST fallida como se esperaba.")


def main():
    get_country('US')
    get_country('DE')
    get_country('GB')
    invalid_country('ZZ')
    post_country()


if __name__ == '__main__':
    main()
